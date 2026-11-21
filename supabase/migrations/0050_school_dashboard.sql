-- Management dashboard: one call that returns a school's numbers for a period (a term, or any dates).
-- Everything is counted in Postgres so the page, the CSV and any later report agree. School admins only.

alter table public.schools add column if not exists pass_mark numeric(5,2) not null default 50 check (pass_mark between 0 and 100);

create or replace function public.school_dashboard(p_from date default null, p_to date default null, p_term uuid default null)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare s uuid := public.my_school(); f date; t date; pm numeric; r jsonb; tid uuid;
begin
  if s is null or not (public.is_school_admin_of(s) or public.is_platform_admin()) then raise exception 'You do not have permission to do that.'; end if;
  select pass_mark into pm from public.schools where id = s;
  -- the period: a term if given, else the dates, else the current term, else the last 90 days
  if p_term is not null then select id, starts_on, ends_on into tid, f, t from public.academic_terms where id = p_term and school_id = s; end if;
  if f is null and p_from is not null then f := p_from; t := coalesce(p_to, current_date); end if;
  if f is null then select id, starts_on, ends_on into tid, f, t from public.academic_terms where school_id = s and current_date between starts_on and ends_on limit 1; end if;
  if f is null then f := current_date - 90; t := current_date; end if;
  -- results come from the chosen term, or the latest term that has results
  if tid is null then
    select r2.term_id into tid from public.term_reports r2 join public.academic_terms a on a.id = r2.term_id
     where r2.school_id = s and a.starts_on <= t order by a.starts_on desc limit 1;
  end if;

  with st as (select p.id, p.class_id, p.enrolment_status, p.class_level, p.created_at from public.profiles p where p.school_id = s and p.role = 'student'),
  cur as (select * from st where enrolment_status in ('active','suspended'))
  select jsonb_build_object(
    'period', jsonb_build_object('from', f, 'to', t, 'term_id', tid,
                'results_term', (select name from public.academic_terms where id = tid), 'pass_mark', pm),

    'enrolment', jsonb_build_object(
      'current', (select count(*) from cur),
      'by_status', (select coalesce(jsonb_object_agg(enrolment_status, n), '{}') from (select enrolment_status, count(*) n from st group by 1) x),
      'by_class', (select coalesce(jsonb_agg(jsonb_build_object('class', c.name, 'grade', c.grade, 'students', (select count(*) from cur where cur.class_id = c.id)) order by c.grade, c.name), '[]')
                   from public.classes c where c.school_id = s and not c.archived),
      'joined', (select count(*) from st where coalesce((select admitted_on from public.student_records sr where sr.student_id = st.id), st.created_at::date) between f and t),
      'left', (select count(distinct e.student_id) from public.enrolment_events e where e.school_id = s and e.to_status in ('withdrawn','transferred','graduated') and e.effective_on between f and t),
      'months', (select coalesce(jsonb_agg(jsonb_build_object('month', to_char(m, 'YYYY-MM'),
                    'joined', (select count(*) from st where coalesce((select admitted_on from public.student_records sr where sr.student_id = st.id), st.created_at::date) >= m and coalesce((select admitted_on from public.student_records sr where sr.student_id = st.id), st.created_at::date) < m + interval '1 month'),
                    'left', (select count(distinct e.student_id) from public.enrolment_events e where e.school_id = s and e.to_status in ('withdrawn','transferred','graduated') and e.effective_on >= m and e.effective_on < m + interval '1 month')) order by m), '[]')
                 from generate_series(date_trunc('month', current_date) - interval '11 months', date_trunc('month', current_date), interval '1 month') m)),

    'admissions', (select jsonb_build_object('received', coalesce(sum(n), 0), 'by_status', coalesce(jsonb_object_agg(status, n) filter (where status is not null), '{}'))
                   from (select a.status, count(*) n from public.applications a where a.school_id = s and a.created_at::date between f and t group by 1) x),

    'results', jsonb_build_object(
      'reports', (select count(*) from public.term_reports where term_id = tid),
      'published', (select count(*) from public.term_reports where term_id = tid and published_at is not null),
      'average', (select round(avg(score), 1) from public.term_results where term_id = tid and score is not null),
      'pass_rate', (select round(100.0 * count(*) filter (where score >= pm) / nullif(count(*), 0), 1) from public.term_results where term_id = tid and score is not null),
      'by_subject', (select coalesce(jsonb_agg(jsonb_build_object('subject', subject, 'entries', n, 'average', av, 'pass_rate', pr) order by pr nulls last, subject), '[]') from (
                      select subject, count(*) n, round(avg(score), 1) av, round(100.0 * count(*) filter (where score >= pm) / count(*), 1) pr
                      from public.term_results where term_id = tid and score is not null group by subject) x),
      'by_class', (select coalesce(jsonb_agg(jsonb_build_object('class', class_name, 'students', n, 'average', av, 'pass_rate', pr) order by class_name), '[]') from (
                    select r2.class_name, count(distinct r2.student_id) n, round(avg(x.score), 1) av,
                           round(100.0 * count(x.*) filter (where x.score >= pm) / nullif(count(x.score), 0), 1) pr
                    from public.term_reports r2 left join public.term_results x on x.term_id = r2.term_id and x.student_id = r2.student_id and x.score is not null
                    where r2.term_id = tid group by r2.class_name) y)),

    'attendance', jsonb_build_object(
      'rate', (select round(100.0 * count(*) filter (where a.status in ('present','late')) / nullif(count(*) filter (where a.status <> 'excused'), 0), 1)
               from public.attendance a join public.classes c on c.id = a.class_id where c.school_id = s and a.day between f and t),
      'days_marked', (select count(distinct a.day) from public.attendance a join public.classes c on c.id = a.class_id where c.school_id = s and a.day between f and t),
      'below_90', (select count(*) from (select a.student_id from public.attendance a join public.classes c on c.id = a.class_id
                     where c.school_id = s and a.day between f and t and a.status <> 'excused' group by a.student_id
                     having count(*) filter (where a.status in ('present','late')) < 0.9 * count(*)) x),
      'by_class', (select coalesce(jsonb_agg(jsonb_build_object('class', c.name, 'rate', x.rate) order by c.grade, c.name), '[]') from public.classes c
                   join (select a.class_id, round(100.0 * count(*) filter (where a.status in ('present','late')) / nullif(count(*) filter (where a.status <> 'excused'), 0), 1) rate
                         from public.attendance a where a.day between f and t group by a.class_id) x on x.class_id = c.id where c.school_id = s)),

    'fees', (select coalesce(jsonb_agg(jsonb_build_object('currency', cur, 'billed', billed, 'paid', paid, 'outstanding', greatest(billed - paid, 0), 'overdue', od,
                     'collected_in_period', (select coalesce(sum(y.amount), 0) from public.fee_payments y join public.fees z on z.id = y.fee_id
                                             where y.school_id = s and y.voided_at is null and z.currency_code = q.cur and y.paid_on between f and t))), '[]')
             from (select currency_code cur, sum(amount) billed, sum(paid) paid,
                          sum(greatest(0, case when exists (select 1 from public.fee_instalments i where i.fee_id = fe.id)
                                               then (select coalesce(sum(i.amount), 0) from public.fee_instalments i where i.fee_id = fe.id and i.due_on <= current_date) - fe.paid
                                               when fe.due_on <= current_date then fe.amount - fe.paid else 0 end)) od
                   from public.fees fe where fe.school_id = s group by currency_code) q),

    'behaviour', jsonb_build_object(
      'merits', (select count(*) from public.behaviour_entries where school_id = s and kind = 'merit' and occurred_on between f and t),
      'concerns', (select count(*) from public.behaviour_entries where school_id = s and kind in ('concern','incident') and occurred_on between f and t),
      'students_3plus', (select count(*) from (select student_id from public.behaviour_entries where school_id = s and kind in ('concern','incident') and occurred_on between f and t group by 1 having count(*) >= 3) x),
      'top_concerns', (select coalesce(jsonb_agg(jsonb_build_object('category', c, 'n', n) order by n desc), '[]') from (
                        select coalesce(category, 'Other') c, count(*) n from public.behaviour_entries where school_id = s and kind in ('concern','incident') and occurred_on between f and t group by 1 order by 2 desc limit 5) x)),

    'teachers', (select coalesce(jsonb_agg(jsonb_build_object('name', p.first_name || ' ' || p.surname, 'role', p.role,
                    'classes', (select count(distinct ts.class_id) from public.teacher_subjects ts join public.classes c on c.id = ts.class_id where ts.teacher_id = p.id and not c.archived),
                    'subjects', (select string_agg(distinct ts.subject, ', ') from public.teacher_subjects ts where ts.teacher_id = p.id),
                    'students', (select count(distinct q.id) from public.teacher_subjects ts join public.profiles q on q.class_id = ts.class_id and q.role = 'student' and q.enrolment_status in ('active','suspended') where ts.teacher_id = p.id),
                    'periods', (select count(*) from public.timetable_slots tt where tt.teacher_id = p.id),
                    'hours', (select round(coalesce(sum(extract(epoch from (tt.ends - tt.starts)) / 3600), 0)::numeric, 1) from public.timetable_slots tt where tt.teacher_id = p.id),
                    'assessments', (select count(*) from public.assessments a where a.created_by = p.id and a.created_at::date between f and t),
                    'tasks', (select count(*) from public.tasks k where k.created_by = p.id and k.created_at::date between f and t),
                    'last_seen', p.last_seen_at) order by p.surname), '[]')
                 from public.profiles p where p.school_id = s and p.role in ('teacher','subject_teacher','school_admin'))
  ) into r;
  return r;
end $$;
revoke all on function public.school_dashboard(date, date, uuid) from public, anon;
grant execute on function public.school_dashboard(date, date, uuid) to authenticated;
