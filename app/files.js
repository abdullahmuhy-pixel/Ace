/* AceFiles: turns files students pick into something Ace can read.
   - image(file): a photo of a question or of notes -> { media_type, data (base64, no prefix), thumb (small data URL) }.
     The photo is resized on the phone first (longest side 1600px, JPEG), so uploads stay small on mobile data.
   - text(file): PDF, PowerPoint (.pptx), Word (.docx) or plain text -> { text, pages, name }.
     pdf.js and JSZip are served from vendor/ and only loaded when a student picks that kind of file.
   Nothing is uploaded here; callers send the result to the ai-tutor or notes-pack edge functions. */
(function () {
  'use strict';
  const BASE = document.baseURI;
  const loaded = {};
  const load = src => loaded[src] || (loaded[src] = new Promise((ok, no) => { const s = document.createElement('script'); s.src = new URL(src, BASE).href; s.onload = ok; s.onerror = () => { delete loaded[src]; no(new Error('Could not load ' + src)) }; document.head.appendChild(s) }));
  const fail = m => { throw { msg: m } };

  function readURL(file) { return new Promise((ok, no) => { const r = new FileReader(); r.onload = () => ok(r.result); r.onerror = () => no(r.error); r.readAsDataURL(file) }) }
  function decode(url) { return new Promise((ok, no) => { const i = new Image(); i.onload = () => ok(i); i.onerror = no; i.src = url }) }
  function draw(img, max, q) {
    const s = Math.min(1, max / Math.max(img.naturalWidth, img.naturalHeight)), w = Math.max(1, Math.round(img.naturalWidth * s)), h = Math.max(1, Math.round(img.naturalHeight * s));
    const cv = document.createElement('canvas'); cv.width = w; cv.height = h; const g = cv.getContext('2d'); g.fillStyle = '#fff'; g.fillRect(0, 0, w, h); g.drawImage(img, 0, 0, w, h);
    return cv.toDataURL('image/jpeg', q);
  }
  async function image(file) {
    if (!file) fail('No photo chosen.');
    if (!/^image\//.test(file.type || '') && !/\.(jpe?g|png|webp|gif|heic|heif)$/i.test(file.name || '')) fail('Choose a photo (JPG or PNG).');
    if (file.size > 25e6) fail('That photo is too large. Try again with a smaller one.');
    let img; try { img = await decode(await readURL(file)) } catch (e) { fail('Ace could not open that photo. Take it again as a JPG or PNG.') }
    let url = draw(img, 1600, .82); if (url.length > 1.9e6) url = draw(img, 1200, .72); if (url.length > 1.9e6) url = draw(img, 900, .65);
    return { media_type: 'image/jpeg', data: url.split(',')[1], thumb: draw(img, 260, .6), name: file.name || 'photo.jpg' };
  }

  const xmlText = (xml, tag) => { const d = new DOMParser().parseFromString(xml, 'application/xml'); return Array.from(d.getElementsByTagName(tag)).map(n => n.textContent) };
  async function pdf(file) {
    await load('vendor/pdf.js'); const lib = window.pdfjsLib; if (!lib) fail('Ace could not open PDFs on this device.');
    lib.GlobalWorkerOptions.workerSrc = new URL('vendor/pdf.worker.js', BASE).href;
    const doc = await lib.getDocument({ data: new Uint8Array(await file.arrayBuffer()) }).promise.catch(() => fail('Ace could not read that PDF. It may be locked with a password.'));
    const n = Math.min(doc.numPages, 80), out = [];
    for (let i = 1; i <= n; i++) {
      const p = await doc.getPage(i), tc = await p.getTextContent(); let line = '', y = null, t = '';
      tc.items.forEach(it => { const yy = it.transform ? Math.round(it.transform[5]) : y; if (y !== null && yy !== y) { t += line.trim() + '\n'; line = '' } line += it.str + (it.hasEOL ? '\n' : ' '); y = yy });
      out.push((t + line).replace(/[ \t]+\n/g, '\n').trim());
      if (out.join('\n').length > 40000) break;
    }
    return { text: out.join('\n\n'), pages: doc.numPages };
  }
  async function office(file, kind) {
    await load('vendor/jszip.min.js'); let zip;
    try { zip = await window.JSZip.loadAsync(await file.arrayBuffer()) } catch (e) { fail('Ace could not open that file. Save it again as .pptx, .docx or PDF.') }
    if (kind === 'pptx') {
      const slides = Object.keys(zip.files).filter(n => /^ppt\/slides\/slide\d+\.xml$/.test(n)).sort((a, b) => +a.match(/(\d+)\.xml/)[1] - +b.match(/(\d+)\.xml/)[1]);
      const out = [];
      for (const s of slides) {
        const xml = await zip.file(s).async('string'), d = new DOMParser().parseFromString(xml, 'application/xml');
        const paras = Array.from(d.getElementsByTagName('a:p')).map(p => Array.from(p.getElementsByTagName('a:t')).map(t => t.textContent).join('')).filter(x => x.trim());
        const nf = s.replace('slides/slide', 'notesSlides/notesSlide'), notes = zip.file(nf) ? xmlText(await zip.file(nf).async('string'), 'a:t').join(' ').trim() : '';
        out.push(`Slide ${out.length + 1}\n` + paras.join('\n') + (notes && !/^\d+$/.test(notes) ? `\nSpeaker notes: ${notes}` : ''));
      }
      return { text: out.join('\n\n'), pages: slides.length };
    }
    const f = zip.file('word/document.xml'); if (!f) fail('That does not look like a Word document.');
    const d = new DOMParser().parseFromString(await f.async('string'), 'application/xml');
    const paras = Array.from(d.getElementsByTagName('w:p')).map(p => Array.from(p.getElementsByTagName('w:t')).map(t => t.textContent).join('')).filter(x => x.trim());
    return { text: paras.join('\n'), pages: null };
  }
  async function text(file) {
    if (!file) fail('No file chosen.');
    if (file.size > 40e6) fail('That file is too large (over 40 MB).');
    const n = (file.name || '').toLowerCase(); let r;
    if (/\.pdf$/.test(n) || file.type === 'application/pdf') r = await pdf(file);
    else if (/\.pptx$/.test(n)) r = await office(file, 'pptx');
    else if (/\.docx$/.test(n)) r = await office(file, 'docx');
    else if (/\.(txt|md|csv)$/.test(n) || /^text\//.test(file.type || '')) r = { text: await file.text(), pages: null };
    else if (/\.(ppt|doc)$/.test(n)) fail('Ace reads the newer .pptx and .docx files. Open the file and save it in that format, or as a PDF.');
    else fail('Choose a PDF, PowerPoint (.pptx), Word (.docx) or text file.');
    r.text = (r.text || '').replace(/\u0000/g, '').replace(/\n{3,}/g, '\n\n').trim(); r.name = file.name;
    if (r.text.length < 40) fail('Ace could not find text in that file. If it is scanned, take photos of the pages instead.');
    return r;
  }
  window.AceFiles = { image, text, load };
})();
