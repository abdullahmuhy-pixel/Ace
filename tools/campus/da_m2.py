"""Introduction to Data Analysis, module 2: Data wrangling with pandas.
Every printed output quoted in this module is produced by running the code (py_common.check)."""
from verify import Q
from py_common import check
T1, T2, T3, T4 = ('Loading and inspecting data', 'Cleaning: missing values, types and duplicates', 'Filtering, sorting and grouping', 'Joining and reshaping tables')

H = "import pandas as pd\ndf = pd.DataFrame({'city': ['Lagos', 'Accra', 'Nairobi', 'Lagos', 'Accra'], 'sales': [120, 80, 95, 150, 60]})\n"
check(H + "print(df.shape)", "(5, 2)")
check(H + "print(df['sales'].mean())", "101.0")
check(H + "print(df['city'].nunique())", "3")
check(H + "print(df['city'].value_counts().iloc[0])", "2")
check(H + "print(len(df[df['sales'] > 90]))", "3")
check(H + "print(df.sort_values('sales', ascending=False)['city'].iloc[0])", "Lagos")
check(H + "print(df[(df['city'] == 'Lagos') & (df['sales'] > 130)].shape[0])", "1")
check(H + "print(df.groupby('city')['sales'].sum().to_dict())", "{'Accra': 140, 'Lagos': 270, 'Nairobi': 95}")
check(H + "print(df.groupby('city')['sales'].mean().to_dict())", "{'Accra': 70.0, 'Lagos': 135.0, 'Nairobi': 95.0}")
S = "import pandas as pd\ns = pd.Series([10, None, 30, None, 50])\n"
check(S + "print(s.isna().sum())", "2")
check(S + "print(s.mean())", "30.0")
check(S + "print(s.fillna(0).mean())", "18.0")
check(S + "print(len(s.dropna()))", "3")
check("import pandas as pd\nd = pd.DataFrame({'id': [1, 2, 2, 3], 'v': [5, 6, 6, 7]})\nprint(d.duplicated().sum(), len(d.drop_duplicates()))", "1 3")
check("import pandas as pd\nt = pd.to_numeric(pd.Series(['1', '2', 'x']), errors='coerce')\nprint(t.sum(), t.isna().sum())", "3.0 1")
J = "import pandas as pd\norders = pd.DataFrame({'order': [1, 2, 3, 4], 'cust': ['A', 'B', 'A', 'D']})\ncust = pd.DataFrame({'cust': ['A', 'B', 'C'], 'name': ['Ama', 'Bola', 'Chidi']})\n"
check(J + "print(len(orders.merge(cust, on='cust')))", "3")
check(J + "print(len(orders.merge(cust, on='cust', how='left')))", "4")
check(J + "print(orders.merge(cust, on='cust', how='left')['name'].isna().sum())", "1")
check(J + "print(len(orders.merge(cust, on='cust', how='outer')))", "5")
W = "import pandas as pd\nw = pd.DataFrame({'shop': ['X', 'Y'], 'Jan': [10, 20], 'Feb': [15, 25], 'Mar': [12, 30]})\nlong = w.melt(id_vars='shop', var_name='month', value_name='sales')\n"
check(W + "print(long.shape)", "(6, 3)")
check(W + "print(long['sales'].sum())", "112")
check(W + "print(long.pivot(index='shop', columns='month', values='sales').shape)", "(2, 3)")

MODULE = {
    'title': 'Data wrangling with pandas',
    'topics': [T1, T2, T3, T4],
    'overview': 'Most of an analyst\'s time goes into getting data ready. This module uses Python\'s pandas library to load and inspect tables, clean missing values, wrong types and duplicates, filter, sort and summarise by group, and combine and reshape tables. Every output shown was produced by running the code.',
    'key_terms': ['DataFrame', 'Series', 'Index', 'dtype', 'Missing value (NaN)', 'Imputation', 'Duplicate', 'Boolean mask', 'Group-by', 'Aggregation', 'Merge', 'Inner join', 'Left join', 'Wide and long format', 'Melt and pivot'],
    'explanation': [
        'A pandas DataFrame is a table whose columns are Series. Load files with pd.read_csv or pd.read_excel, then inspect: df.shape (rows, columns), df.head(), df.info() (types and missing counts) and df.describe() (summary statistics).',
        'Cleaning comes next: count and handle missing values (isna, dropna, fillna), convert columns to the right type (pd.to_numeric, pd.to_datetime), and remove duplicates. Each choice changes the results, so record what you did and why.',
        'Analysis then filters rows with Boolean masks, sorts, and summarises by group with groupby and aggregation functions. Real projects combine several tables with merge (joins) and reshape between wide and long formats with melt and pivot.'],
    'quick_facts': [
        'df.shape → (rows, columns); df.info() shows types and missing counts.',
        'isna().sum() counts missing; mean() skips NaN.',
        'df[df[col] > x] filters; use & and | with brackets for combined conditions.',
        'df.groupby(key)[col].agg(...) summarises by group.',
        'merge how=inner keeps matches; left keeps all left rows.'],
}

NOTES = {
    T1: {
        'overview': 'Loading and inspecting data tells you what you are working with before you change anything.',
        'key_terms': ['pandas', 'DataFrame', 'Series', 'read_csv', 'shape', 'head', 'info', 'describe', 'dtype', 'value_counts'],
        'explanation': [
            'import pandas as pd, then df = pd.read_csv("sales.csv") loads a file into a DataFrame. For a small example we can build one directly: df = pd.DataFrame({"city": ["Lagos", "Accra", "Nairobi", "Lagos", "Accra"], "sales": [120, 80, 95, 150, 60]}).',
            'print(df.shape) gives (5, 2): five rows and two columns. df.head() shows the first rows; df.info() lists each column\'s dtype (int64, float64, object or string, datetime64) and how many non-missing values it has; df.describe() gives count, mean, SD, min, quartiles and max for numerical columns.',
            'For a single column: df["sales"].mean() gives 101.0; df["city"].nunique() gives 3 distinct cities; df["city"].value_counts() counts each category, largest first (Lagos and Accra each appear 2 times). Always check the row count and types against what you expected.'],
        'formulas_label': 'Code',
        'formulas': ['pd.read_csv(path)', 'df.shape, df.head(), df.info(), df.describe()', 'df["col"].mean(), .nunique(), .value_counts()'],
        'steps': ['Load the file.', 'Check shape against the expected row count.', 'Check dtypes and missing counts with info().', 'Summarise key columns.'],
        'worked_example': {
            'problem': 'For the five-row sales DataFrame, what do df.shape and df["sales"].mean() print?',
            'steps': ['There are 5 rows and 2 columns, so shape is (5, 2).', 'Sales sum to 120 + 80 + 95 + 150 + 60 = 505.', 'Mean = 505/5 = 101.0 (pandas prints a float).'],
            'answer': '(5, 2) and 101.0.',
            'check': 'Running the code prints exactly these values ✓.'},
        'mistakes': ['Skipping inspection and analysing wrongly typed columns.', 'Confusing df.shape (an attribute) with a method call.', 'Forgetting that numbers read as text have dtype object.', 'Not checking the row count after loading.'],
        'real_world': 'Analysts at banks and retailers start every project with the same inspection steps, because a single mis-typed column can ruin a report.',
        'exam_strategy': 'When asked what code prints, work it out by hand step by step; pandas follows the same arithmetic you would.',
        'recap': ['Load.', 'Shape and types.', 'Describe.', 'Value counts.']},
    T2: {
        'overview': 'Real data is messy. Cleaning decisions about missing values, types and duplicates directly affect results.',
        'key_terms': ['NaN', 'isna', 'dropna', 'fillna', 'Imputation', 'to_numeric', 'errors="coerce"', 'duplicated', 'drop_duplicates', 'Data-cleaning log'],
        'explanation': [
            'Missing values appear as NaN. For s = pd.Series([10, None, 30, None, 50]): s.isna().sum() is 2. s.mean() skips missing values and gives 30.0. Filling with zero, s.fillna(0).mean(), gives 18.0, a very different answer. s.dropna() keeps 3 values. Choose based on why values are missing; zero is rarely a safe fill.',
            'Wrong types are common: numbers stored as text, dates as strings. pd.to_numeric(pd.Series(["1", "2", "x"]), errors="coerce") turns "x" into NaN, so the sum is 3.0 with 1 missing value. pd.to_datetime does the same for dates.',
            'Duplicates inflate counts and totals. For a table with rows (1, 5), (2, 6), (2, 6), (3, 7), d.duplicated().sum() is 1 and d.drop_duplicates() keeps 3 rows. Decide which columns define a duplicate (often an ID), and keep a log of every cleaning step so the analysis can be repeated.'],
        'formulas_label': 'Code',
        'formulas': ['s.isna().sum()', 's.dropna(), s.fillna(value)', 'pd.to_numeric(s, errors="coerce")', 'df.duplicated().sum(), df.drop_duplicates()'],
        'steps': ['Count missing values per column.', 'Decide to drop, fill or flag, with a reason.', 'Fix types.', 'Remove duplicates and log every step.'],
        'worked_example': {
            'problem': 's = pd.Series([10, None, 30, None, 50]). What do s.mean() and s.fillna(0).mean() print, and why do they differ?',
            'steps': ['s.mean() uses the 3 present values: (10 + 30 + 50)/3 = 30.0.', 's.fillna(0) gives [10, 0, 30, 0, 50]; mean = 90/5 = 18.0.', 'Filling with 0 pretends the missing values were zero.'],
            'answer': '30.0 and 18.0; filling with zero drags the mean down.',
            'check': 'Running the code prints 30.0 and 18.0 ✓.'},
        'mistakes': ['Filling missing values with 0 without thinking.', 'Deleting all rows with any missing value and losing most data.', 'Leaving numbers stored as text.', 'Removing "duplicates" that are genuinely repeated events.'],
        'real_world': 'Health ministries cleaning facility reports must decide whether a blank means "no cases" or "not reported"; the two give very different disease estimates.',
        'exam_strategy': 'For any cleaning question, state the assumption your choice makes about the missing or duplicated data.',
        'recap': ['Count NaNs.', 'Drop, fill or flag with reasons.', 'Fix types.', 'De-duplicate carefully.']},
    T3: {
        'overview': 'Filtering, sorting and grouping turn a clean table into answers.',
        'key_terms': ['Boolean mask', 'Logical and (&)', 'Logical or (|)', 'sort_values', 'groupby', 'Aggregation', 'agg', 'Split-apply-combine'],
        'explanation': [
            'A Boolean mask selects rows: df[df["sales"] > 90] keeps rows where sales exceed 90 (3 rows). Combine conditions with & and |, each in brackets: df[(df["city"] == "Lagos") & (df["sales"] > 130)] has 1 row. sort_values("sales", ascending=False) puts the largest first; its first city is Lagos.',
            'groupby follows split-apply-combine: split rows by a key, apply a function to each group, combine the results. df.groupby("city")["sales"].sum() gives Accra 140, Lagos 270 and Nairobi 95; .mean() gives Accra 70.0, Lagos 135.0 and Nairobi 95.0.',
            'agg computes several summaries at once, for example df.groupby("city")["sales"].agg(["count", "mean", "max"]). Always report group sizes alongside averages: a mean of one value (Nairobi) is not comparable to a mean of many.'],
        'formulas_label': 'Code',
        'formulas': ['df[df["col"] > x]', 'df[(cond1) & (cond2)]', 'df.sort_values("col", ascending=False)', 'df.groupby("key")["col"].sum() / .mean() / .agg([...])'],
        'steps': ['Write the question in words ("total sales by city").', 'Filter rows if needed.', 'Group by the category.', 'Aggregate and sort the result.'],
        'worked_example': {
            'problem': 'What does df.groupby("city")["sales"].sum() give for the sales table?',
            'steps': ['Lagos rows: 120 + 150 = 270.', 'Accra rows: 80 + 60 = 140; Nairobi: 95.', 'pandas sorts group keys alphabetically.'],
            'answer': 'Accra 140, Lagos 270, Nairobi 95.',
            'check': 'Totals add to 505, the overall sum ✓.'},
        'mistakes': ['Using "and" instead of & in masks.', 'Leaving out the brackets around each condition.', 'Comparing group means without group sizes.', 'Forgetting that sort_values returns a new DataFrame.'],
        'real_world': 'A supermarket chain\'s weekly report is mostly group-by summaries: sales by store, by product line and by day.',
        'exam_strategy': 'Translate each English phrase: "for each" → groupby, "only" → filter, "top" → sort then head.',
        'recap': ['Masks filter.', '& and | with brackets.', 'Split-apply-combine.', 'Report group sizes.']},
    T4: {
        'overview': 'Real analyses combine tables and reshape them. Joins match rows by keys; melt and pivot switch between wide and long formats.',
        'key_terms': ['Key', 'merge', 'Inner join', 'Left join', 'Outer join', 'Unmatched rows', 'Wide format', 'Long format', 'melt', 'pivot'],
        'explanation': [
            'orders has customers A, B, A, D; cust lists A, B and C. orders.merge(cust, on="cust") is an inner join: only matching rows, so 3 rows (D has no match). how="left" keeps all 4 orders and fills the unknown name with NaN (1 missing). how="outer" keeps everything from both tables: 5 rows, including customer C with no orders.',
            'Always check row counts before and after a join. If a key appears more than once in both tables, rows multiply; if keys are spelt differently ("Lagos" vs "lagos") matches are silently lost.',
            'Wide tables have one column per period: shops X and Y with Jan, Feb and Mar columns (2 × 4). w.melt(id_vars="shop", var_name="month", value_name="sales") gives long format, 6 rows × 3 columns, ready for groupby and plotting; total sales stay 112. pivot reverses it, back to 2 shops × 3 months.'],
        'formulas_label': 'Code',
        'formulas': ['a.merge(b, on="key", how="inner" | "left" | "right" | "outer")', 'df.melt(id_vars=..., var_name=..., value_name=...)', 'df.pivot(index=..., columns=..., values=...)'],
        'steps': ['Identify the key column(s).', 'Choose the join type for the question.', 'Check row counts and unmatched rows.', 'Reshape to long for analysis, wide for display.'],
        'worked_example': {
            'problem': 'Orders for customers A, B, A and D are joined to a customer table listing A, B and C. How many rows do inner, left and outer joins give?',
            'steps': ['Inner: matches only, A, B, A → 3 rows.', 'Left: all 4 orders, D with a missing name.', 'Outer: 4 orders plus customer C with no orders → 5 rows.'],
            'answer': '3, 4 and 5 rows.',
            'check': 'Running the merges gives 3, 4 and 5 ✓.'},
        'mistakes': ['Not checking row counts after a join.', 'Using an inner join and silently losing unmatched records.', 'Joining on keys with inconsistent spelling or type.', 'Analysing wide data that should be long.'],
        'real_world': 'Mobile-money analysts join transaction tables to customer and agent tables to study usage by region.',
        'exam_strategy': 'Draw the two key lists side by side and mark matches; the row counts for each join type then follow.',
        'recap': ['Keys match rows.', 'Inner, left, outer.', 'Check counts.', 'Melt to long, pivot to wide.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'For the five-row, two-column sales DataFrame, print(df.shape) shows:', ['(5, 2)', '(2, 5)', '10', '[5, 2]'], 0, 'Rows, columns.'),
    Q(T1, 'df["sales"].mean() for sales 120, 80, 95, 150, 60 prints:', ['101.0', '95.0', '505', '101'], 0, '505/5 as a float.'),
    Q(T1, 'df["city"].nunique() for Lagos, Accra, Nairobi, Lagos, Accra is:', ['3', '5', '2', '4'], 0, 'Distinct values.', ans=3, num=True),
    Q(T1, 'Which method lists each column\'s dtype and non-missing count?', ['df.info()', 'df.describe()', 'df.head()', 'df.shape'], 0, 'Types and counts.'),
    Q(T1, 'A column of numbers read as text usually has dtype:', ['object (or string)', 'int64', 'float64', 'bool'], 0, 'Needs conversion.'),
    Q(T1, 'df.describe() mainly reports:', ['summary statistics of numerical columns', 'the first five rows', 'missing values only', 'column names only'], 0, 'Count, mean, SD …'),
    # T2
    Q(T2, 's = pd.Series([10, None, 30, None, 50]); s.isna().sum() is:', ['2', '3', '0', '5'], 0, 'Two missing.', ans=2, num=True),
    Q(T2, 's.mean() for that series prints:', ['30.0', '18.0', '90.0', 'nan'], 0, 'Missing values skipped.'),
    Q(T2, 's.fillna(0).mean() prints:', ['18.0', '30.0', '22.5', '0.0'], 0, '90/5.'),
    Q(T2, 'pd.to_numeric(pd.Series(["1", "2", "x"]), errors="coerce").sum() prints:', ['3.0', '3', 'an error', '12x'], 0, '"x" becomes NaN.'),
    Q(T2, 'Rows (1, 5), (2, 6), (2, 6), (3, 7): how many duplicates does duplicated().sum() report?', ['1', '2', '0', '4'], 0, 'Second (2, 6).', ans=1, num=True),
    Q(T2, 'Filling missing incomes with 0 before averaging will usually:', ['bias the mean downwards', 'have no effect', 'bias it upwards', 'remove outliers'], 0, 'Zeros are not real.'),
    # T3
    Q(T3, 'How many rows does df[df["sales"] > 90] return for sales 120, 80, 95, 150, 60?', ['3', '2', '4', '5'], 0, '120, 95, 150.', ans=3, num=True),
    Q(T3, 'Combining conditions in pandas uses:', ['& and | with each condition in brackets', 'and/or keywords', 'commas', '+ and −'], 0, 'Element-wise.'),
    Q(T3, 'df.groupby("city")["sales"].sum() gives Lagos:', ['270', '135', '150', '505'], 0, '120 + 150.', ans=270, num=True),
    Q(T3, 'The mean sales for Accra (80 and 60) is:', ['70.0', '140', '80', '60'], 0, '140/2.'),
    Q(T3, 'After sort_values("sales", ascending=False), the first city is:', ['Lagos', 'Accra', 'Nairobi', 'unchanged'], 0, '150 is largest.'),
    Q(T3, 'groupby follows the pattern:', ['split-apply-combine', 'load-save-close', 'sort-filter-merge', 'map-reduce-index'], 0, 'Three stages.'),
    # T4
    Q(T4, 'Orders for A, B, A, D inner-joined to customers A, B, C give how many rows?', ['3', '4', '5', '2'], 0, 'D drops out.', ans=3, num=True),
    Q(T4, 'A left join of those orders to customers gives:', ['4 rows, one with a missing name', '3 rows', '5 rows', '7 rows'], 0, 'Keeps all orders.'),
    Q(T4, 'An outer join gives how many rows?', ['5', '4', '3', '6'], 0, 'Adds customer C.', ans=5, num=True),
    Q(T4, 'Melting a 2-shop table with Jan, Feb and Mar columns gives a shape of:', ['(6, 3)', '(2, 4)', '(3, 6)', '(8, 2)'], 0, '2 × 3 rows; shop, month, sales.'),
    Q(T4, 'After melting, the total of the sales column (10, 20, 15, 25, 12, 30) is:', ['112', '57', '55', '6'], 0, 'Values are kept.', ans=112, num=True),
    Q(T4, 'Before trusting a join, you should always check:', ['row counts before and after', 'the column order', 'the file name', 'the font'], 0, 'Lost or multiplied rows.'),
]

FLASH = [
    ['Inspect a DataFrame', 'shape, head(), info(), describe().'],
    ['Count missing values', 's.isna().sum(); mean() skips NaN.'],
    ['fillna caution', 'Filling with 0 changes summaries; choose with a reason.'],
    ['Convert types', 'pd.to_numeric(..., errors="coerce"), pd.to_datetime.'],
    ['Filter rows', 'df[(cond1) & (cond2)].'],
    ['Group summaries', 'df.groupby(key)[col].sum()/mean()/agg().'],
    ['Join types', 'Inner = matches; left = all left rows; outer = everything.'],
    ['Reshape', 'melt: wide → long; pivot: long → wide.'],
]
