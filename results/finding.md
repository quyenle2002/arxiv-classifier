Setup

arXiv metadata from Kaggle, randomly sampled 2% → 64,066 papers
Kept 11 classes with at least ~1,000 papers each: cs, math, cond-mat, astro-ph, physics, hep-ph, quant-ph, hep-th, eess, gr-qc, stat
Label = archive of each paper’s first-listed category; input = title + abstract
Split 70/15/15, stratified: 41,787 train, 8,954 validation, 8,955 test (test not used yet)
Features: TF-IDF, 50,000 words, English stop words removed

Results (validation set)
Model	Accuracy	Macro F1
Always guess cs	0.281	0.040
Logistic regression	0.844	0.741
Logistic regression, balanced	0.829	0.763
Strongest classes: astro-ph, math, cs (F1 about 0.89–0.92)
Weakest classes in the original model: eess (0.31), stat (0.51), physics and gr-qc (about 0.67)


Error patterns (original model)

eess → cs: 171 of 245 eess papers predicted as cs, only 52 correct. Its subfields (audio, images, signals, control) overlap with CS subfields, eess.SY and cs.SY are aliases, and eess only started in 2017.
stat → cs: 79 wrong vs. 80 correct. Likely ML papers cross-listed in stat.ML and cs.LG.
physics: errors spread across cond-mat (89), cs (73), and others, since it’s a broad catch-all archive.
From the normalized matrix: gr-qc → hep-th (12% of gr-qc papers), from shared math and vocabulary.
Possible reasoning is due to the shear amout of cs paper model will lean toward it when unsure

Class weighting

Accuracy down 1.5 points, macro F1 up 2.2 points
eess: recall 0.21 → 0.73, precision 0.57 → 0.37, F1 0.31 → 0.49
stat: recall 0.42 → 0.74, precision 0.67 → 0.44, F1 0.51 → 0.55
cs: precision 0.84 → 0.93, recall 0.94 → 0.80. 246 cs papers now predicted as eess, so the confusion flipped direction rather than disappearing.
Takeaways: weighting fixes the model ignoring small classes, but not overlap between fields. Pick the model by goal: balanced for finding all papers of a small field (recall), original for most labels correct overall (accuracy).