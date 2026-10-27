/* Ace audio teacher.
   Turns lesson content into a spoken lesson the way a teacher would give it: a welcome, the big picture,
   key words, the explanation with pauses to let points land, a worked example where the listener tries first,
   the mistakes students make, a real-life connection, an exam tip, a recap and a question to finish.
   Speech is the browser's own voice (free, works offline once the page is cached). Lines are spoken one sentence
   at a time with real pauses between them, so long lessons never hit the browser's long-utterance cut-off.
   Used by the student app, Ace Campus (generated from the app) and Ace Academy. Public API: window.AceTeacher. */
(function () {
  'use strict';
  const SY = window.speechSynthesis || null;
  const RM = window.matchMedia ? matchMedia('(prefers-reduced-motion: reduce)') : { matches: false };
  const LS = { get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }, set(k, v) { try { localStorage.setItem(k, v); } catch (e) { } } };

  /* ---------- what the teacher says, per language ---------- */
  const PB = {
    en: {
      hi: ["Hi, I'm Ace. Today's lesson is {t}. Get comfortable, and let's work through it together.", "Welcome. Today's topic: {t}. Grab a pen if you like; I'll go at a steady pace.", "Hello! Let's learn {t} together. I'll explain it the way I would in class, with examples along the way."],
      big: ["First, the big picture.", "Let's start with what this topic is really about."],
      terms: ["Before we go further, here are the key words you'll hear me use.", "A few key terms first. Make sure each one makes sense to you."],
      termsOut: ["Keep those words in mind. They'll come up again.", "Hold on to those words; we'll use them in a moment."],
      expl: ["Now let's look at it in more detail.", "Right, let's dig a little deeper."],
      aside: ["Let me pause there for a moment. Make sure that part is clear before we move on.", "Stay with me; the next part builds on that.", "That's an important point, so let it sink in for a second.", "Here's where it starts to come together.", "If that felt like a lot, that's normal. We'll take it step by step.", "Picture that in your head before we carry on."],
      fm: ["Now, here's something worth writing down.", "These are the facts to keep in your notes. Pause me if you need time to write."],
      steps: ["Here's a method you can follow every time.", "When you meet a question on this, follow these steps."],
      step: "Step {n}.",
      we: ["Let's do an example together. Here's the question.", "Time for a worked example. Listen to the problem first."],
      weTry: ["Before I show you, think about how you'd start. I'll give you a few seconds.", "Try it in your head first. I'll wait a moment."],
      weShow: ["Okay, here's how I'd work through it.", "Right, let's go through it together."],
      seq: ["First.", "Next.", "Then.", "After that.", "And then.", "Finally."],
      weAns: ["So the answer is: {a}.", "And that gives us our answer: {a}."],
      weAns2: ["Here's our answer.", "So, putting it all together."],
      weChk: ["Always check your work. {v}", "A quick check: {v}"],
      cm: ["Now, a warning. These are the mistakes I see students make again and again.", "Let me tell you where students usually lose marks."],
      cmEach: ["Watch out for this: {x}", "Another one: {x}", "And this one: {x}", "Also: {x}"],
      cmOut: ["Avoid those, and you're already ahead of many students.", "Remember those, and you'll save yourself easy marks."],
      rw: ["So why does this matter outside the classroom? Here's a real-life example.", "Let's connect this to real life."],
      rwOut: ["Next time you come across that, you'll know exactly what's going on.", "See? This isn't just for the exam."],
      es: ["A word about the exam.", "Here's an exam tip."],
      rc: ["Let's wrap up. If you remember nothing else, remember these.", "Quick recap before we finish."],
      qIn: ["Now it's your turn. Here's a question.", "Let's see if it stuck. Try this one."],
      opt: "{l}: {o}.",
      qThink: ["Take a moment to choose.", "Think about it. I'll give you a few seconds."],
      qAns: ["The answer is {l}: {o}.", "It's {l}: {o}."],
      qWhy: "Here's why. {e}",
      qGood: ["If you got that, well done.", "Did you get it? Great if you did. If not, that's exactly why we practise."],
      bye: ["That's the end of this lesson. When you're ready, try the practice questions. You're doing well.", "And that's {t}. Nice work. Take a short break, then test yourself with the questions."],
      nextT: ["Next topic: {t}.", "Moving on to {t}."],
      modIn: ["This is {t}. There are {n} lessons here, and I'll take you through them one by one.", "Welcome to {t}. We'll go through {n} lessons, one after another."],
      modBye: ["That's everything in this set. Well done for sticking with it.", "And we're done. That was a lot of learning, so be proud of yourself."],
      cardIn: ["Let's review with flashcards. I'll read the front, give you a moment to recall the answer, then tell you.", "Flashcard time. Try to answer each one before I do."],
      cardThink: ["What's the answer?", "Say it out loud if you can.", "Do you remember?"],
      cardBack: ["The answer: {a}", "It's {a}"],
      qsIn: ["Let's practise some questions out loud. I'll read each one, give you time to think, then go through the answer.", "Here are some practice questions. Answer each one in your head before I do."],
      qsN: "Question {n}.",
      thIn: "This one is a written question.",
      thThink: ["Plan your answer. What points would you make?", "Think about how you'd answer that in the exam."],
      thPts: "A strong answer would make these points.",
      lesIn: ["Welcome to this lesson: {t}. It takes about {m} minutes, and I'll talk you through it.", "This lesson is {t}. Settle in; I'll guide you through it."],
      head: ["Next: {h}.", "Now let's look at {h}."],
      list: ["Here are the main points.", "Let's go through these one by one."],
      tip: ["Here's a practical tip.", "A tip from experience."],
      code: "There's a code example on your screen with {n} lines. Have a look at it now; I'll give you a moment.",
      chk: "Quick check.",
      xIn: "Let me explain that a bit more.",
      xOut: "Right, back to where we were.",
      xFail: "I couldn't get a fuller explanation just now. Let's carry on.",
      lesBye: ["That's the end of this lesson. Well done.", "And that's this lesson done. Nice work."],
      courseIn: ["Welcome to {t}. There are {n} lessons, and I'll read you through them one by one.", "This is the audio version of {t}. {n} lessons, at your pace."],
      sec: { intro: 'Welcome', big: 'Big picture', terms: 'Key terms', expl: 'Explanation', fm: 'Write these down', steps: 'Method', we: 'Worked example', cm: 'Common mistakes', rw: 'Real life', es: 'Exam tip', rc: 'Recap', q: 'Your turn', end: 'Wrap-up', x: 'Explained further' },
      ui: { listen: 'Listen', audio: 'Audio lesson', play: 'Play', pause: 'Pause', back: 'Back a sentence', next: 'Next part', speed: 'Speed', voice: 'Voice', best: 'Best voice on this device', chapters: 'Parts', transcript: 'Transcript', more: 'More', close: 'Stop and close', explain: 'Explain this more', explainBusy: 'Ace is thinking…', look: 'Have a look', think: 'Your turn', resume: 'Picking up where you left off.', restart: 'Start again', novoice: 'Your device has no voice for this language, so the lesson is shown as captions.', test: 'Test voice', testLine: 'Hello! This is how I will sound in your lessons.', module: 'Listen to this module', subject: 'Audio course', cards: 'Listen to these cards', qs: 'Listen and answer', aiNote: 'Uses one Ace message', signin: 'Sign in to ask Ace for more.', listenAll: 'Listen to the whole course', weak: 'Listen to my weak topics', audioTool: 'Audio lessons', audioToolSub: 'Learn by listening: a teacher talks you through every topic', cont: 'Continue listening', pick: 'Choose a subject', topics: 'topics', none: 'Audio lessons for this country are coming soon.' },
      w: { eq: 'equals', to: 'gives', so: 'so', le: 'is less than or equal to', ge: 'is greater than or equal to', ne: 'is not equal to', ap: 'is approximately', lt: 'is less than', gt: 'is greater than', sq: 'squared', cu: 'cubed', pw: 'to the power of', rt: 'the square root of', tm: 'times', dv: 'divided by', pm: 'plus or minus', mi: 'minus', pi: 'pi', dg: 'degrees', per: 'per', eg: 'for example', ie: 'that is', delta: 'change in', and: 'and', base: 'base' }
    },
    es: {
      hi: ["Hola, soy Ace. La lección de hoy es {t}. Ponte cómodo y vamos a verla juntos.", "Bienvenido. El tema de hoy: {t}. Ten un bolígrafo a mano si quieres; iré a buen ritmo.", "¡Hola! Hoy vemos juntos este tema: {t}. Te lo explico como lo haría en clase, con ejemplos."],
      big: ["Primero, la idea general.", "Empecemos por lo esencial del tema."],
      terms: ["Antes de seguir, estas son las palabras clave que vas a oír.", "Primero, unos términos clave. Asegúrate de entender cada uno."],
      termsOut: ["Ten presentes esas palabras. Volverán a salir.", "Guarda esas palabras; las usaremos enseguida."],
      expl: ["Ahora veámoslo con más detalle.", "Bien, profundicemos un poco."],
      aside: ["Hagamos una pausa aquí. Asegúrate de que esto quede claro antes de seguir.", "Sigue conmigo; lo siguiente se apoya en esto.", "Este punto es importante, así que dale un segundo.", "Aquí es donde todo empieza a encajar.", "Si te parece mucho, es normal. Vamos paso a paso.", "Imagínatelo antes de continuar."],
      fm: ["Ahora, algo que vale la pena apuntar.", "Esto es lo que debes tener en tus apuntes. Páusame si necesitas tiempo."],
      steps: ["Este es un método que puedes seguir siempre.", "Cuando te salga una pregunta de esto, sigue estos pasos."],
      step: "Paso {n}.",
      we: ["Hagamos un ejemplo juntos. Esta es la pregunta.", "Vamos con un ejemplo resuelto. Primero escucha el problema."],
      weTry: ["Antes de mostrártelo, piensa cómo empezarías. Te doy unos segundos.", "Inténtalo mentalmente primero. Espero un momento."],
      weShow: ["Bien, así es como lo haría yo.", "Vamos a resolverlo juntos."],
      seq: ["Primero.", "Después.", "Luego.", "A continuación.", "Y entonces.", "Por último."],
      weAns: ["Así que la respuesta es: {a}.", "Y esa es nuestra respuesta: {a}."],
      weAns2: ["Esta es nuestra respuesta.", "Así que, juntándolo todo."],
      weChk: ["Comprueba siempre tu trabajo. {v}", "Una comprobación rápida: {v}"],
      cm: ["Ahora, una advertencia. Estos son los errores que veo una y otra vez.", "Te cuento dónde suelen perder puntos los estudiantes."],
      cmEach: ["Cuidado con esto: {x}", "Otro: {x}", "Y este: {x}", "También: {x}"],
      cmOut: ["Evítalos y ya vas por delante de muchos.", "Recuérdalos y te ahorrarás puntos fáciles."],
      rw: ["¿Y por qué importa esto fuera del aula? Aquí tienes un ejemplo de la vida real.", "Conectemos esto con la vida real."],
      rwOut: ["La próxima vez que lo veas, sabrás exactamente qué pasa.", "¿Ves? No es solo para el examen."],
      es: ["Una palabra sobre el examen.", "Un consejo para el examen."],
      rc: ["Vamos a cerrar. Si no recuerdas nada más, recuerda esto.", "Un repaso rápido antes de terminar."],
      qIn: ["Ahora te toca a ti. Aquí va una pregunta.", "A ver si se te ha quedado. Prueba esta."],
      opt: "{l}: {o}.",
      qThink: ["Tómate un momento para elegir.", "Piénsalo. Te doy unos segundos."],
      qAns: ["La respuesta es la {l}: {o}.", "Es la {l}: {o}."],
      qWhy: "Te explico por qué. {e}",
      qGood: ["Si la acertaste, muy bien.", "¿La acertaste? Genial. Si no, para eso practicamos."],
      bye: ["Aquí termina la lección. Cuando quieras, prueba las preguntas de práctica. Lo estás haciendo bien.", "Y listo. Buen trabajo. Descansa un poco y luego ponte a prueba."],
      nextT: ["Siguiente tema: {t}.", "Ahora un tema nuevo: {t}."],
      modIn: ["Esto es {t}. Hay {n} lecciones y te las explico una a una.", "Bienvenido a {t}. Veremos {n} lecciones, una tras otra."],
      modBye: ["Eso es todo en este bloque. Bien hecho por llegar hasta aquí.", "Terminamos. Ha sido mucho aprendizaje; siéntete orgulloso."],
      cardIn: ["Repasemos con tarjetas. Leo el anverso, te doy un momento para recordar y luego te digo la respuesta.", "Hora de las tarjetas. Intenta responder antes que yo."],
      cardThink: ["¿Cuál es la respuesta?", "Dilo en voz alta si puedes.", "¿Te acuerdas?"],
      cardBack: ["La respuesta: {a}", "Es {a}"],
      qsIn: ["Practiquemos preguntas en voz alta. Leo cada una, te doy tiempo para pensar y luego vemos la respuesta.", "Aquí tienes preguntas de práctica. Respóndelas mentalmente antes que yo."],
      qsN: "Pregunta {n}.",
      thIn: "Esta es una pregunta de desarrollo.",
      thThink: ["Planifica tu respuesta. ¿Qué puntos incluirías?", "Piensa cómo la responderías en el examen."],
      thPts: "Una buena respuesta incluiría estos puntos.",
      lesIn: ["Bienvenido a esta lección: {t}. Dura unos {m} minutos y te la explico.", "Esta lección es {t}. Ponte cómodo; te guío."],
      head: ["Ahora: {h}.", "Veamos {h}."],
      list: ["Estos son los puntos principales.", "Veámoslos uno a uno."],
      tip: ["Un consejo práctico.", "Un consejo de experiencia."],
      code: "En tu pantalla hay un ejemplo de código de {n} líneas. Míralo ahora; te doy un momento.",
      chk: "Comprobación rápida.",
      xIn: "Déjame explicarlo un poco más.",
      xOut: "Bien, volvamos a donde estábamos.",
      xFail: "Ahora no he podido darte una explicación más completa. Sigamos.",
      lesBye: ["Aquí termina la lección. Bien hecho.", "Y con esto terminamos la lección. Buen trabajo."],
      courseIn: ["Bienvenido a {t}. Hay {n} lecciones y te las leo una a una.", "Esta es la versión en audio de {t}. {n} lecciones, a tu ritmo."],
      sec: { intro: 'Bienvenida', big: 'Idea general', terms: 'Términos clave', expl: 'Explicación', fm: 'Para apuntar', steps: 'Método', we: 'Ejemplo resuelto', cm: 'Errores comunes', rw: 'Vida real', es: 'Consejo de examen', rc: 'Repaso', q: 'Tu turno', end: 'Cierre', x: 'Más explicación' },
      ui: { listen: 'Escuchar', audio: 'Lección en audio', play: 'Reproducir', pause: 'Pausa', back: 'Frase anterior', next: 'Siguiente parte', speed: 'Velocidad', voice: 'Voz', best: 'La mejor voz del dispositivo', chapters: 'Partes', transcript: 'Transcripción', more: 'Más', close: 'Parar y cerrar', explain: 'Explícalo más', explainBusy: 'Ace está pensando…', look: 'Échale un vistazo', think: 'Tu turno', resume: 'Seguimos donde lo dejaste.', restart: 'Empezar de nuevo', novoice: 'Tu dispositivo no tiene voz para este idioma; la lección se muestra como subtítulos.', test: 'Probar voz', testLine: '¡Hola! Así sonaré en tus lecciones.', module: 'Escuchar este módulo', subject: 'Curso en audio', cards: 'Escuchar estas tarjetas', qs: 'Escuchar y responder', aiNote: 'Usa un mensaje de Ace', signin: 'Inicia sesión para pedirle más a Ace.', listenAll: 'Escuchar todo el curso', weak: 'Escuchar mis puntos débiles', audioTool: 'Lecciones en audio', audioToolSub: 'Aprende escuchando: un profesor te explica cada tema', cont: 'Seguir escuchando', pick: 'Elige una asignatura', topics: 'temas', none: 'Las lecciones en audio para este país llegarán pronto.' },
      w: { eq: 'es igual a', to: 'da', so: 'por tanto', le: 'es menor o igual que', ge: 'es mayor o igual que', ne: 'es distinto de', ap: 'es aproximadamente', lt: 'es menor que', gt: 'es mayor que', sq: 'al cuadrado', cu: 'al cubo', pw: 'elevado a', rt: 'la raíz cuadrada de', tm: 'por', dv: 'entre', pm: 'más o menos', mi: 'menos', pi: 'pi', dg: 'grados', per: 'por', eg: 'por ejemplo', ie: 'es decir', delta: 'variación de', and: 'y', base: 'en base' }
    },
    fr: {
      hi: ["Bonjour, je suis Ace. La leçon du jour : {t}. Installe-toi, on va la voir ensemble.", "Bienvenue. Le thème du jour : {t}. Prends un stylo si tu veux ; j'avance à un rythme tranquille.", "Bonjour ! Aujourd'hui, on étudie ensemble : {t}. Je t'explique comme en classe, avec des exemples."],
      big: ["D'abord, la vue d'ensemble.", "Commençons par l'essentiel du sujet."],
      terms: ["Avant d'aller plus loin, voici les mots clés que tu vas m'entendre utiliser.", "D'abord quelques termes clés. Vérifie que chacun est clair pour toi."],
      termsOut: ["Garde ces mots en tête. Ils vont revenir.", "Retiens ces mots ; on s'en sert tout de suite."],
      expl: ["Regardons maintenant plus en détail.", "Bien, creusons un peu."],
      aside: ["Faisons une pause ici. Assure-toi que c'est clair avant de continuer.", "Reste avec moi ; la suite s'appuie là-dessus.", "C'est un point important, laisse-le bien s'installer.", "C'est là que tout commence à s'assembler.", "Si ça te paraît beaucoup, c'est normal. On avance pas à pas.", "Représente-toi ça avant qu'on continue."],
      fm: ["Voici quelque chose à noter.", "Voilà ce qu'il faut garder dans tes notes. Mets-moi en pause si tu as besoin de temps."],
      steps: ["Voici une méthode à suivre à chaque fois.", "Quand tu tombes sur une question là-dessus, suis ces étapes."],
      step: "Étape {n}.",
      we: ["Faisons un exemple ensemble. Voici la question.", "Place à un exemple corrigé. Écoute d'abord l'énoncé."],
      weTry: ["Avant que je te montre, réfléchis à la façon de commencer. Je te laisse quelques secondes.", "Essaie d'abord dans ta tête. J'attends un instant."],
      weShow: ["Bon, voici comment je m'y prendrais.", "Allez, on le fait ensemble."],
      seq: ["D'abord.", "Ensuite.", "Puis.", "Après cela.", "Et alors.", "Enfin."],
      weAns: ["La réponse est donc : {a}.", "Et voilà notre réponse : {a}."],
      weAns2: ["Voici notre réponse.", "Donc, en rassemblant tout."],
      weChk: ["Vérifie toujours ton travail. {v}", "Petite vérification : {v}"],
      cm: ["Maintenant, une mise en garde. Voici les erreurs que je vois sans arrêt.", "Je te dis où les élèves perdent souvent des points."],
      cmEach: ["Attention à ceci : {x}", "Une autre : {x}", "Et celle-ci : {x}", "Aussi : {x}"],
      cmOut: ["Évite-les et tu as déjà une longueur d'avance.", "Retiens-les et tu gagneras des points faciles."],
      rw: ["Et pourquoi ça compte en dehors de la classe ? Voici un exemple de la vie réelle.", "Faisons le lien avec la vie réelle."],
      rwOut: ["La prochaine fois que tu verras ça, tu sauras exactement ce qui se passe.", "Tu vois ? Ce n'est pas que pour l'examen."],
      es: ["Un mot sur l'examen.", "Un conseil pour l'examen."],
      rc: ["On termine. Si tu ne retiens qu'une chose, retiens ceci.", "Un petit récapitulatif avant de finir."],
      qIn: ["À toi maintenant. Voici une question.", "Voyons si c'est rentré. Essaie celle-ci."],
      opt: "{l} : {o}.",
      qThink: ["Prends un moment pour choisir.", "Réfléchis. Je te laisse quelques secondes."],
      qAns: ["La réponse est {l} : {o}.", "C'est {l} : {o}."],
      qWhy: "Voici pourquoi. {e}",
      qGood: ["Si tu as trouvé, bravo.", "Tu as trouvé ? Super. Sinon, c'est justement pour ça qu'on s'entraîne."],
      bye: ["C'est la fin de cette leçon. Quand tu es prêt, essaie les questions d'entraînement. Tu t'en sors bien.", "Et voilà. Beau travail. Fais une petite pause, puis teste-toi."],
      nextT: ["Thème suivant : {t}.", "Maintenant, un nouveau thème : {t}."],
      modIn: ["Voici {t}. Il y a {n} leçons, et je te les présente une par une.", "Bienvenue dans {t}. On va voir {n} leçons, l'une après l'autre."],
      modBye: ["C'est tout pour cette partie. Bravo d'être allé jusqu'au bout.", "Et c'est fini. Tu as beaucoup appris, sois fier de toi."],
      cardIn: ["Révisons avec des fiches. Je lis le recto, je te laisse un moment pour te souvenir, puis je te donne la réponse.", "C'est l'heure des fiches. Essaie de répondre avant moi."],
      cardThink: ["Quelle est la réponse ?", "Dis-le à voix haute si tu peux.", "Tu t'en souviens ?"],
      cardBack: ["La réponse : {a}", "C'est {a}"],
      qsIn: ["Entraînons-nous à voix haute. Je lis chaque question, je te laisse réfléchir, puis on voit la réponse.", "Voici des questions d'entraînement. Réponds dans ta tête avant moi."],
      qsN: "Question {n}.",
      thIn: "C'est une question rédactionnelle.",
      thThink: ["Prépare ta réponse. Quels points mettrais-tu ?", "Réfléchis à comment tu répondrais à l'examen."],
      thPts: "Une bonne réponse développerait ces points.",
      lesIn: ["Bienvenue dans cette leçon : {t}. Elle prend environ {m} minutes, et je te guide.", "Cette leçon, c'est {t}. Installe-toi, je t'accompagne."],
      head: ["Maintenant : {h}.", "Voyons {h}."],
      list: ["Voici les points principaux.", "Voyons-les un par un."],
      tip: ["Un conseil pratique.", "Un conseil d'expérience."],
      code: "Il y a un exemple de code de {n} lignes à l'écran. Regarde-le maintenant ; je te laisse un moment.",
      chk: "Petite vérification.",
      xIn: "Laisse-moi expliquer un peu plus.",
      xOut: "Bien, reprenons où on en était.",
      xFail: "Je n'ai pas pu obtenir une explication plus complète pour l'instant. Continuons.",
      lesBye: ["C'est la fin de cette leçon. Bravo.", "Et voilà, leçon terminée. Beau travail."],
      courseIn: ["Bienvenue dans {t}. Il y a {n} leçons, et je te les lis une par une.", "Voici la version audio de {t}. {n} leçons, à ton rythme."],
      sec: { intro: 'Bienvenue', big: "Vue d'ensemble", terms: 'Mots clés', expl: 'Explication', fm: 'À noter', steps: 'Méthode', we: 'Exemple corrigé', cm: 'Erreurs fréquentes', rw: 'Vie réelle', es: "Conseil d'examen", rc: 'Récapitulatif', q: 'À toi', end: 'Conclusion', x: 'Pour aller plus loin' },
      ui: { listen: 'Écouter', audio: 'Leçon audio', play: 'Lecture', pause: 'Pause', back: 'Phrase précédente', next: 'Partie suivante', speed: 'Vitesse', voice: 'Voix', best: "La meilleure voix de l'appareil", chapters: 'Parties', transcript: 'Transcription', more: 'Plus', close: 'Arrêter et fermer', explain: 'Explique davantage', explainBusy: 'Ace réfléchit…', look: 'Jette un œil', think: 'À toi', resume: 'On reprend là où tu t\'étais arrêté.', restart: 'Recommencer', novoice: "Ton appareil n'a pas de voix pour cette langue ; la leçon s'affiche en sous-titres.", test: 'Tester la voix', testLine: 'Bonjour ! Voilà comment je parlerai dans tes leçons.', module: 'Écouter ce module', subject: 'Cours audio', cards: 'Écouter ces fiches', qs: 'Écouter et répondre', aiNote: 'Utilise un message Ace', signin: 'Connecte-toi pour demander plus à Ace.', listenAll: 'Écouter tout le cours', weak: 'Écouter mes points faibles', audioTool: 'Leçons audio', audioToolSub: 'Apprendre en écoutant : un professeur t\'explique chaque thème', cont: "Continuer l'écoute", pick: 'Choisis une matière', topics: 'thèmes', none: 'Les leçons audio pour ce pays arrivent bientôt.' },
      w: { eq: 'égale', to: 'donne', so: 'donc', le: 'est inférieur ou égal à', ge: 'est supérieur ou égal à', ne: 'est différent de', ap: 'vaut environ', lt: 'est inférieur à', gt: 'est supérieur à', sq: 'au carré', cu: 'au cube', pw: 'puissance', rt: 'la racine carrée de', tm: 'fois', dv: 'divisé par', pm: 'plus ou moins', mi: 'moins', pi: 'pi', dg: 'degrés', per: 'par', eg: 'par exemple', ie: "c'est-à-dire", delta: 'variation de', and: 'et', base: 'en base' }
    },
    it: {
      hi: ["Ciao, sono Ace. La lezione di oggi è {t}. Mettiti comodo e vediamola insieme.", "Benvenuto. L'argomento di oggi: {t}. Prendi una penna se vuoi; vado con calma.", "Ciao! Oggi studiamo insieme questo argomento: {t}. Te lo spiego come farei in classe, con qualche esempio."],
      big: ["Prima di tutto, il quadro generale.", "Partiamo da che cosa tratta davvero questo argomento."],
      terms: ["Prima di andare avanti, ecco le parole chiave che mi sentirai usare.", "Prima qualche termine chiave. Assicurati che ognuno ti sia chiaro."],
      termsOut: ["Tieni a mente queste parole. Torneranno.", "Ricorda queste parole; le useremo tra poco."],
      expl: ["Ora vediamolo più nel dettaglio.", "Bene, andiamo un po' più a fondo."],
      aside: ["Fermiamoci un attimo. Assicurati che questa parte sia chiara prima di proseguire.", "Seguimi; la parte successiva si basa su questa.", "È un punto importante, lascialo sedimentare un secondo.", "Ecco dove tutto comincia a tornare.", "Se ti sembra tanto, è normale. Andiamo passo dopo passo.", "Immaginalo prima di continuare."],
      fm: ["Ecco una cosa da scrivere.", "Questo è ciò che devi avere negli appunti. Mettimi in pausa se ti serve tempo."],
      steps: ["Ecco un metodo da seguire ogni volta.", "Quando trovi una domanda su questo, segui questi passaggi."],
      step: "Passo {n}.",
      we: ["Facciamo un esempio insieme. Ecco la domanda.", "È il momento di un esempio svolto. Ascolta prima il problema."],
      weTry: ["Prima che te lo mostri, pensa a come inizieresti. Ti do qualche secondo.", "Provaci prima nella tua testa. Aspetto un momento."],
      weShow: ["Bene, ecco come lo farei io.", "Allora, risolviamolo insieme."],
      seq: ["Per prima cosa.", "Poi.", "Quindi.", "Dopodiché.", "E allora.", "Infine."],
      weAns: ["Quindi la risposta è: {a}.", "Ed ecco la nostra risposta: {a}."],
      weAns2: ["Ecco la nostra risposta.", "Quindi, mettendo tutto insieme."],
      weChk: ["Controlla sempre il tuo lavoro. {v}", "Una verifica veloce: {v}"],
      cm: ["Ora, un avvertimento. Questi sono gli errori che vedo fare di continuo.", "Ti dico dove gli studenti perdono spesso punti."],
      cmEach: ["Attenzione a questo: {x}", "Un altro: {x}", "E questo: {x}", "Inoltre: {x}"],
      cmOut: ["Evitali e sei già avanti rispetto a molti.", "Ricordali e risparmierai punti facili."],
      rw: ["E perché conta fuori dall'aula? Ecco un esempio dalla vita reale.", "Colleghiamolo alla vita reale."],
      rwOut: ["La prossima volta che lo incontri, saprai esattamente cosa succede.", "Vedi? Non serve solo per l'esame."],
      es: ["Una parola sull'esame.", "Un consiglio per l'esame."],
      rc: ["Chiudiamo. Se non ricordi altro, ricorda questo.", "Un ripasso veloce prima di finire."],
      qIn: ["Ora tocca a te. Ecco una domanda.", "Vediamo se ti è rimasto. Prova questa."],
      opt: "{l}: {o}.",
      qThink: ["Prenditi un momento per scegliere.", "Pensaci. Ti do qualche secondo."],
      qAns: ["La risposta è la {l}: {o}.", "È la {l}: {o}."],
      qWhy: "Ecco perché. {e}",
      qGood: ["Se l'hai indovinata, bravo.", "L'hai indovinata? Ottimo. Se no, è proprio per questo che ci esercitiamo."],
      bye: ["Questa lezione finisce qui. Quando vuoi, prova le domande di esercitazione. Stai andando bene.", "Ed ecco fatto. Ottimo lavoro. Fai una breve pausa, poi mettiti alla prova."],
      nextT: ["Prossimo argomento: {t}.", "Ora un nuovo argomento: {t}."],
      modIn: ["Questo è {t}. Ci sono {n} lezioni e te le spiego una alla volta.", "Benvenuto in {t}. Vedremo {n} lezioni, una dopo l'altra."],
      modBye: ["È tutto per questa parte. Bravo per essere arrivato fino in fondo.", "Abbiamo finito. Hai imparato tanto, sii fiero di te."],
      cardIn: ["Ripassiamo con le flashcard. Leggo il fronte, ti lascio un momento per ricordare, poi ti dico la risposta.", "È l'ora delle flashcard. Prova a rispondere prima di me."],
      cardThink: ["Qual è la risposta?", "Dilla ad alta voce, se puoi.", "Te lo ricordi?"],
      cardBack: ["La risposta: {a}", "È {a}"],
      qsIn: ["Esercitiamoci ad alta voce. Leggo ogni domanda, ti lascio il tempo di pensare e poi vediamo la risposta.", "Ecco alcune domande di esercitazione. Rispondi mentalmente prima di me."],
      qsN: "Domanda {n}.",
      thIn: "Questa è una domanda aperta.",
      thThink: ["Pianifica la risposta. Quali punti tratteresti?", "Pensa a come risponderesti all'esame."],
      thPts: "Una buona risposta toccherebbe questi punti.",
      lesIn: ["Benvenuto in questa lezione: {t}. Dura circa {m} minuti e ti guido io.", "Questa lezione è {t}. Mettiti comodo, ti accompagno."],
      head: ["Ora: {h}.", "Vediamo {h}."],
      list: ["Ecco i punti principali.", "Vediamoli uno per uno."],
      tip: ["Un consiglio pratico.", "Un consiglio dall'esperienza."],
      code: "Sullo schermo c'è un esempio di codice di {n} righe. Guardalo ora; ti lascio un momento.",
      chk: "Verifica veloce.",
      xIn: "Lascia che te lo spieghi un po' meglio.",
      xOut: "Bene, torniamo dove eravamo.",
      xFail: "Ora non sono riuscito a darti una spiegazione più completa. Andiamo avanti.",
      lesBye: ["La lezione finisce qui. Bravo.", "Ed ecco, lezione finita. Ottimo lavoro."],
      courseIn: ["Benvenuto in {t}. Ci sono {n} lezioni e te le leggo una alla volta.", "Questa è la versione audio di {t}. {n} lezioni, con i tuoi tempi."],
      sec: { intro: 'Benvenuto', big: 'Quadro generale', terms: 'Parole chiave', expl: 'Spiegazione', fm: 'Da annotare', steps: 'Metodo', we: 'Esempio svolto', cm: 'Errori comuni', rw: 'Vita reale', es: "Consiglio d'esame", rc: 'Ripasso', q: 'Tocca a te', end: 'Chiusura', x: 'Spiegato meglio' },
      ui: { listen: 'Ascolta', audio: 'Lezione audio', play: 'Riproduci', pause: 'Pausa', back: 'Frase precedente', next: 'Parte successiva', speed: 'Velocità', voice: 'Voce', best: 'La voce migliore del dispositivo', chapters: 'Parti', transcript: 'Trascrizione', more: 'Altro', close: 'Ferma e chiudi', explain: 'Spiegamelo meglio', explainBusy: 'Ace sta pensando…', look: "Dai un'occhiata", think: 'Tocca a te', resume: 'Riprendiamo da dove eri rimasto.', restart: 'Ricomincia', novoice: 'Il tuo dispositivo non ha una voce per questa lingua, quindi la lezione appare come sottotitoli.', test: 'Prova la voce', testLine: 'Ciao! Ecco come suonerò nelle tue lezioni.', module: 'Ascolta questo modulo', subject: 'Corso audio', cards: 'Ascolta queste carte', qs: 'Ascolta e rispondi', aiNote: 'Usa un messaggio di Ace', signin: 'Accedi per chiedere di più ad Ace.', listenAll: 'Ascolta tutto il corso', weak: 'Ascolta i miei punti deboli', audioTool: 'Lezioni audio', audioToolSub: 'Impara ascoltando: un insegnante ti spiega ogni argomento', cont: 'Continua ad ascoltare', pick: 'Scegli una materia', topics: 'argomenti', none: 'Le lezioni audio per questo paese arriveranno presto.' },
      w: { eq: 'uguale a', to: 'dà', so: 'quindi', le: 'è minore o uguale a', ge: 'è maggiore o uguale a', ne: 'è diverso da', ap: 'è circa', lt: 'è minore di', gt: 'è maggiore di', sq: 'al quadrato', cu: 'al cubo', pw: 'elevato a', rt: 'la radice quadrata di', tm: 'per', dv: 'diviso', pm: 'più o meno', mi: 'meno', pi: 'pi greco', dg: 'gradi', per: 'al', eg: 'per esempio', ie: 'cioè', delta: 'variazione di', and: 'e', base: 'in base' }
    },
    pt: {
      hi: ["Olá, eu sou o Ace. A lição de hoje é {t}. Fica à vontade e vamos ver juntos.", "Bem-vindo. O tema de hoje: {t}. Pega numa caneta, se quiseres; vou com calma.", "Olá! Hoje estudamos juntos este tema: {t}. Explico como faria na aula, com exemplos."],
      big: ["Primeiro, a ideia geral.", "Comecemos pelo essencial do tema."],
      terms: ["Antes de avançar, estas são as palavras-chave que me vais ouvir usar.", "Primeiro, alguns termos-chave. Garante que percebes cada um."],
      termsOut: ["Guarda estas palavras. Vão voltar a aparecer.", "Fixa estas palavras; vamos usá-las já a seguir."],
      expl: ["Agora vamos ver com mais detalhe.", "Muito bem, vamos aprofundar um pouco."],
      aside: ["Vamos fazer uma pausa aqui. Garante que isto ficou claro antes de continuar.", "Fica comigo; a parte seguinte assenta nesta.", "Este é um ponto importante, deixa-o assentar.", "É aqui que tudo começa a encaixar.", "Se parece muito, é normal. Vamos passo a passo.", "Imagina isso antes de continuarmos."],
      fm: ["Agora, algo que vale a pena anotar.", "Isto é o que deves ter nos teus apontamentos. Põe-me em pausa se precisares de tempo."],
      steps: ["Aqui está um método para seguires sempre.", "Quando te sair uma pergunta sobre isto, segue estes passos."],
      step: "Passo {n}.",
      we: ["Vamos fazer um exemplo juntos. Aqui está a pergunta.", "Hora de um exemplo resolvido. Ouve primeiro o problema."],
      weTry: ["Antes de te mostrar, pensa em como começarias. Dou-te uns segundos.", "Tenta primeiro de cabeça. Espero um momento."],
      weShow: ["Muito bem, eis como eu faria.", "Vamos resolver juntos."],
      seq: ["Primeiro.", "Depois.", "Em seguida.", "A seguir.", "E então.", "Por fim."],
      weAns: ["Portanto, a resposta é: {a}.", "E aqui está a nossa resposta: {a}."],
      weAns2: ["Aqui está a nossa resposta.", "Então, juntando tudo."],
      weChk: ["Verifica sempre o teu trabalho. {v}", "Uma verificação rápida: {v}"],
      cm: ["Agora, um aviso. Estes são os erros que vejo vezes sem conta.", "Digo-te onde os alunos costumam perder pontos."],
      cmEach: ["Cuidado com isto: {x}", "Outro: {x}", "E este: {x}", "Também: {x}"],
      cmOut: ["Evita-os e já estás à frente de muitos.", "Lembra-te deles e ganhas pontos fáceis."],
      rw: ["E porque é que isto importa fora da sala de aula? Aqui está um exemplo da vida real.", "Vamos ligar isto à vida real."],
      rwOut: ["Da próxima vez que vires isso, vais saber exatamente o que se passa.", "Vês? Não é só para o exame."],
      es: ["Uma palavra sobre o exame.", "Uma dica para o exame."],
      rc: ["Vamos terminar. Se não te lembrares de mais nada, lembra-te disto.", "Uma revisão rápida antes de acabar."],
      qIn: ["Agora é a tua vez. Aqui vai uma pergunta.", "Vamos ver se ficou. Experimenta esta."],
      opt: "{l}: {o}.",
      qThink: ["Tira um momento para escolher.", "Pensa. Dou-te uns segundos."],
      qAns: ["A resposta é a {l}: {o}.", "É a {l}: {o}."],
      qWhy: "Eis porquê. {e}",
      qGood: ["Se acertaste, muito bem.", "Acertaste? Ótimo. Se não, é para isso que praticamos."],
      bye: ["Esta lição termina aqui. Quando quiseres, experimenta as perguntas de prática. Estás a ir bem.", "E pronto. Bom trabalho. Faz uma pequena pausa e depois testa-te."],
      nextT: ["Próximo tema: {t}.", "Agora, um novo tema: {t}."],
      modIn: ["Isto é {t}. Há {n} lições e explico-tas uma a uma.", "Bem-vindo a {t}. Vamos ver {n} lições, uma após a outra."],
      modBye: ["É tudo neste bloco. Muito bem por chegares ao fim.", "Terminámos. Aprendeste muito; fica orgulhoso."],
      cardIn: ["Vamos rever com cartões. Leio a frente, dou-te um momento para te lembrares e depois digo a resposta.", "Hora dos cartões. Tenta responder antes de mim."],
      cardThink: ["Qual é a resposta?", "Diz em voz alta, se puderes.", "Lembras-te?"],
      cardBack: ["A resposta: {a}", "É {a}"],
      qsIn: ["Vamos praticar perguntas em voz alta. Leio cada uma, dou-te tempo para pensar e depois vemos a resposta.", "Aqui tens perguntas de prática. Responde de cabeça antes de mim."],
      qsN: "Pergunta {n}.",
      thIn: "Esta é uma pergunta de resposta aberta.",
      thThink: ["Planeia a tua resposta. Que pontos incluirias?", "Pensa em como responderias no exame."],
      thPts: "Uma boa resposta incluiria estes pontos.",
      lesIn: ["Bem-vindo a esta lição: {t}. Demora cerca de {m} minutos e eu guio-te.", "Esta lição é {t}. Fica à vontade; eu acompanho-te."],
      head: ["Agora: {h}.", "Vejamos {h}."],
      list: ["Estes são os pontos principais.", "Vamos vê-los um a um."],
      tip: ["Uma dica prática.", "Uma dica de experiência."],
      code: "No ecrã há um exemplo de código com {n} linhas. Olha para ele agora; dou-te um momento.",
      chk: "Verificação rápida.",
      xIn: "Deixa-me explicar isto um pouco melhor.",
      xOut: "Muito bem, voltemos onde estávamos.",
      xFail: "Agora não consegui uma explicação mais completa. Vamos continuar.",
      lesBye: ["Esta lição termina aqui. Muito bem.", "E pronto, lição terminada. Bom trabalho."],
      courseIn: ["Bem-vindo a {t}. Há {n} lições e leio-tas uma a uma.", "Esta é a versão áudio de {t}. {n} lições, ao teu ritmo."],
      sec: { intro: 'Boas-vindas', big: 'Ideia geral', terms: 'Palavras-chave', expl: 'Explicação', fm: 'Para anotar', steps: 'Método', we: 'Exemplo resolvido', cm: 'Erros comuns', rw: 'Vida real', es: 'Dica de exame', rc: 'Revisão', q: 'A tua vez', end: 'Fecho', x: 'Mais explicação' },
      ui: { listen: 'Ouvir', audio: 'Lição em áudio', play: 'Reproduzir', pause: 'Pausa', back: 'Frase anterior', next: 'Parte seguinte', speed: 'Velocidade', voice: 'Voz', best: 'A melhor voz do dispositivo', chapters: 'Partes', transcript: 'Transcrição', more: 'Mais', close: 'Parar e fechar', explain: 'Explica melhor', explainBusy: 'O Ace está a pensar…', look: 'Dá uma olhadela', think: 'A tua vez', resume: 'Continuamos onde paraste.', restart: 'Recomeçar', novoice: 'O teu dispositivo não tem voz para esta língua, por isso a lição aparece em legendas.', test: 'Testar voz', testLine: 'Olá! É assim que vou soar nas tuas lições.', module: 'Ouvir este módulo', subject: 'Curso em áudio', cards: 'Ouvir estes cartões', qs: 'Ouvir e responder', aiNote: 'Usa uma mensagem do Ace', signin: 'Inicia sessão para pedir mais ao Ace.', listenAll: 'Ouvir o curso todo', weak: 'Ouvir os meus pontos fracos', audioTool: 'Lições em áudio', audioToolSub: 'Aprende a ouvir: um professor explica-te cada tema', cont: 'Continuar a ouvir', pick: 'Escolhe uma disciplina', topics: 'temas', none: 'As lições em áudio para este país chegam em breve.' },
      w: { eq: 'é igual a', to: 'dá', so: 'logo', le: 'é menor ou igual a', ge: 'é maior ou igual a', ne: 'é diferente de', ap: 'é aproximadamente', lt: 'é menor que', gt: 'é maior que', sq: 'ao quadrado', cu: 'ao cubo', pw: 'elevado a', rt: 'a raiz quadrada de', tm: 'vezes', dv: 'a dividir por', pm: 'mais ou menos', mi: 'menos', pi: 'pi', dg: 'graus', per: 'por', eg: 'por exemplo', ie: 'ou seja', delta: 'variação de', and: 'e', base: 'na base' }
    },
    de: {
      hi: ["Hallo, ich bin Ace. Die heutige Lektion: {t}. Mach es dir bequem, wir gehen das gemeinsam durch.", "Willkommen. Unser Thema heute: {t}. Nimm dir gern einen Stift; ich gehe in ruhigem Tempo vor.", "Hallo! Heute lernen wir zusammen: {t}. Ich erkläre es dir wie im Unterricht, mit Beispielen."],
      big: ["Zuerst das große Ganze.", "Fangen wir damit an, worum es eigentlich geht."],
      terms: ["Bevor wir weitermachen, hier die Schlüsselbegriffe, die du von mir hören wirst.", "Zuerst ein paar Schlüsselbegriffe. Achte darauf, dass dir jeder klar ist."],
      termsOut: ["Behalte diese Wörter im Kopf. Sie kommen wieder.", "Merk dir diese Wörter; wir brauchen sie gleich."],
      expl: ["Schauen wir uns das jetzt genauer an.", "Gut, gehen wir etwas tiefer."],
      aside: ["Lass uns hier kurz innehalten. Stell sicher, dass das klar ist, bevor wir weitermachen.", "Bleib dran; der nächste Teil baut darauf auf.", "Das ist ein wichtiger Punkt, lass ihn kurz wirken.", "Hier fügt sich alles zusammen.", "Wenn dir das viel vorkommt, ist das normal. Wir gehen Schritt für Schritt.", "Stell dir das kurz bildlich vor."],
      fm: ["Jetzt etwas, das du aufschreiben solltest.", "Das gehört in deine Notizen. Halte mich an, wenn du Zeit brauchst."],
      steps: ["Hier ist eine Methode, der du jedes Mal folgen kannst.", "Wenn dazu eine Frage kommt, geh so vor."],
      step: "Schritt {n}.",
      we: ["Machen wir zusammen ein Beispiel. Hier ist die Aufgabe.", "Zeit für ein Beispiel. Hör dir zuerst die Aufgabe an."],
      weTry: ["Bevor ich es zeige, überleg, wie du anfangen würdest. Ich gebe dir ein paar Sekunden.", "Versuch es erst im Kopf. Ich warte kurz."],
      weShow: ["Gut, so würde ich vorgehen.", "Also, lösen wir es gemeinsam."],
      seq: ["Zuerst.", "Dann.", "Danach.", "Als Nächstes.", "Und dann.", "Zum Schluss."],
      weAns: ["Die Antwort ist also: {a}.", "Und das ist unsere Antwort: {a}."],
      weAns2: ["Hier ist unsere Antwort.", "Also, alles zusammen."],
      weChk: ["Überprüfe immer deine Arbeit. {v}", "Eine kurze Kontrolle: {v}"],
      cm: ["Jetzt eine Warnung. Diese Fehler sehe ich immer wieder.", "Ich sage dir, wo Schüler oft Punkte verlieren."],
      cmEach: ["Pass auf: {x}", "Noch einer: {x}", "Und dieser: {x}", "Außerdem: {x}"],
      cmOut: ["Vermeide sie, und du bist vielen schon voraus.", "Denk daran, dann holst du leichte Punkte."],
      rw: ["Und warum ist das außerhalb der Schule wichtig? Hier ein Beispiel aus dem Alltag.", "Verbinden wir das mit dem echten Leben."],
      rwOut: ["Wenn dir das das nächste Mal begegnet, weißt du genau, was los ist.", "Siehst du? Das ist nicht nur für die Prüfung."],
      es: ["Ein Wort zur Prüfung.", "Ein Prüfungstipp."],
      rc: ["Zum Schluss: Wenn du dir nur eins merkst, dann das.", "Eine kurze Wiederholung zum Abschluss."],
      qIn: ["Jetzt bist du dran. Hier ist eine Frage.", "Mal sehen, ob es hängen geblieben ist. Versuch diese."],
      opt: "{l}: {o}.",
      qThink: ["Nimm dir einen Moment zum Wählen.", "Denk nach. Ich gebe dir ein paar Sekunden."],
      qAns: ["Die Antwort ist {l}: {o}.", "Es ist {l}: {o}."],
      qWhy: "Und zwar deshalb. {e}",
      qGood: ["Wenn du das hattest, gut gemacht.", "Richtig gehabt? Super. Wenn nicht, genau dafür üben wir."],
      bye: ["Das war diese Lektion. Wenn du bereit bist, probier die Übungsfragen. Du machst das gut.", "Und fertig. Gute Arbeit. Mach eine kurze Pause und teste dich dann."],
      nextT: ["Nächstes Thema: {t}.", "Jetzt ein neues Thema: {t}."],
      modIn: ["Das ist {t}. Es gibt {n} Lektionen, und ich führe dich durch jede einzelne.", "Willkommen bei {t}. Wir gehen {n} Lektionen nacheinander durch."],
      modBye: ["Das war alles in diesem Teil. Gut, dass du drangeblieben bist.", "Geschafft. Du hast viel gelernt, sei stolz auf dich."],
      cardIn: ["Wiederholen wir mit Karteikarten. Ich lese die Vorderseite, gebe dir einen Moment und sage dir dann die Antwort.", "Karteikarten-Zeit. Versuch, vor mir zu antworten."],
      cardThink: ["Wie lautet die Antwort?", "Sag es laut, wenn du kannst.", "Weißt du es noch?"],
      cardBack: ["Die Antwort: {a}", "Es ist {a}"],
      qsIn: ["Üben wir Fragen laut. Ich lese jede vor, gebe dir Zeit zum Nachdenken, dann gehen wir die Antwort durch.", "Hier sind Übungsfragen. Antworte im Kopf, bevor ich es tue."],
      qsN: "Frage {n}.",
      thIn: "Das ist eine offene Frage.",
      thThink: ["Plane deine Antwort. Welche Punkte würdest du nennen?", "Überleg, wie du das in der Prüfung beantworten würdest."],
      thPts: "Eine gute Antwort würde diese Punkte nennen.",
      lesIn: ["Willkommen zu dieser Lektion: {t}. Sie dauert etwa {m} Minuten, und ich führe dich durch.", "Diese Lektion ist {t}. Mach es dir bequem; ich begleite dich."],
      head: ["Jetzt: {h}.", "Schauen wir uns {h} an."],
      list: ["Hier sind die wichtigsten Punkte.", "Gehen wir sie einzeln durch."],
      tip: ["Ein praktischer Tipp.", "Ein Tipp aus Erfahrung."],
      code: "Auf deinem Bildschirm ist ein Codebeispiel mit {n} Zeilen. Schau es dir jetzt an; ich gebe dir einen Moment.",
      chk: "Kurze Kontrolle.",
      xIn: "Lass mich das etwas genauer erklären.",
      xOut: "Gut, zurück zu der Stelle, wo wir waren.",
      xFail: "Ich konnte gerade keine ausführlichere Erklärung holen. Machen wir weiter.",
      lesBye: ["Das war diese Lektion. Gut gemacht.", "Und damit ist die Lektion fertig. Gute Arbeit."],
      courseIn: ["Willkommen bei {t}. Es gibt {n} Lektionen, und ich lese sie dir nacheinander vor.", "Das ist die Audioversion von {t}. {n} Lektionen, in deinem Tempo."],
      sec: { intro: 'Willkommen', big: 'Das große Ganze', terms: 'Schlüsselbegriffe', expl: 'Erklärung', fm: 'Zum Aufschreiben', steps: 'Methode', we: 'Beispiel', cm: 'Häufige Fehler', rw: 'Alltag', es: 'Prüfungstipp', rc: 'Wiederholung', q: 'Du bist dran', end: 'Abschluss', x: 'Genauer erklärt' },
      ui: { listen: 'Anhören', audio: 'Audiolektion', play: 'Abspielen', pause: 'Pause', back: 'Satz zurück', next: 'Nächster Teil', speed: 'Tempo', voice: 'Stimme', best: 'Beste Stimme auf diesem Gerät', chapters: 'Teile', transcript: 'Mitschrift', more: 'Mehr', close: 'Stoppen und schließen', explain: 'Genauer erklären', explainBusy: 'Ace denkt nach…', look: 'Schau es dir an', think: 'Du bist dran', resume: 'Wir machen da weiter, wo du aufgehört hast.', restart: 'Von vorn', novoice: 'Dein Gerät hat keine Stimme für diese Sprache, daher erscheint die Lektion als Untertitel.', test: 'Stimme testen', testLine: 'Hallo! So klinge ich in deinen Lektionen.', module: 'Dieses Modul anhören', subject: 'Audiokurs', cards: 'Diese Karten anhören', qs: 'Anhören und antworten', aiNote: 'Verbraucht eine Ace-Nachricht', signin: 'Melde dich an, um Ace mehr zu fragen.', listenAll: 'Ganzen Kurs anhören', weak: 'Meine schwachen Themen anhören', audioTool: 'Audiolektionen', audioToolSub: 'Lernen durch Zuhören: eine Lehrkraft erklärt dir jedes Thema', cont: 'Weiter anhören', pick: 'Wähle ein Fach', topics: 'Themen', none: 'Audiolektionen für dieses Land kommen bald.' },
      w: { eq: 'gleich', to: 'ergibt', so: 'also', le: 'ist kleiner oder gleich', ge: 'ist größer oder gleich', ne: 'ist ungleich', ap: 'ist ungefähr', lt: 'ist kleiner als', gt: 'ist größer als', sq: 'zum Quadrat', cu: 'hoch drei', pw: 'hoch', rt: 'die Wurzel aus', tm: 'mal', dv: 'geteilt durch', pm: 'plus minus', mi: 'minus', pi: 'Pi', dg: 'Grad', per: 'pro', eg: 'zum Beispiel', ie: 'das heißt', delta: 'Änderung von', and: 'und', base: 'zur Basis' }
    }
  };
  const bank = l => PB[(l || 'en').slice(0, 2)] || PB.en;

  /* ---------- seeded variety: the same lesson always sounds the same, different lessons sound different ---------- */
  function hash(s) { let h = 2166136261; for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); } return h >>> 0; }
  function rng(seed) { let a = hash(String(seed)) || 1; return () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
  const fill = (s, v) => String(s).replace(/\{(\w)\}/g, (m, k) => v && v[k] != null ? v[k] : '');

  /* ---------- language detection (a few common words), so German content in an Italian school is read in German ---------- */
  const SW = {
    en: 'the and of to is in that with for are this it as be by on from'.split(' '),
    es: 'el la los las de que y en es por una con para del se no'.split(' '),
    fr: 'le la les des et est une du que dans pour en un sur pas au'.split(' '),
    it: 'il la che di è per una del della non gli le si con nel sono'.split(' '),
    de: 'der die das und ist nicht mit ein eine zu von den im sich auf'.split(' '),
    pt: 'o a os as de que é um uma não do da em com para no'.split(' ')
  };
  function detect(text, fb) {
    const w = String(text || '').toLowerCase().match(/[a-zà-ÿßäöüèéìòù']+/g) || []; if (w.length < 12) return fb || 'en';
    const sc = {}; Object.keys(SW).forEach(l => { const set = new Set(SW[l]); sc[l] = w.reduce((n, x) => n + (set.has(x) ? 1 : 0), 0); });
    let best = fb || 'en'; Object.keys(sc).forEach(l => { if (sc[l] > (sc[best] || 0)) best = l; });
    if (fb && sc[fb] != null && sc[fb] >= sc[best] * 0.8) return fb; return best;
  }

  /* ---------- make written text sayable ---------- */
  let EMO = null, NONW = /[^A-Za-z0-9\u00C0-\u024F]+/g;
  try { EMO = new RegExp('[\\p{Extended_Pictographic}\\uFE0F\\u200D]', 'gu'); NONW = new RegExp('[^\\p{L}\\p{N}]+', 'gu'); } catch (e) { }
  function strip(x) {
    let s = String(x == null ? '' : x);
    s = s.replace(/<sup>(.*?)<\/sup>/gi, '^$1').replace(/<sub>(.*?)<\/sub>/gi, ' $1').replace(/<br\s*\/?>/gi, '. ').replace(/<[^>]+>/g, ' ');
    s = s.replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'");
    if (EMO) s = s.replace(EMO, ' ');
    return s.replace(/[✓✔✗✘•▪◦★☆]/g, ' ').replace(/([\w)])\s+\*\s+(?=[\w(])/g, '$1 × ').replace(/\*\*|__/g, '').replace(/(^|\s)[*_#](?=\S)|(\S)[*_](?=\s|$)/g, '$1$2').replace(/\s+/g, ' ').trim();
  }
  function spoken(x, lang) {
    const W = bank(lang).w; let s = strip(String(x == null ? '' : x).replace(/\s*(↔|⇄|⟷|⇔)\s*/g, ' ~and~ ')).replace(/\s*~and~\s*/g, ' ' + W.and + ' ');
    s = s.replace(/\be\.g\.,?/gi, W.eg + ',').replace(/\bi\.e\.,?/gi, W.ie + ',').replace(/\bp\.\s?ej\.,?/gi, W.eg + ',').replace(/\bz\.\s?B\.,?/g, W.eg + ',').replace(/\bad es\.,?/g, W.eg + ',');
    s = s.replace(/\b(Mr|Mrs|Ms|Dr|St|Prof|Sr|Sra|Mme|Mlle|vs|cf|Fig|No|approx)\./g, '$1');
    s = s.replace(/\b([A-Z])\.\s(?=[A-Z])/g, '$1 ');
    const SUB = '₀₁₂₃₄₅₆₇₈₉', sub = t => t.replace(/[₀-₉]/g, d => SUB.indexOf(d));
    s = s.replace(/\b([0-9A-F]+)([₀-₉]+)/g, (m, n, b) => n + ' ' + W.base + ' ' + sub(b)).replace(/([A-Za-z])([₀-₉ₖₙᵢ]+)/g, (m, l, b) => l + ' ' + sub(b).replace('ₖ', 'k').replace('ₙ', 'n').replace('ᵢ', 'i') + ' ');
    s = s.replace(/([\w)])([ᵏⁿˣ])/g, (m, a, b) => a + ' ' + W.pw + ' ' + ({ 'ᵏ': 'k', 'ⁿ': 'n', 'ˣ': 'x' })[b]);
    s = s.replace(/√\s*\(([^)]+)\)/g, ' ' + W.rt + ' $1 ').replace(/√\s*(\w+)/g, ' ' + W.rt + ' $1 ');
    s = s.replace(/(\w|\))\s*(\^2|²)(?!\d)/g, '$1 ' + W.sq).replace(/(\w|\))\s*(\^3|³)(?!\d)/g, '$1 ' + W.cu);
    s = s.replace(/\^\(([^)]+)\)/g, ' ' + W.pw + ' $1').replace(/\^(-?\w+)/g, ' ' + W.pw + ' $1');
    s = s.replace(/⁻¹/g, ' ' + W.pw + ' ' + W.mi + ' 1').replace(/[⁰¹⁴⁵⁶⁷⁸⁹]/g, d => ' ' + W.pw + ' ' + '⁰¹²³⁴⁵⁶⁷⁸⁹'.indexOf(d));
    s = s.replace(/\s*>=\s*/g, ' ' + W.ge + ' ').replace(/\s*<=(?!>)\s*/g, ' ' + W.le + ' ').replace(/\s*!=\s*/g, ' ' + W.ne + ' ');
    s = s.replace(/\s*(→|⟶|=>|->)\s*/g, ' ' + W.to + ' ').replace(/\s*(⇒|∴)\s*/g, ', ' + W.so + ', ');
    s = s.replace(/\s*≤\s*/g, ' ' + W.le + ' ').replace(/\s*≥\s*/g, ' ' + W.ge + ' ').replace(/\s*≠\s*/g, ' ' + W.ne + ' ').replace(/\s*≈\s*/g, ' ' + W.ap + ' ');
    s = s.replace(/([\w)'|])\s*<\s*(?=[\w(−|-])/g, '$1 ' + W.lt + ' ').replace(/([\w)'|])\s*>\s*(?=[\w(−|-])/g, '$1 ' + W.gt + ' ');
    s = s.replace(/(^|[\s(:;,])>\s*(?=\d)/g, '$1' + W.gt + ' ').replace(/(^|[\s(:;,])<\s*(?=\d)/g, '$1' + W.lt + ' ');
    s = s.replace(/\s*±\s*/g, ' ' + W.pm + ' ').replace(/\s*[×✕]\s*/g, ' ' + W.tm + ' ').replace(/\s*÷\s*/g, ' ' + W.dv + ' ');
    s = s.replace(/\s*−\s*/g, ' ' + W.mi + ' ').replace(/(\d|\))\s+-\s+(?=[\d(a-z])/gi, '$1 ' + W.mi + ' ');
    s = s.replace(/([\w)\]])\s*=\s*(?=[\w(−\-√.,'"])/g, '$1 ' + W.eq + ' ');
    s = s.replace(/π/g, ' ' + W.pi + ' ').replace(/Δ(?=[A-Za-z])/g, W.delta + ' ').replace(/Δ/g, ' delta ').replace(/°\s*C\b/g, ' ' + W.dg + ' Celsius').replace(/°/g, ' ' + W.dg);
    s = s.replace(/([\w)])\s+\/\s+(?=[\w(])/g, '$1 ' + W.dv + ' ');
    s = s.replace(/…/g, '...').replace(/\s*;\s*/g, '; ').replace(/\s+([,.;:!?])/g, '$1').replace(/\s+/g, ' ').trim();
    return s;
  }
  /* one sentence per utterance; very long sentences are split at commas so no single utterance runs past ~220 characters */
  function sentences(s) {
    if (!s) return [];
    const out = [];
    s.replace(/([.!?…]["”»)]?)\s+(?=["“«(¿¡]?[A-ZÀ-ÝÄÖÜ0-9])/g, '$1\u2029').split('\u2029').forEach(x => {
      x = x.trim(); if (!x) return;
      if (x.length <= 220) { out.push(x); return; }
      let cur = ''; x.replace(/([,;:])\s+/g, '$1\u2028').split('\u2028').forEach(p => { if ((cur + ' ' + p).length > 200 && cur) { out.push(cur.trim()); cur = p; } else cur = (cur + ' ' + p).trim(); }); if (cur) out.push(cur);
    });
    return out;
  }
  const endDot = s => { s = String(s).trim(); return /[.!?…:]$/.test(s) ? s : s + '.'; };

  /* ---------- script builder ---------- */
  function Builder(lang, seed) {
    const P = bank(lang), r = rng(seed), L = [], ch = [];
    let c = -1, part = '';
    const b = {
      P, lang, L, ch,
      pick(k, v) { const a = P[k]; return fill(Array.isArray(a) ? a[Math.floor(r() * a.length)] : a, v); },
      chap(name) { ch.push(name); c = ch.length - 1; part = ''; },
      part(name) { part = name; },
      sec(key, solo) { const n = P.sec[key] || key; if (solo) b.chap(n); else b.part(n); },
      say(t, o) { o = o || {}; const ss = sentences(spoken(t, lang)); ss.forEach((x, j) => L.push({ t: x, s: c, sb: part, p: j === ss.length - 1 ? (o.p == null ? 520 : o.p) : 260, r: o.r || 1, pi: o.pi || 1, k: o.k || 'say' })); },
      line(k, v, o) { b.say(b.pick(k, v), o); },
      think(ms, label) { L.push({ k: 'think', ms, t: label || P.ui.think, s: c, sb: part }); }
    };
    return b;
  }
  const ASIDE = { r: 0.94, p: 700 }, EMPH = { r: 0.95, p: 650 }, ASK = { pi: 1.04, p: 450 };

  /* a topic from the syllabus (fields ov, kt, ex, fm, st, we, cm, rw, es, rc) */
  function topicInto(b, T, name, o) {
    const solo = !!o.solo, P = b.P;
    if (solo) { b.sec('intro', 1); b.line('hi', { t: name }, { p: 700 }); }
    else { b.chap(name); b.part(P.sec.intro); b.line('nextT', { t: name }, { p: 600 }); }
    if (T.ov) { b.sec('big', solo); b.line('big', null, ASIDE); b.say(T.ov, { p: 800 }); }
    if (T.kt && T.kt.length) { b.sec('terms', solo); b.line('terms', null, ASIDE); T.kt.forEach((k, i) => b.say(endDot(k), { p: i === T.kt.length - 1 ? 600 : 420 })); b.line('termsOut', null, ASIDE); }
    if (T.ex && T.ex.length) {
      b.sec('expl', solo); b.line('expl', null, ASIDE);
      T.ex.forEach((p, i) => { b.say(p, { p: 750 }); if (i < T.ex.length - 1) b.line('aside', null, ASIDE); });
    }
    if (T.fm && T.fm.length) { b.sec('fm', solo); b.line('fm', null, ASIDE); T.fm.forEach(f => b.say(endDot(f), { p: 900, r: 0.92 })); }
    if (T.st && T.st.length && o.method !== false) { b.sec('steps', solo); b.line('steps', null, ASIDE); T.st.forEach((x, i) => { b.say(fill(P.step, { n: i + 1 }), { p: 250 }); b.say(x, { p: 600 }); }); }
    const w = T.we;
    if (w && w.p) {
      b.sec('we', solo); b.line('we', null, ASIDE); b.say(w.p, { p: 600, r: 0.95 }); b.line('weTry', null, ASK); b.think(6000);
      b.line('weShow', null, ASIDE);
      (w.s || []).forEach((x, i, a) => { b.say(P.seq[i === a.length - 1 && a.length > 1 ? P.seq.length - 1 : Math.min(i, P.seq.length - 2)], { p: 200 }); b.say(x, { p: 650 }); });
      if (w.a) { const wa = strip(w.a).replace(/[.]$/, ''); if (wa.length > 48 || /:/.test(wa)) { b.line('weAns2', null, EMPH); b.say(endDot(wa), EMPH); } else b.line('weAns', { a: wa }, EMPH); }
      const v = strip(w.v || '').replace(/^(check|verify|verification|verifica|comprobación|comprueba|vérification|vérifie|kontrolle|probe|verificação|verifica-se)\s*:\s*/i, ''); if (v.replace(NONW, ' ').trim().split(' ').length >= 3) b.line('weChk', { v: endDot(v) });
    }
    if (T.cm && T.cm.length) { b.sec('cm', solo); b.line('cm', null, ASIDE); T.cm.forEach((x, i) => b.say(fill(P.cmEach[Math.min(i, P.cmEach.length - 1)], { x: endDot(strip(x)) }), { p: 600 })); b.line('cmOut', null, ASIDE); }
    if (T.rw) { b.sec('rw', solo); b.line('rw', null, ASIDE); b.say(T.rw, { p: 700 }); b.line('rwOut', null, ASIDE); }
    if (T.es) { b.sec('es', solo); b.line('es', null, ASIDE); b.say(T.es, { p: 700 }); }
    if (T.rc && T.rc.length) { b.sec('rc', solo); b.line('rc', null, ASIDE); T.rc.forEach(x => b.say(endDot(x), EMPH)); }
    const q = (o.qs || [])[0];
    if (q && q.o && q.o.length) { b.sec('q', solo); b.line('qIn', null, ASIDE); askMCQ(b, q); }
    if (solo) { b.sec('end', 1); b.line('bye', { t: name }, { p: 400 }); }
  }
  function askMCQ(b, q) {
    const P = b.P; b.say(q.q, ASK); q.o.forEach((x, i) => b.say(fill(P.opt, { l: 'ABCD'[i], o: strip(x).replace(/[.]$/, '') }), { p: 380 }));
    b.line('qThink', null, ASK); b.think(7000);
    b.line('qAns', { l: 'ABCD'[q.a], o: strip(q.o[q.a]).replace(/[.]$/, '') }, EMPH);
    if (q.e) b.say(fill(P.qWhy, { e: endDot(strip(q.e)) }), { p: 700 });
    b.line('qGood', null, ASIDE);
  }
  function langOf(T, fb) { return detect([T.ov].concat(T.ex || []).join(' '), fb); }

  const API = {};
  /* single topic */
  API.topic = function (T, name, ctx) {
    ctx = ctx || {}; const lang = langOf(T, ctx.lang), b = Builder(lang, 'topic|' + name);
    topicInto(b, T, name, { solo: true, qs: ctx.qs });
    return { key: ctx.key || 'topic|' + name, title: name, sub: ctx.subject || '', lang, L: b.L, ch: b.ch, kind: 'topic', ctx };
  };
  /* several topics in a row (a module, a subject, weak topics) */
  API.playlist = function (title, items, ctx) {
    ctx = ctx || {}; items = items.filter(x => x && x.T);
    const lang = detect(items.slice(0, 3).map(x => [x.T.ov].concat(x.T.ex || []).join(' ')).join(' '), ctx.lang), b = Builder(lang, 'list|' + title), P = b.P;
    b.chap(P.sec.intro); b.line('modIn', { t: title, n: items.length }, { p: 800 });
    items.forEach(x => topicInto(b, x.T, x.name, { solo: false, qs: x.qs, method: false }));
    b.chap(P.sec.end); b.line('modBye', null, { p: 400 });
    return { key: ctx.key || 'list|' + title, title, sub: ctx.subject || '', lang, L: b.L, ch: b.ch, kind: 'list', ctx };
  };
  /* flashcards: [[front, back], ...] */
  API.cards = function (title, cards, ctx) {
    ctx = ctx || {}; const lang = detect(cards.slice(0, 20).map(c => c[0] + ' ' + c[1]).join(' '), ctx.lang), b = Builder(lang, 'cards|' + title), P = b.P;
    b.chap(P.sec.intro); b.line('cardIn', null, { p: 700 });
    cards.forEach((c, i) => { b.chap((i + 1) + '. ' + strip(c[0]).slice(0, 60)); b.say(endDot(c[0]), ASK); b.line('cardThink', null, ASK); b.think(4500); b.line('cardBack', { a: endDot(strip(c[1])) }, EMPH); });
    b.chap(P.sec.end); b.line('modBye', null, { p: 400 });
    return { key: ctx.key || 'cards|' + title, title, sub: ctx.subject || '', lang, L: b.L, ch: b.ch, kind: 'cards', ctx };
  };
  /* practice questions: {q, o:[..], a, e} or theory {q, pts:[..]} */
  API.questions = function (title, qs, ctx) {
    ctx = ctx || {}; const lang = detect(qs.slice(0, 10).map(q => q.q + ' ' + (q.e || '')).join(' '), ctx.lang), b = Builder(lang, 'qs|' + title), P = b.P;
    b.chap(P.sec.intro); b.line('qsIn', null, { p: 700 });
    qs.forEach((q, i) => {
      b.chap(fill(P.qsN, { n: i + 1 }).replace(/\.$/, '')); b.say(fill(P.qsN, { n: i + 1 }), { p: 300 });
      if (q.pts) { b.say(P.thIn, { p: 300 }); b.say(q.q, ASK); b.line('thThink', null, ASK); b.think(9000); b.say(P.thPts, EMPH); q.pts.forEach(x => b.say(endDot(x), { p: 500 })); }
      else askMCQ(b, q);
    });
    b.chap(P.sec.end); b.line('modBye', null, { p: 400 });
    return { key: ctx.key || 'qs|' + title, title, sub: ctx.subject || '', lang, L: b.L, ch: b.ch, kind: 'qs', ctx };
  };
  /* Ace Academy lesson: body blocks {p}{h}{list}{steps}{tip}{code,lang}{check} */
  function lessonInto(b, l, solo) {
    const P = b.P;
    if (solo) { b.chap(P.sec.intro); b.line('lesIn', { t: l.title, m: l.minutes || 10 }, { p: 700 }); }
    else { b.chap(l.title); b.part(P.sec.intro); b.line('nextT', { t: l.title }, { p: 600 }); }
    let paras = 0;
    (l.body || []).forEach((x, i, a) => {
      if (x.h != null) { if (solo) b.chap(strip(x.h)); else b.part(strip(x.h)); b.line('head', { h: strip(x.h).replace(/[.]$/, '') }, ASIDE); paras = 0; }
      else if (x.p != null) { if (paras > 0 && paras % 2 === 0 && a[i + 1] && a[i + 1].p != null) b.line('aside', null, ASIDE); b.say(x.p, { p: 700 }); paras++; }
      else if (x.list) { b.line('list', null, ASIDE); x.list.forEach(y => b.say(endDot(y), { p: 550 })); }
      else if (x.steps) { x.steps.forEach((y, n) => { b.say(fill(P.step, { n: n + 1 }), { p: 220 }); b.say(endDot(y), { p: 600 }); }); }
      else if (x.tip != null) { b.line('tip', null, ASIDE); b.say(x.tip, EMPH); }
      else if (x.code != null) { b.say(fill(P.code, { n: String(x.code).split('\n').length }), ASIDE); b.think(5000, P.ui.look); }
      else if (x.check) { const c = x.check; b.say(P.chk, ASIDE); askMCQ(b, { q: c.q, o: c.o, a: c.a, e: c.e }); }
    });
    if (solo) { b.chap(P.sec.end); b.line('lesBye', null, { p: 400 }); }
  }
  API.lesson = function (l, ctx) {
    ctx = ctx || {}; const b = Builder(ctx.lang || 'en', 'les|' + l.id); lessonInto(b, l, true);
    return { key: ctx.key || 'les|' + l.id, title: l.title, sub: ctx.subject || '', lang: b.lang, L: b.L, ch: b.ch, kind: 'lesson', ctx };
  };
  API.course = function (c, from, ctx) {
    ctx = ctx || {}; const b = Builder(ctx.lang || 'en', 'course|' + c.slug), P = b.P, ls = c.lessons.slice(from || 0);
    b.chap(P.sec.intro); b.line('courseIn', { t: c.title, n: ls.length }, { p: 800 });
    ls.forEach(l => lessonInto(b, l, false));
    b.chap(P.sec.end); b.line('modBye', null, { p: 400 });
    return { key: ctx.key || 'course|' + c.slug, title: c.title, sub: ctx.subject || '', lang: b.lang, L: b.L, ch: b.ch, kind: 'course', ctx };
  };

  /* ---------- voices ---------- */
  let VOICES = [];
  function loadVoices() { try { VOICES = SY ? SY.getVoices() : []; } catch (e) { VOICES = []; } }
  if (SY) { loadVoices(); try { SY.addEventListener('voiceschanged', () => { loadVoices(); if (DOCK && !DOCK.hidden) paint(); }); } catch (e) { SY.onvoiceschanged = loadVoices; } }
  function voicesFor(lang) { const l = (lang || 'en').slice(0, 2).toLowerCase(); return VOICES.filter(v => v.lang && v.lang.replace('_', '-').toLowerCase().slice(0, 2) === l); }
  function score(v, region) {
    let s = 0; const n = v.name || '';
    if (/natural|neural|online|premium|enhanced|wavenet|studio/i.test(n)) s += 6;
    if (/google/i.test(n)) s += 3; if (/siri|samantha|daniel|karen|moira|serena|alice|thomas|amélie|anna|paulina|monica|luciana/i.test(n)) s += 2;
    if (/compact|espeak|robot/i.test(n)) s -= 5;
    if (region && v.lang && v.lang.replace('_', '-').toUpperCase().endsWith('-' + region.toUpperCase())) s += 3;
    if (v.localService === false) s += 1;
    return s;
  }
  function pickVoice(lang, region) {
    const vs = voicesFor(lang); if (!vs.length) return null;
    const want = LS.get('ace-voice-' + lang.slice(0, 2)); const m = want && vs.find(v => v.name === want); if (m) return m;
    return vs.slice().sort((a, b) => score(b, region) - score(a, region))[0];
  }

  /* ---------- engine ---------- */
  const E = { S: null, i: 0, on: false, gen: 0, tm: null, iv: null, rate: +(LS.get('ace-rate') || 1) || 1, xbusy: false, captions: false };
  const RATE_BASE = 0.97;
  function clear() { E.gen++; clearTimeout(E.tm); clearInterval(E.iv); E.tm = E.iv = null; try { if (SY) SY.cancel(); } catch (e) { } }
  function savePos() { if (E.S && E.S.key) { try { const m = JSON.parse(LS.get('ace-audio-pos') || '{}'); m[E.S.key] = { i: E.i, n: E.S.L.length, t: E.S.title, at: Date.now() }; const ks = Object.keys(m).sort((a, b) => m[b].at - m[a].at).slice(0, 40), o = {}; ks.forEach(k => o[k] = m[k]); LS.set('ace-audio-pos', JSON.stringify(o)); LS.set('ace-audio-last', JSON.stringify({ key: E.S.key, t: E.S.title, sub: E.S.sub, ctx: E.S.ctx && E.S.ctx.resume || null })); } catch (e) { } } }
  function posOf(key) { try { return JSON.parse(LS.get('ace-audio-pos') || '{}')[key] || null; } catch (e) { return null; } }
  function step(g) {
    if (g !== E.gen) return;
    const S = E.S; if (!S) return;
    if (E.i >= S.L.length) { finish(); return; }
    const ln = S.L[E.i]; paint();
    if (E.i % 5 === 0) savePos();
    if (ln.k === 'think') { E.tm = setTimeout(() => { if (g !== E.gen) return; E.i++; step(g); }, ln.ms / Math.max(0.75, E.rate)); return; }
    const v = SY && pickVoice(S.lang, S.ctx && S.ctx.region);
    if (!SY || !v) { E.captions = true; paint(); E.tm = setTimeout(() => adv(g, ln), Math.max(1500, ln.t.split(' ').length * 360 / E.rate)); return; }
    E.captions = false;
    const u = new SpeechSynthesisUtterance(ln.t); u.voice = v; u.lang = v.lang; u.rate = Math.min(2, RATE_BASE * E.rate * (ln.r || 1)); u.pitch = ln.pi || 1;
    let fired = false; const done = () => { if (fired) return; fired = true; clearInterval(E.iv); adv(g, ln); };
    u.onend = done; u.onerror = e => { if (g !== E.gen) return; if (e && (e.error === 'interrupted' || e.error === 'canceled')) return; done(); };
    u.onboundary = e => { if (g === E.gen && e.name !== 'sentence') mark(e.charIndex); };
    E.tm = setTimeout(() => {
      if (g !== E.gen) return; try { SY.speak(u); } catch (e) { done(); return; }
      let idle = 0; E.iv = setInterval(() => { if (g !== E.gen) { clearInterval(E.iv); return; } if (!SY.speaking && !SY.pending) { if (++idle >= 3) done(); } else idle = 0; }, 700);
    }, 40);
  }
  function adv(g, ln) { if (g !== E.gen) return; E.tm = setTimeout(() => { if (g !== E.gen) return; E.i++; step(g); }, (ln.p == null ? 400 : ln.p) / Math.max(0.75, E.rate)); }
  function finish() { E.on = false; savePos(); paint(); mood('cheer'); setTimeout(() => mood('idle'), 2500); }
  function go(i) { clear(); if (!E.S) return; E.i = Math.max(0, Math.min(i, E.S.L.length)); E.on = true; if (E.i >= E.S.L.length) E.i = 0; step(E.gen); }
  function pause() { clear(); E.on = false; savePos(); paint(); }
  function chStart(c) { const L = E.S.L; for (let i = 0; i < L.length; i++) if (L[i].s === c) return i; return 0; }
  function nextPart() { const L = E.S.L, cur = L[Math.min(E.i, L.length - 1)]; let i = E.i + 1; while (i < L.length && L[i].s === cur.s && L[i].sb === cur.sb) i++; go(i); }
  function prevLine() { let i = E.i - 1; while (i > 0 && E.S.L[i].k === 'think') i--; go(i); }

  API.play = function (S, opt) {
    opt = opt || {}; if (!S || !S.L || !S.L.length) return;
    clear(); E.S = S; build(); open();
    const p = posOf(S.key); let at = opt.at != null ? opt.at : 0;
    if (opt.at == null && p && p.n === S.L.length && p.i > 3 && p.i < S.L.length - 2) { at = Math.max(0, p.i - 1); toast(bank(S.lang).ui.resume); }
    go(at);
  };
  API.toggle = function (key, make, opt) { if (E.S && E.S.key === key) { if (E.on) pause(); else go(E.i); return; } const S = make(); if (S) { S.key = key; API.play(S, opt); } };
  API.stop = function () { clear(); E.on = false; savePos(); E.S = null; if (DOCK) { DOCK.classList.remove('in'); DOCK.hidden = true; } document.documentElement.classList.remove('at-open'); sync(); };
  API.pause = () => { if (E.on) pause(); };
  API.isOn = key => !!(E.S && E.S.key === key && E.on);
  API.last = () => { try { return JSON.parse(LS.get('ace-audio-last') || 'null'); } catch (e) { return null; } };
  API.pos = posOf;
  API.t = (k, lang) => bank(lang || (document.documentElement.lang || 'en')).ui[k] || PB.en.ui[k] || k;
  API.voiceFor = (lang, region) => pickVoice(lang || 'en', region);
  API.rate = () => E.rate;
  API.spoken = spoken; API.sentences = sentences; API.detect = detect; API.bank = bank;
  API.state = () => ({ key: E.S && E.S.key, i: E.i, n: E.S ? E.S.L.length : 0, on: E.on, captions: E.captions, lang: E.S && E.S.lang });

  /* "Explain this more": asks Ace (AI) for a spoken explanation of the current passage with a real-life example */
  async function explain() {
    const S = E.S; if (!S || !S.ctx || typeof S.ctx.explain !== 'function' || E.xbusy) return;
    const U = bank(S.lang).ui, P = bank(S.lang), L = S.L, at = Math.min(E.i, L.length - 1), cur = L[at];
    let a = at, z = at; while (a > 0 && L[a - 1].s === cur.s && L[a - 1].sb === cur.sb && at - a < 6) a--; while (z < L.length - 1 && L[z + 1].s === cur.s && L[z + 1].sb === cur.sb && z - at < 3) z++;
    const passage = L.slice(a, z + 1).filter(x => x.k !== 'think').map(x => x.t).join(' ');
    pause(); E.xbusy = true; paint();
    let txt = '';
    try { txt = await S.ctx.explain(passage, { title: S.title, subject: S.sub, part: cur.sb || S.ch[cur.s] || '', lang: S.lang }); } catch (e) { txt = ''; toast((e && e.msg) || U.signin); }
    E.xbusy = false;
    const ins = []; const push = (t, o) => { sentences(spoken(t, S.lang)).forEach((x, j, arr) => ins.push({ t: x, s: cur.s, sb: P.sec.x, p: j === arr.length - 1 ? ((o && o.p) || 600) : 280, r: (o && o.r) || 1, k: 'x' })); };
    if (txt) { push(P.xIn, ASIDE); push(txt); push(P.xOut, ASIDE); } else push(P.xFail, ASIDE);
    S.L.splice(at, 0, ...ins); S.key = S.key + '+x'; build(); go(at);
  }

  /* ---------- player UI ---------- */
  let DOCK = null, CAP = null, toastT = null;
  const ic = {
    play: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13a1 1 0 0 0 1.5.86l10.5-6.5a1 1 0 0 0 0-1.72L9.5 4.64A1 1 0 0 0 8 5.5z"/></svg>',
    pause: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="6.5" y="5" width="4" height="14" rx="1.2"/><rect x="13.5" y="5" width="4" height="14" rx="1.2"/></svg>',
    back: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5V2L7 6l5 4V7a6 6 0 1 1-6 6H4a8 8 0 1 0 8-8z"/></svg>',
    next: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 6.5v11a1 1 0 0 0 1.6.8L14 12.8V17a1 1 0 0 0 2 0V7a1 1 0 0 0-2 0v4.2L6.6 5.7A1 1 0 0 0 5 6.5z"/></svg>',
    more: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 14l5-5 5 5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    x: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>'
  };
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[m]));
  function css() {
    if (document.getElementById('at-css')) return;
    const st = document.createElement('style'); st.id = 'at-css';
    st.textContent = `
.at-dock{--at-bg:var(--surface,var(--card,#fff));--at-fg:var(--text,var(--ink,#17123A));--at-mut:var(--text3,var(--mut,#5c5a72));--at-line:var(--border,var(--line,#d9dcf5));--at-pri:var(--primary,var(--pri,#3D35F5));--at-btn:var(--btn,var(--pri,#3D35F5));--at-on:var(--priInk,#fff);--at-tint:var(--tint,var(--soft,#eceeff));--at-hi:var(--yellow,var(--gold,#FFC72C));
 position:fixed;z-index:60;left:var(--at-l,0px);right:0;bottom:calc(var(--at-b,0px) + 10px + env(safe-area-inset-bottom,0px));margin:0 auto;width:min(760px,calc(100% - var(--at-l,0px) - 20px));
 background:var(--at-bg);color:var(--at-fg);border:1.5px solid var(--at-line);border-radius:22px;box-shadow:0 18px 50px -18px rgba(20,16,70,.45),0 2px 0 var(--at-line);
 font-family:var(--fb,'Atkinson Hyperlegible',system-ui,sans-serif);transform:translateY(130%);opacity:0;transition:transform .55s cubic-bezier(.34,1.56,.64,1),opacity .3s}
.at-dock.in{transform:none;opacity:1}
.at-bar{height:4px;background:var(--at-tint);border-radius:22px 22px 0 0;overflow:hidden}.at-bar i{display:block;height:100%;background:var(--at-pri);width:0;transition:width .5s ease}
.at-row{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:12px;align-items:center;padding:10px 12px 10px 10px}
.at-av{position:relative;width:54px;height:54px;border:0;border-radius:50%;background:var(--at-tint);padding:0;cursor:pointer;flex:none;display:grid;place-items:center;color:var(--at-pri)}
.at-av .ace{width:40px;height:40px;display:block}.at-av .ace svg{width:100%;height:100%}
.at-av .at-ring{position:absolute;inset:-3px;border-radius:50%;border:2.5px solid var(--at-pri);opacity:0}
.at-dock[data-st=talk] .at-av .at-ring{animation:atpulse 1.6s ease-out infinite}.at-dock[data-st=talk] .at-av .at-ring+.at-ring{animation-delay:.8s}
.at-dock[data-st=talk] .at-av .ace{animation:attalk .42s ease-in-out infinite alternate}
.at-cd{position:absolute;inset:-3px;width:60px;height:60px;transform:rotate(-90deg);pointer-events:none;opacity:0}
.at-dock[data-st=think] .at-cd{opacity:1}.at-cd circle{fill:none;stroke:var(--at-hi);stroke-width:4;stroke-linecap:round;stroke-dasharray:176;stroke-dashoffset:0}
.at-mid{min-width:0}
.at-k{display:flex;gap:8px;align-items:baseline;font-size:12px;color:var(--at-mut);white-space:nowrap;overflow:hidden}
.at-k b{color:var(--at-pri);font-weight:700;overflow:hidden;text-overflow:ellipsis;max-width:55%}.at-k span{overflow:hidden;text-overflow:ellipsis}
.at-cap{margin:3px 0 0;font:600 15px/1.4 var(--fb,system-ui);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;min-height:2.8em}
.at-cap .w{transition:color .15s,background-color .15s;border-radius:4px}.at-cap .w.on{background:var(--at-hi);color:#17123A}.at-cap .w.past{color:var(--at-mut)}
.at-dock[data-st=think] .at-cap{color:var(--at-pri)}
.at-eq{display:inline-flex;gap:2px;align-items:flex-end;height:12px;margin-left:auto;flex:none}.at-eq i{width:3px;height:30%;background:var(--at-pri);border-radius:2px}
.at-dock[data-st=talk] .at-eq i{animation:ateq .9s ease-in-out infinite}.at-eq i:nth-child(2){animation-delay:-.3s!important}.at-eq i:nth-child(3){animation-delay:-.55s!important}.at-eq i:nth-child(4){animation-delay:-.15s!important}
.at-ctl{display:flex;gap:4px;align-items:center}
.at-ctl button,.at-x{border:0;background:transparent;color:var(--at-fg);width:40px;height:40px;border-radius:12px;display:grid;place-items:center;cursor:pointer;padding:0;font:700 13px var(--fb,system-ui)}
.at-ctl button:hover,.at-x:hover{background:var(--at-tint)}.at-ctl svg,.at-x svg{width:22px;height:22px;fill:currentColor}
.at-ctl .at-pp{width:48px;height:48px;border-radius:50%;background:var(--at-btn);color:var(--at-on);box-shadow:0 3px 0 var(--btn-ledge,rgba(0,0,0,.25));transition:transform .15s}
.at-ctl .at-pp:hover{background:var(--at-btn);transform:scale(1.06)}.at-ctl .at-pp:active{transform:translateY(2px);box-shadow:none}
.at-sp{min-width:44px;width:auto!important;padding:0 6px!important;font-variant-numeric:tabular-nums}
.at-dock.open .at-mo svg{transform:rotate(180deg)}.at-mo svg{transition:transform .3s}
.at-xp{display:flex;gap:8px;flex-wrap:wrap;margin-top:6px}
.at-xb{border:1.5px solid var(--at-line);background:var(--at-bg);color:var(--at-pri);border-radius:99px;padding:5px 12px;font:700 12.5px var(--fb,system-ui);cursor:pointer;transition:transform .15s,background-color .15s}
.at-xb:hover{background:var(--at-tint);transform:translateY(-1px)}.at-xb[disabled]{opacity:.6;cursor:progress}.at-xb small{font-weight:400;color:var(--at-mut);margin-left:4px}
.at-pn[hidden],.at-dock[hidden]{display:none}
.at-pn{border-top:1.5px solid var(--at-line);max-height:min(46vh,420px);display:grid;grid-template-rows:auto minmax(0,1fr)}
.at-tabs{display:flex;gap:4px;padding:8px 10px 0}.at-tabs button{border:0;background:transparent;color:var(--at-mut);font:700 13px var(--fb,system-ui);padding:8px 12px;border-radius:10px;cursor:pointer}
.at-tabs button[aria-selected=true]{background:var(--at-tint);color:var(--at-fg)}
.at-body{overflow:auto;padding:8px 10px 12px;overscroll-behavior:contain}
.at-ln{display:block;width:100%;text-align:left;border:0;background:transparent;color:var(--at-fg);padding:6px 10px;border-radius:10px;font:15px/1.45 var(--fb,system-ui);cursor:pointer}
.at-ln:hover{background:var(--at-tint)}.at-ln.on{background:var(--at-tint);box-shadow:inset 3px 0 0 var(--at-pri);font-weight:700}.at-ln.th{color:var(--at-mut);font-style:italic}.at-ln.xx{color:var(--at-pri)}
.at-h{font:700 12px var(--fb,system-ui);color:var(--at-mut);margin:10px 10px 2px}
.at-chs{display:grid;gap:4px}.at-ch{display:grid;grid-template-columns:28px minmax(0,1fr);gap:8px;align-items:center;text-align:left;border:0;background:transparent;color:var(--at-fg);padding:8px 10px;border-radius:12px;font:600 14px var(--fb,system-ui);cursor:pointer}
.at-ch:hover{background:var(--at-tint)}.at-ch i{width:26px;height:26px;border-radius:50%;display:grid;place-items:center;background:var(--at-tint);font-style:normal;font-size:12px;font-weight:700;color:var(--at-mut)}
.at-ch.dn i{background:var(--at-pri);color:var(--at-on)}.at-ch.on{background:var(--at-tint)}.at-ch.on i{background:var(--at-hi);color:#17123A}
.at-vo{display:grid;gap:12px;padding:6px 6px 4px}.at-vo label{display:grid;gap:6px;font:700 13px var(--fb,system-ui)}
.at-vo select{width:100%;padding:10px;border-radius:12px;border:1.5px solid var(--at-line);background:var(--at-bg);color:var(--at-fg);font:15px var(--fb,system-ui)}
.at-vo input[type=range]{width:100%;accent-color:var(--at-pri)}.at-vo .row{display:flex;gap:8px;flex-wrap:wrap}
.at-note{font-size:12.5px;color:var(--at-mut);margin:0}
.at-toast{position:absolute;left:50%;bottom:calc(100% + 8px);transform:translateX(-50%);background:var(--at-fg);color:var(--at-bg);padding:6px 12px;border-radius:99px;font:700 12.5px var(--fb,system-ui);white-space:nowrap;max-width:94%;overflow:hidden;text-overflow:ellipsis;opacity:0;transition:opacity .3s,transform .3s;pointer-events:none}
.at-toast.on{opacity:1;transform:translate(-50%,-3px)}
html.at-open body{padding-bottom:calc(var(--at-h,120px) + 20px)}
[data-at-key].at-on{position:relative}
[data-at-key].at-on::after{content:'';position:absolute;right:6px;top:50%;width:6px;height:6px;margin-top:-3px;border-radius:50%;background:currentColor;animation:atblink 1s ease-in-out infinite}
@keyframes atpulse{0%{transform:scale(1);opacity:.7}100%{transform:scale(1.35);opacity:0}}
@keyframes attalk{from{transform:translateY(0) rotate(-2deg)}to{transform:translateY(-2px) rotate(2deg)}}
@keyframes ateq{0%,100%{height:25%}50%{height:100%}}
@keyframes atblink{50%{opacity:.25}}
@media (max-width:560px){.at-dock{width:calc(100% - 16px);border-radius:20px}.at-row{gap:8px;padding:8px}.at-av{width:46px;height:46px}.at-av .ace{width:34px;height:34px}.at-cd{width:52px;height:52px}
 .at-ctl .at-bk,.at-ctl .at-sp{display:none}.at-ctl button{width:36px;height:36px}.at-ctl .at-pp{width:44px;height:44px}.at-cap{font-size:14px}}
@media (prefers-reduced-motion:reduce){.at-dock,.at-dock *{animation:none!important;transition:none!important}}`;
    document.head.appendChild(st);
  }
  function build() {
    css();
    const U = bank(E.S.lang).ui;
    if (!DOCK) {
      DOCK = document.createElement('section'); DOCK.className = 'at-dock'; DOCK.hidden = true; document.body.appendChild(DOCK);
      DOCK.addEventListener('click', onClick); DOCK.addEventListener('input', onInput); DOCK.addEventListener('change', onInput);
      DOCK.addEventListener('keydown', e => { if (e.key === 'Escape' && DOCK.classList.contains('open')) { DOCK.classList.remove('open'); paint(true); } });
      window.addEventListener('resize', place); new MutationObserver(sync).observe(document.body, { childList: true, subtree: true });
    }
    DOCK.setAttribute('aria-label', U.audio);
    const av = (window.AceUI && AceUI.svg && AceUI.svg()) ? `<span class="ace" data-mood="idle">${AceUI.svg()}</span>` : `<svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true" fill="currentColor"><path d="M12 3a4 4 0 0 1 4 4v5a4 4 0 0 1-8 0V7a4 4 0 0 1 4-4zm-7 9h2a5 5 0 0 0 10 0h2a7 7 0 0 1-6 6.92V21h-2v-2.08A7 7 0 0 1 5 12z"/></svg>`;
    DOCK.innerHTML = `<div class="at-toast" role="status"></div><div class="at-bar"><i></i></div><div class="at-row">
<button class="at-av" data-t="open" aria-label="${esc(U.transcript)}"><i class="at-ring"></i><i class="at-ring"></i>${av}<svg class="at-cd" viewBox="0 0 60 60"><circle cx="30" cy="30" r="28"/></svg></button>
<div class="at-mid"><div class="at-k"><b></b><span></span><span class="at-eq" aria-hidden="true"><i></i><i></i><i></i><i></i></span></div><p class="at-cap"></p><div class="at-xp"></div></div>
<div class="at-ctl"><button class="at-bk" data-t="back" aria-label="${esc(U.back)}" title="${esc(U.back)}">${ic.back}</button><button class="at-pp" data-t="pp"></button><button data-t="next" aria-label="${esc(U.next)}" title="${esc(U.next)}">${ic.next}</button><button class="at-sp" data-t="speed" aria-label="${esc(U.speed)}" title="${esc(U.speed)}"></button><button class="at-mo" data-t="open" aria-label="${esc(U.more)}" aria-expanded="false">${ic.more}</button><button data-t="close" aria-label="${esc(U.close)}" title="${esc(U.close)}">${ic.x}</button></div></div>
<div class="at-pn" hidden><div class="at-tabs" role="tablist"><button role="tab" data-t="tab" data-v="tr">${esc(U.transcript)}</button><button role="tab" data-t="tab" data-v="ch">${esc(U.chapters)}</button><button role="tab" data-t="tab" data-v="vo">${esc(U.voice)}</button></div><div class="at-body"></div></div>`;
    CAP = DOCK.querySelector('.at-cap'); E.tab = E.tab || 'tr';
  }
  function open() { DOCK.hidden = false; document.documentElement.classList.add('at-open'); place(); requestAnimationFrame(() => requestAnimationFrame(() => DOCK.classList.add('in'))); }
  function place() {
    if (!DOCK || DOCK.hidden) return; const nav = document.querySelector('nav'); let b = 0, l = 0;
    if (nav) { const cs = getComputedStyle(nav), r = nav.getBoundingClientRect(); if (cs.position === 'fixed' && r.height > 0) { if (r.top > innerHeight / 2) b = Math.max(0, innerHeight - r.top); else if (r.height > innerHeight / 2 && r.left < 10) l = r.right; } }
    DOCK.style.setProperty('--at-b', b + 'px'); DOCK.style.setProperty('--at-l', l + 'px');
    document.documentElement.style.setProperty('--at-h', DOCK.offsetHeight + 'px');
  }
  function mood(m) { const a = DOCK && DOCK.querySelector('.at-av .ace'); if (a) a.dataset.mood = m; }
  function toast(t) { if (!DOCK) return; const el = DOCK.querySelector('.at-toast'); el.textContent = t; el.classList.add('on'); clearTimeout(toastT); toastT = setTimeout(() => el.classList.remove('on'), 2600); }
  let CUR = { t: null, starts: [] };
  function setCap(t) {
    if (CUR.t === t) return; CUR.t = t; const parts = t.split(/(\s+)/); let pos = 0; CUR.starts = []; let h = '';
    parts.forEach(p => { if (!p) return; if (/^\s+$/.test(p)) { h += p; pos += p.length; return; } CUR.starts.push(pos); h += `<span class="w">${esc(p)}</span>`; pos += p.length; });
    CAP.innerHTML = h;
  }
  function mark(ci) { if (!CAP) return; const ws = CAP.querySelectorAll('.w'); let k = 0; for (let i = 0; i < CUR.starts.length; i++) if (CUR.starts[i] <= ci) k = i; ws.forEach((w, i) => { w.classList.toggle('on', i === k); w.classList.toggle('past', i < k); }); }
  function paint(force) {
    if (!DOCK || !E.S) return; const S = E.S, U = bank(S.lang).ui, L = S.L, ln = L[Math.min(E.i, L.length - 1)] || {};
    const think = E.on && ln.k === 'think', talk = E.on && !think && !E.captions;
    DOCK.dataset.st = E.xbusy ? 'load' : think ? 'think' : talk ? 'talk' : E.on ? 'cap' : 'pause';
    DOCK.querySelector('.at-bar i').style.width = (L.length ? Math.round(100 * Math.min(E.i, L.length) / L.length) : 0) + '%';
    DOCK.querySelector('.at-k b').textContent = S.title; DOCK.querySelector('.at-k span').textContent = ln.sb || S.ch[ln.s] || '';
    if (E.xbusy) setCap(U.explainBusy); else if (E.i >= L.length) setCap(bank(S.lang).sec.end + ' ✓'); else setCap(think ? (ln.t || U.think) + '…' : ln.t || '');
    const cd = DOCK.querySelector('.at-cd circle'); if (cd) { cd.style.transition = 'none'; cd.style.strokeDashoffset = '0'; if (think && !RM.matches) { void cd.getBoundingClientRect(); cd.style.transition = `stroke-dashoffset ${ln.ms / Math.max(0.75, E.rate)}ms linear`; cd.style.strokeDashoffset = '176'; } }
    mood(think ? 'think' : E.i >= L.length ? 'cheer' : 'idle');
    const pp = DOCK.querySelector('.at-pp'); pp.innerHTML = E.on ? ic.pause : ic.play; pp.setAttribute('aria-label', E.on ? U.pause : U.play); pp.title = pp.getAttribute('aria-label');
    DOCK.querySelector('.at-sp').textContent = (Math.round(E.rate * 100) / 100) + '×';
    const xp = DOCK.querySelector('.at-xp');
    xp.innerHTML = (S.ctx && typeof S.ctx.explain === 'function' && E.i < L.length ? `<button class="at-xb" data-t="explain" ${E.xbusy ? 'disabled' : ''}>💬 ${esc(E.xbusy ? U.explainBusy : U.explain)}<small>${esc(U.aiNote)}</small></button>` : '') + (E.i >= L.length ? `<button class="at-xb" data-t="restart">↺ ${esc(U.restart)}</button>` : '') + (E.captions && E.on ? `<p class="at-note">${esc(U.novoice)}</p>` : '');
    const pn = DOCK.querySelector('.at-pn'), opn = DOCK.classList.contains('open'); pn.hidden = !opn; DOCK.querySelector('.at-mo').setAttribute('aria-expanded', String(opn));
    if (opn) panel(force);
    place(); sync();
  }
  let PNK = '';
  function panel(force) {
    const S = E.S, U = bank(S.lang).ui, L = S.L, ln = L[Math.min(E.i, L.length - 1)] || {}, body = DOCK.querySelector('.at-body');
    DOCK.querySelectorAll('.at-tabs button').forEach(b => b.setAttribute('aria-selected', String(b.dataset.v === E.tab)));
    if (E.tab === 'tr') {
      const k = 'tr|' + S.key + '|' + ln.s + '|' + L.length;
      if (force || PNK !== k) { PNK = k; let h = '', lastSb = null; L.forEach((x, i) => { if (x.s !== ln.s) return; if (x.sb && x.sb !== lastSb) { h += `<p class="at-h">${esc(x.sb)}</p>`; lastSb = x.sb; } h += `<button class="at-ln ${x.k === 'think' ? 'th' : ''} ${x.k === 'x' ? 'xx' : ''}" data-t="jump" data-v="${i}">${esc(x.k === 'think' ? '⏳ ' + x.t + '…' : x.t)}</button>`; }); body.innerHTML = `<p class="at-h">${esc(S.ch[ln.s] || '')}</p>` + h; }
      body.querySelectorAll('.at-ln').forEach(b => b.classList.toggle('on', +b.dataset.v === E.i));
      const on = body.querySelector('.at-ln.on'); if (on) { const r = on.offsetTop - body.clientHeight / 3; body.scrollTo({ top: r, behavior: RM.matches ? 'auto' : 'smooth' }); }
    } else if (E.tab === 'ch') {
      const k = 'ch|' + S.key + '|' + ln.s; if (!force && PNK === k) return; PNK = k;
      body.innerHTML = `<div class="at-chs">${S.ch.map((c, i) => `<button class="at-ch ${i < ln.s ? 'dn' : ''} ${i === ln.s ? 'on' : ''}" data-t="ch" data-v="${i}"><i>${i < ln.s ? '✓' : i + 1}</i><span>${esc(c)}</span></button>`).join('')}</div>`;
      const on = body.querySelector('.at-ch.on'); if (on) on.scrollIntoView({ block: 'nearest' });
    } else {
      const k = 'vo|' + S.lang + '|' + VOICES.length + '|' + E.rate; if (!force && PNK === k) return; PNK = k;
      const vs = voicesFor(S.lang), cur = LS.get('ace-voice-' + S.lang.slice(0, 2)) || '';
      body.innerHTML = `<div class="at-vo"><label>${esc(U.voice)}<select data-t="voice">${`<option value="">${esc(U.best)}</option>` + vs.map(v => `<option value="${esc(v.name)}" ${v.name === cur ? 'selected' : ''}>${esc(v.name)} (${esc(v.lang)})</option>`).join('')}</select></label>
<label>${esc(U.speed)}: <output>${E.rate.toFixed(2)}×</output><input type="range" min="0.7" max="1.6" step="0.05" value="${E.rate}" data-t="rate"></label>
<div class="row"><button class="at-xb" data-t="test">▶ ${esc(U.test)}</button></div>${vs.length ? '' : `<p class="at-note">${esc(U.novoice)}</p>`}</div>`;
    }
  }
  function onClick(e) {
    const b = e.target.closest('[data-t]'); if (!b || !E.S) return; const t = b.dataset.t;
    if (t === 'pp') { if (E.on) pause(); else go(E.i >= E.S.L.length ? 0 : E.i); }
    else if (t === 'back') prevLine();
    else if (t === 'next') nextPart();
    else if (t === 'speed') { const R = [0.85, 1, 1.15, 1.3, 1.5], k = R.findIndex(x => x > E.rate + 0.01); setRate(R[k < 0 ? 0 : k]); }
    else if (t === 'open') { DOCK.classList.toggle('open'); paint(true); }
    else if (t === 'close') API.stop();
    else if (t === 'tab') { E.tab = b.dataset.v; paint(true); }
    else if (t === 'jump') go(+b.dataset.v);
    else if (t === 'ch') go(chStart(+b.dataset.v));
    else if (t === 'explain') explain();
    else if (t === 'restart') go(0);
    else if (t === 'test') { const was = E.on; pause(); const v = pickVoice(E.S.lang); if (SY && v) { const u = new SpeechSynthesisUtterance(bank(E.S.lang).ui.testLine); u.voice = v; u.lang = v.lang; u.rate = RATE_BASE * E.rate; SY.speak(u); if (was) u.onend = () => go(E.i); } }
  }
  function setRate(r) { E.rate = Math.round(r * 100) / 100; LS.set('ace-rate', String(E.rate)); if (E.on) go(E.i); else paint(true); }
  function onInput(e) {
    const t = e.target.dataset && e.target.dataset.t; if (!t || !E.S) return;
    if (t === 'rate') { const o = e.target.parentNode.querySelector('output'); if (o) o.textContent = (+e.target.value).toFixed(2) + '×'; if (e.type === 'change') setRate(+e.target.value); }
    else if (t === 'voice' && e.type === 'change') { LS.set('ace-voice-' + E.S.lang.slice(0, 2), e.target.value); if (E.on) go(E.i); }
  }
  /* buttons elsewhere on the page that start audio carry data-at-key: show which one is playing */
  let syncT = null;
  function sync() { if (syncT) return; syncT = requestAnimationFrame(() => { syncT = null; const k = E.S && E.on ? E.S.key.replace(/\+x$/, '') : null; document.querySelectorAll('[data-at-key]').forEach(el => { const on = !!k && el.dataset.atKey === k; el.classList.toggle('at-on', on); el.setAttribute('aria-pressed', String(on)); }); }); }
  document.addEventListener('visibilitychange', () => { if (document.hidden) savePos(); });
  window.addEventListener('pagehide', savePos);

  window.AceTeacher = API;
})();
