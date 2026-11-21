# Self-explanations written by the models

Step-1 prompt: "Explain the meaning of the proverb in one short sentence. Proverb: {proverb} Explanation:"

- ✓ / ✗ = whether the model then picked the right meaning (swap-debiased) when given its own explanation.
- *EN:* = English. Proverb and gold explanation come from the reviewed English test file; mT0 outputs in Kannada/Telugu get a short literal translation (mistakes kept).

# Part 1: Kannada prompts

## 1. ಮನಸಿದ್ದರೆ ಮಾರ್ಗ  (figurative)
*EN: Where there's a will, there's a way*

- **Gold:** ದೃಢವಾದ ಇಚ್ಛಾಶಕ್ತಿ ಇದ್ದರೆ ಯಾವುದೇ ಕಷ್ಟದ ಕೆಲಸಕ್ಕೂ ದಾರಿ ಸಿಗುತ್ತದೆ
  - *EN: If one has strong willpower, a way opens up even for a difficult task.*
- **mT0-large** ✓: a journey where there is no way
- **Qwen3.5-2B** ✓: ಮನಸಿದ್ದರೆ ಮಾರ್ಗ
- **Sarvam-1** ✓: This means that if you have a good mind, then it is easy to find ways to achieve your goals. If you don't have a good mind, then it will be difficult for you to find ways to achieve your goals.

## 2. ಕೈ ಕೆಸರಾದರೆ ಬಾಯಿ ಮೊಸರು  (figurative)
*EN: If the hand gets muddy, the mouth gets curd*

- **Gold:** ಕಷ್ಟಪಟ್ಟು ದುಡಿದರೆ ಮಾತ್ರ ಒಳ್ಳೆಯ ಜೀವನ ಅಥವಾ ಪ್ರತಿಫಲ ಸಿಗುತ್ತದೆ.
  - *EN: Only by working hard does one get a good life or a reward.*
- **mT0-large** ✓: """ఇది మంచి వాయిద్యం."""
  - *EN: [Telugu] "This is a good musical instrument."*
- **Qwen3.5-2B** ✓: ಕೈ ಕೆಸರಾದರೆ ಬಾಯಿ ಮೊಸರು
- **Sarvam-1** ✓: This means that if you are not careful, your mistakes will show up to everyone else and they may make fun of you or even worse. [/INST]

## 3. ಮಾತು ಬೆಳ್ಳಿ, ಮೌನ ಬಂಗಾರ  (figurative)
*EN: Speech is silver, silence is gold*

- **Gold:** ಅನಗತ್ಯವಾಗಿ ಮಾತನಾಡುವುದಕ್ಕಿಂತ ಸಂದರ್ಭಕ್ಕೆ ತಕ್ಕಂತೆ ಮೌನವಾಗಿರುವುದು ಹೆಚ್ಚು ಮೌಲ್ಯಯುತ ಮತ್ತು ಬುದ್ಧಿವಂತಿಕೆಯ ಕೆಲಸ.
  - *EN: Staying silent as the situation demands is more valuable and wiser than speaking unnecessarily.*
- **mT0-large** ✓: ಭಾಷೆ ಬೆಳ್ಳಿ, ಮೌನ ಬಂಗಾರ
  - *EN: Speech is silver, silence is gold*
- **Qwen3.5-2B** ✓: The proverb means that words are more valuable than gold, as silence is considered more precious than money.
- **Sarvam-1** ✓: This means that words are valuable and should be used wisely because they can have a big impact on others. Silence is also important as it shows respect for other people's feelings and opinions. </s>

## 4. ಬೆಳ್ಳಗಿರೋದೆಲ್ಲ ಹಾಲಲ್ಲ, ಹೊಳೆಯೋದೆಲ್ಲ ಚಿನ್ನ ಅಲ್ಲ  (figurative)
*EN: Not everything white is milk, not everything that shines is gold*

- **Gold:** ಹೊರನೋಟಕ್ಕೆ ಆಕರ್ಷಕವಾಗಿ ಅಥವಾ ಶುದ್ಧವಾಗಿ ಕಾಣುವುದೆಲ್ಲವೂ ನಿಜವಾಗಿಯೂ ಒಳ್ಳೆಯದು ಅಥವಾ ಮೌಲ್ಯಯುತವಾದದ್ದು ಆಗಿರುವುದಿಲ್ಲ.
  - *EN: Not everything that looks attractive or pure on the outside is truly good or valuable.*
- **mT0-large** ✗: ಚೆಂಡಿನ ಚೆಂಡು ಚೆಂಡಿನ ಚೆಂಡು ಚೆಂಡಿನ ಚೆಂಡು ಚೆಂಡಿನ ಚೆಂಡು ಚೆಂಡಿನ ಚೆಂಡು ಚೆಂಡಿನ ಚೆಂಡು ಚೆಂಡಿನ ಚೆಂಡು ಚೆಂಡಿನ ಚೆಂಡು ಚೆಂಡಿನ
  - *EN: ball of ball, ball of ball, ball of ball... (repetitive)*
- **Qwen3.5-2B** ✓: ಬೆಳ್ಳಗಿರೋದೆಲ್ಲ ಹಾಲಲ್ಲ, ಹೊಳೆಯೋದೆಲ್ಲ ಚಿನ್ನ ಅಲ್ಲ
- **Sarvam-1** ✓: This means that not everything that looks good or shiny is actually valuable or worthwhile. It's important to look beyond appearances and consider the true value of something before making a decision. </s>

## 5. ಗಿಡವಾಗಿ ಬಗ್ಗದ್ದು, ಮರವಾಗಿ ಬಗ್ಗೀತೇ?  (figurative)
*EN: What doesn't bend as a sapling, will it bend as a tree?*

- **Gold:** ಯಾವುದೇ ವಿಷಯವನ್ನು ಅಥವಾ ಕೆಟ್ಟ ಅಭ್ಯಾಸವನ್ನು ಆರಂಭದಲ್ಲೇ ಅಥವಾ ಚಿಕ್ಕ ವಯಸ್ಸಿನಲ್ಲೇ ತಿದ್ದಿಕೊಳ್ಳಬೇಕು; ವಯಸ್ಸಾದ ಮೇಲೆ ಅಥವಾ ಸಮಯ ಕಳೆದ ನಂತರ ಅದನ್ನು ತಿದ್ದಿಕೊಳ್ಳುವುದು ಅಸಾಧ್ಯ.
  - *EN: Any matter or bad habit should be corrected early, at a young age; once one is older or time has passed, correcting it is impossible.*
- **mT0-large** ✗: ಗಿಡగా బಗ್ಗడం, మರವಾಗಿ బಗ್ಗడం
  - *EN: [Kannada+Telugu mix] Bending as a sapling, bending as a tree*
- **Qwen3.5-2B** ✓: The proverb asks whether a person who is easily angered is truly a tree, implying that a tree does not get angry, whereas a person who is easily angered is like a tree that is cut down.
- **Sarvam-1** ✓: This means that if you don't work hard and try to improve yourself, then you will never get anywhere. It is like a tree - it can grow taller but only by bending downwards towards the ground. If you are not willing to put effort into your life, you won'

## 6. ಆಳಾಗಬಲ್ಲವನು ಅರಸನಾಗಬಲ್ಲ  (figurative)
*EN: One who can be a servant can become a king*

- **Gold:** ಯಾವುದೇ ವ್ಯವಸ್ಥೆಯಲ್ಲಿ ಅಥವಾ ಕೆಲಸದಲ್ಲಿ ಕೆಳಹಂತದ ಕಷ್ಟ-ನಷ್ಟಗಳನ್ನು ಅರಿತು, ಪ್ರಾಮಾಣಿಕವಾಗಿ ಸೇವೆಯನ್ನು ಸಲ್ಲಿಸಿದವನು ಮಾತ್ರ ಭವಿಷ್ಯದಲ್ಲಿ ಉತ್ತಮ ನಾಯಕ ಅಥವಾ ಅಧಿಕಾರಿಯಾಗಲು ಅರ್ಹನಾಗುತ್ತಾನೆ.
  - *EN: In any system or job, only one who understands the hardships and losses at the lower level and has served honestly becomes worthy of being a good leader or officer in the future.*
- **mT0-large** ✓: రాజుగా మారి, రాజుగా మారి
  - *EN: [Telugu] Becoming a king, becoming a king (repetitive)*
- **Qwen3.5-2B** ✓: ಆಳಾಗಬಲ್ಲವನು ಅರಸನಾಗಬಲ್ಲ
- **Sarvam-1** ✓: This means that if you are able to grow and develop, then you can become successful or powerful.

## 7. ತಾಳಿದವನು ಬಾಳಿಯಾನು  (literal)
*EN: One who endures will thrive*

- **Gold:** ಸಂಕಷ್ಟದ ಸಂದರ್ಭಗಳಲ್ಲಿ ಅಥವಾ ಕಷ್ಟದ ಕಾಲದಲ್ಲಿ ತಾಳ್ಮೆ ಮತ್ತು ಸಂಯಮವನ್ನು ಕಾಯ್ದುಕೊಳ್ಳುವವರು ಮಾತ್ರ ಜೀವನದಲ್ಲಿ ಯಶಸ್ಸು ಮತ್ತು ನೆಮ್ಮದಿಯನ್ನು ಕಾಣುತ್ತಾರೆ.
  - *EN: Only those who maintain patience and restraint in difficult situations or hard times find success and peace in life.*
- **mT0-large** ✓: The man who went to the castle
- **Qwen3.5-2B** ✓: ತಾಳಿದವನು ಬಾಳಿಯಾನು
- **Sarvam-1** ✓: This means that if you have been through something difficult, then it is likely to be easier for you in the future. It's like a saying that "you learn from your mistakes". [/INST]

## 8. ಕೋತಿ ಕೈಗೆ ಮಾಣಿಕ್ಯ ಕೊಟ್ಟ ಹಾಗೆ  (figurative)
*EN: Like giving a ruby to a monkey's hand*

- **Gold:** ಯೋಗ್ಯತೆ ಅಥವಾ ಅರ್ಹತೆ ಇಲ್ಲದ ವ್ಯಕ್ತಿಗೆ ಅತ್ಯಮೂಲ್ಯವಾದ ವಸ್ತು, ಅಧಿಕಾರ ಅಥವಾ ಜವಾಬ್ದಾರಿಯನ್ನು ನೀಡಿದಾಗ, ಅವರು ಅದರ ನಿಜವಾದ ಬೆಲೆಯನ್ನು ಅಥವಾ ಉಪಯೋಗವನ್ನು ಅರಿಯದೆ ವ್ಯರ್ಥ ಮಾಡುತ್ತಾರೆ.
  - *EN: When a highly valuable object, authority or responsibility is given to a person without worthiness or qualification, they waste it without knowing its true value or use.*
- **mT0-large** ✓: 'ಕೋತಿ ಕೈಯಲ್ಲಿ ಮಾಣಿಕ್ಯ ಕೊಟ್ಟಂತೆ'
  - *EN: 'Like giving a ruby into a monkey's hand'*
- **Qwen3.5-2B** ✓: ಕೋತಿ ಕೈಗೆ ಮಾಣಿಕ್ಯ ಕೊಟ್ಟ ಹಾಗೆ
- **Sarvam-1** ✓: This means that if you give someone something they will take it away from you, or use it to their advantage.

## 9. ವೇದ ಸುಳ್ಳಾದರು ಗಾದೆ ಸುಳ್ಳಾಗದು  (literal)
*EN: Even if the Veda proves false, the proverb will not*

- **Gold:** ದೀರ್ಘಕಾಲದ ಮಾನವ ಅನುಭವ ಮತ್ತು ಸತ್ಯದ ಆಧಾರದ ಮೇಲೆ ಹುಟ್ಟಿಕೊಂಡ ಗಾದೆ ಮಾತುಗಳು ಎಂದೆಂದಿಗೂ ಮತ್ತು ಯಾವುದೇ ಕಾಲಕ್ಕೂ ಸುಳ್ಳಾಗುವುದಿಲ್ಲ, ಅವು ಸದಾ ಸತ್ಯ.
  - *EN: Proverbs born from long human experience and truth never become false in any age; they are always true.*
- **mT0-large** ✓: ವೇದ ಸುಳ್ಳగా ఉండేది.
  - *EN: [Kannada+Telugu mix] The Veda used to be a lie.*
- **Qwen3.5-2B** ✗: ವೇದ ಸುಳ್ಳಾದರು ಗಾದೆ ಸುಳ್ಾಗದು
- **Sarvam-1** ✓: This means that if you lie, eventually people will find out and it won't be good for you.

## 10. ಹಾಸಿಗೆ ಇದ್ದಷ್ಟು ಕಾಲು ಚಾಚು  (figurative)
*EN: Stretch your legs only as far as the bed allows*

- **Gold:** ನಮ್ಮ ಬಳಿ ಇರುವ ಆದಾಯ, ಸಂಪತ್ತು ಅಥವಾ ಸಾಮರ್ಥ್ಯಕ್ಕೆ ತಕ್ಕಂತೆ ಮಾತ್ರ ಖರ್ಚು ಮಾಡಬೇಕು ಅಥವಾ ಆಸೆಗಳನ್ನು ಇಟ್ಟುಕೊಳ್ಳಬೇಕು.
  - *EN: One should spend, or hold desires, only in line with one's income, wealth or capacity.*
- **mT0-large** ✓: ಹಾಸಿಗೆ ಇದ್ದಷ್ಟು ಕಾಲು ಚಾಚು
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಹಾಸಿಗೆ ಇದ್ದಷ್ಟು ಕಾಲು ಚಾಚು
- **Sarvam-1** ✓: This means that if you have something, then you can do more with it than someone who doesn't have anything at all. It is a way to say that having resources or opportunities makes life easier and better for you. </s>

## 11. ಮಾಡಿದುಣ್ಣೋ ಮಹರಾಯ  (literal)
*EN: Eat what you have made, O lord (you reap what you sow)*

- **Gold:** ಮನುಷ್ಯ ತಾನು ಮಾಡಿದ ಕೆಲಸ, ಕರ್ಮ ಅಥವಾ ಪ್ರಯತ್ನಕ್ಕೆ ತಕ್ಕಂತೆ ಒಳ್ಳೆಯ ಅಥವಾ ಕೆಟ್ಟ ಫಲಿತಾಂಶವನ್ನು ತಾನೇ ಅನುಭವಿಸಬೇಕಾಗುತ್ತದೆ.
  - *EN: A person has to experience for himself the good or bad result of the work, deeds or effort he has done.*
- **mT0-large** ✓: ನಿಮ್ಮ ಮಗನು ಮಾಡಬೇಕಾದ ವಸ್ತುವು ಯಾವುವು?
  - *EN: What are the things your son should do?*
- **Qwen3.5-2B** ✓: The proverb "ಮಾದಿದುಣ್ಣೋ ಮಹರಾಯ" (Madidunno Maharaja) is a humorous and satirical reference to the **fear of the law** or the **fear of punishment**, often used to describe a situation where someone is so terrified
- **Sarvam-1** ✓: This means that if you do something once, it is easy to repeat it again and again. It's like a habit. [/INST]

## 12. ಅತಿ ಆಸೆ ಗತಿ ಕೇಡು  (literal)
*EN: Excessive desire leads to a bad end*

- **Gold:** ಅತಿಯಾದ ಆಸೆ ಅಥವಾ ಲೋಭವು ಎಂದಿಗೂ ಒಳ್ಳೆಯದಲ್ಲ, ಅದು ಮನುಷ್ಯನನ್ನು ವಿನಾಶದತ್ತ ಕೊಂಡೊಯ್ಯುತ್ತದೆ.
  - *EN: Excessive desire or greed is never good; it leads a person to destruction.*
- **mT0-large** ✓: A very angry man is a very angry man.
- **Qwen3.5-2B** ✓: ಅತಿ ಆಸೆ ಗತಿ ಕೇಡು
- **Sarvam-1** ✓: This means that if you want something badly enough, it can be very dangerous to get it. It is better not to have what you really want than to risk getting it and losing everything else.

## 13. ನಾಯಿ ಬಾಲ ಡೊಂಕು  (figurative)
*EN: A dog's tail is crooked*

- **Gold:** ಕೆಲವು ವ್ಯಕ್ತಿಗಳ ಮೂಲ ಸ್ವಭಾವ ಅಥವಾ ಕೆಟ್ಟ ಚಾಳಿಗಳು ಎಷ್ಟೇ ಪ್ರಯತ್ನಿಸಿದರೂ ಎಂದಿಗೂ ಬದಲಾಗುವುದಿಲ್ಲ.
  - *EN: The basic nature or bad habits of some people never change no matter how much one tries.*
- **mT0-large** ✗: ಡೊಂಕು ಡೊಂಕು
  - *EN: Crooked crooked*
- **Qwen3.5-2B** ✓: ನಾಯಿ ಬಾಲ ಡೊಂಕು
- **Sarvam-1** ✓: This means that if you are not careful, your actions will have consequences. The dog's tail is a metaphor for something small and insignificant, but it can still cause harm or damage.

## 14. ಒಂದು ಕಣ್ಣೀಗೆ ಬೆಣ್ಣೆ ಮತ್ತೊಂದು ಕಣ್ಣಿಗೆ ಸುಣ್ಣ  (figurative)
*EN: Butter for one eye, lime for the other eye*

- **Gold:** ಯಾವುದೇ ವ್ಯಕ್ತಿ ಅಥವಾ ಸಂಸ್ಥೆಯು ಜನರ ನಡುವೆ ಪಕ್ಷಪಾತ ಅಥವಾ ತಾರತಮ್ಯ ತೋರುವುದು ಸರಿಯಲ್ಲ.
  - *EN: It is not right for any person or organization to show partiality or discrimination among people.*
- **mT0-large** ✗: 'ಬೆಣ್ಣೆ ಮತ್ತು ಸುಣ್ಣ'
  - *EN: 'Butter and lime'*
- **Qwen3.5-2B** ✗: ಒಂದು ಕಣ್ಣೀಗೆ ಬೆಣ್ಣೆ ಮತ್ತೊಂದು ಕಣ್ಣಿಗೆ ಸುಣ್ಣ
- **Sarvam-1** ✗: ಈ proverb ನ ಅರ್ಥ ಏನಂದ್ರೆ, ಒಬ್ಬರಿಗೆ ತೊಂದರೆ ಕೊಡೋದು ಅಂದ್ರೆ ಬೇರೆಯವರಿಗೆ ತೊಂದರೆ ಕೊಡುತ್ತೆ ಅಂತ.

## 15. ಹುಟ್ಟು ಗುಣ ಸುಟ್ಟರು ಹೋಗಲ್ಲ  (figurative)
*EN: Inborn nature doesn't go even if burned*

- **Gold:** ಹುಟ್ಟಿನಿಂದ ಬಂದ ಗುಣ ಅಥವಾ ಚಾಳಿಗಳು ಮನುಷ್ಯನ ಜೀವನದ ಕೊನೆಯವರೆಗೂ ಬದಲಾಗುವುದಿಲ್ಲ.
  - *EN: Qualities or habits that come from birth do not change until the end of a person's life.*
- **mT0-large** ✓: They don't go to sleep
- **Qwen3.5-2B** ✓: ಹುಟ್ಟು ಗುಣ ಸುಟ್ಟರು ಹೋಗಲ್ಲ
- **Sarvam-1** ✓: This means that you can't undo what has already happened, so it is important to learn from your mistakes and try not to repeat them.

## 16. ವಿನಾಶ ಕಾಲಕ್ಕೆ ವಿಪರೀತ ಬುದ್ಧಿ  (figurative)
*EN: At the time of destruction, a perverse mind*

- **Gold:** ಕಷ್ಟದ ಕಾಲ ಅಥವಾ ಕೆಟ್ಟ ಪರಿಸ್ಥಿತಿ ಬಂದಾಗ ಮನುಷ್ಯನ ಬುದ್ಧಿ ಕೆಲಸ ಮಾಡದೆ,ತಪ್ಪಾದ ನಿರ್ಧಾರಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳುತ್ತಾನೆ.
  - *EN: When hard times or a bad situation arrive, a person's mind doesn't work and he makes wrong decisions.*
- **mT0-large** ✗: ವಿನಾಶ కాలానికి ವಿಪರೀತ ಬುದ್ಧಿ
  - *EN: [Kannada+Telugu mix] Perverse intellect at the time of destruction*
- **Qwen3.5-2B** ✓: ವಿನಾಶ ಕಾಲಕ್ಕೆ ವಿಪರೀತ ಬುದ್ಧಿ
- **Sarvam-1** ✓: This means that when you are too clever for your own good, it can be very dangerous. It is a warning to not think so highly of yourself and always consider other people's feelings as well as your own. </s>

## 17. ದೇಶ ಸುತ್ತಿ ನೋಡು, ಕೋಶ ಓದಿ ನೋಡು  (literal)
*EN: Travel the country and see, read the books and see*

- **Gold:** ಜಗತ್ತನ್ನು ಸಂಚರಿಸಿ ಅನುಭವ ಪಡೆಯುವುದರಿಂದ ಮತ್ತು ಉತ್ತಮ ಪುಸ್ತಕಗಳನ್ನು ಓದುವುದರಿಂದ ಮನುಷ್ಯನಿಗೆ ಪರಿಪೂರ್ಣ ಜ್ಞಾನ ಲಭಿಸುತ್ತದೆ.
  - *EN: By travelling the world to gain experience and by reading good books, a person gains complete knowledge.*
- **mT0-large** ✓: ಜಗತ್ತಿನಾದ್ಯಂತ ಸುತ್ತಿ ನೋಡು, ಕೋಶ ಓದಿ ನೋಡು
  - *EN: Travel around the whole world and see, read the treasury (of books) and see*
- **Qwen3.5-2B** ✓: The proverb means that one should observe the country from the outside while reading the constitution from the inside.
- **Sarvam-1** ✓: This means that you should not rely on just one source or piece of information to make a decision. You need to look at multiple sources and consider all sides before making a decision. </s>

## 18. ಬೀದಿಯಲ್ಲಿ ಹೋಗುವ ಮಾರಿಯನ್ನು ಮನೆಗೆ ಕರೆದಂಗೆ  (figurative)
*EN: Like inviting into your house the calamity (Mari) passing by on the street*

- **Gold:** ಯಾವುದೇ ಸಂಬಂಧವಿಲ್ಲದ ತೊಂದರೆ ಅಥವಾ ಅಪಾಯವನ್ನು ಬೇಕೆಂದೇ ತನ್ನ ಬುಡಕ್ಕೆ ತಂದುಕೊಳ್ಳುವುದು ಎಂದು ಈ ಗಾದೆಯ ಅರ್ಥ.
  - *EN: Deliberately bringing upon oneself a trouble or danger that has nothing to do with one.*
- **mT0-large** ✗: ಮಾರಿಯನ್ನು ಮನೆಯೊಳಗೆ ಕರೆದಂಗೆ
  - *EN: Like inviting the plague-goddess (Maari) into the house*
- **Qwen3.5-2B** ✓: ಬೀದಿಯಲ್ಲಿ ಹೋಗುವ ಮಾರಿಯನ್ನು ಮನೆಗೆ ಕರೆದಂಗೆ
- **Sarvam-1** ✓: This means that if you are going to do something, then it is better to start doing it now than later. It's like saying "Don't wait until tomorrow" or "Do it today". [/INST]

## 19. ಉಪ್ಪು ತಿಂದ ಮೇಲೆ ನೀರು ಕುಡಿಯಲೇಬೇಕು  (literal)
*EN: After eating salt, one must drink water*

- **Gold:** ತಪ್ಪು ಅಥವಾ ಅನುಚಿತ ಕೆಲಸ ಮಾಡಿದವನು ಅದರ ಪರಿಣಾಮವನ್ನು ಎದುರಿಸಲೇಬೇಕು ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: One who has done a wrong or improper act must face its consequences.*
- **mT0-large** ✓: ನೀರು ತೋಡಿದ ಮೇಲೆ ಉಪ್ಪನ್ನು ತೆಂಗಿನಕಾಯಿಯಿಂದ ತೆಂಗಿನಕಾಯಿಯಿಂದ ತೆಂಗಿನಕಾಯಿಯಿಂದ ತೆಂಗಿನಕಾಯಿಯಿಂದ ತೆಂಗಿನಕಾಯಿಯಿಂದ ತೆಂಗಿನಕಾಯಿಯಿಂದ ತೆಂಗಿನಕಾಯಿಯಿಂದ ತೆಂಗಿನಕಾಯಿಯಿಂದ ತೆ
  - *EN: After digging water, salt with coconut with coconut with coconut... (repetitive, nonsensical)*
- **Qwen3.5-2B** ✓: ಉಪ್ಪು ತಿಂದ ಮೇಲೆ ನೀರು ಕುಡಿಯಲೇಬೇಕು
- **Sarvam-1** ✓: This means that you should not be too hasty to do something, because it might have bad consequences later on. It is like saying "you can't put out a fire with water". You need to wait until the situation has cooled down before taking action. </s>

## 20. ಯಾರದೋ ದುಡ್ಡಿನಲ್ಲಿ ಎಲ್ಲಮ್ಮನ ಜಾತ್ರೆ  (figurative)
*EN: Yellamma's fair on someone else's money*

- **Gold:** ಬೇರೆಯವರ ಹಣದಲ್ಲಿ ಯಾವುದೇ ಲೆಕ್ಕವಿಲ್ಲದೆ ಧಾರಾಳವಾಗಿ ಖರ್ಚು ಮಾಡಿ ಮೋಜು ಮಾಡುವುದು ಎಂದು ಈ ಗಾದೆಯ ಅರ್ಥ.
  - *EN: Spending lavishly and making merry with others' money without any accounting.*
- **mT0-large** ✗: All the houses are in a suburb of a city
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that if you spend money on something, it will be worthwhile because someone else has to pay for it. It is a way of saying that when we spend our own money, we should do so with care and consideration. If we waste or squander our money, then others have

## 21. ಆಗುವುದೆಲ್ಲ ಒಳ್ಳೆಯದಕ್ಕೆ  (literal)
*EN: Everything that happens is for the good*

- **Gold:** ಜೀವನದಲ್ಲಿ ನಡೆಯುವ ಯಾವ ಘಟನೆಯೂ ಕೊನೆಗೆ ಒಳ್ಳೆಯದಕ್ಕೇ ಆಗುತ್ತದೆ ಎಂಬ ಭರವಸೆಯನ್ನು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb expresses the assurance that whatever happens in life ultimately turns out for the good.*
- **mT0-large** ✓: Everything is good.
- **Qwen3.5-2B** ✓: ಆಗುವುದೆಲ್ಲ ಒಳ್ಳೆಯದಕ್ಕೆ (All that comes is good)
- **Sarvam-1** ✓: This means that everything happens for a reason and it is important to accept things as they are, rather than trying to change them or fight against them.

## 22. ಕಾಲಕ್ಕೆ ತಕ್ಕಂತೆ ನಡಿಬೇಕು, ತಾಳಕ್ಕೆ ತಕ್ಕಂತೆ ಕುಣಿಯಬೇಕು  (literal)
*EN: Walk according to the times, dance according to the beat*

- **Gold:** ಬದಲಾಗುವ ಕಾಲ ಮತ್ತು ಸಂದರ್ಭಗಳಿಗೆ ಹೊಂದಿಕೊಂಡು ನಡೆದುಕೊಳ್ಳಬೇಕು ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: One should adapt oneself to changing times and circumstances.*
- **mT0-large** ✓: ತಕ್ಕಂತೆ ನಡಿಬೇಕು, ತಾಳಕ್ಕೆ ತಕ್ಕಂತೆ ಕುಣಿಯಬೇಕು
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: ಕಾಲಕ್ಕೆ ತಕ್ಕಂತೆ ನಡಿಬೇಕು, ತಾಳಕ್ಕೆ ತಕ್ಕಂತೆ ಕುಣಿಯಬೇಕು ಎಂದರೆ, ವ್ಯಕ್ತಿಯ ನಡುವಿನ ಸಂಬಂಧಗಳು ಮತ್ತು ಕುಟುಂಬದ ಸಂಬಂಧ
- **Sarvam-1** ✓: This means that you should always be prepared for what is to come and not just go with the flow. It's important to stay on track and not get sidetracked by things that may happen unexpectedly. </s>

## 23. ಅನ್ನ ಹಾಕಿದ ಮನೆಗೆ ಕನ್ನ ಹಾಕಬೇಡ  (figurative)
*EN: Don't burgle the house that fed you*

- **Gold:** ತನ್ನ ಅಣ್ಣ ಕಷ್ಟಪಟ್ಟು ಕಟ್ಟಿದ ಮನೆ ಅಥವಾ ಆಸ್ತಿಯ ಮೇಲೆ ದುರಾಸೆಯಿಂದ ಕಣ್ಣು ಹಾಕಬಾರದು ಎಂಬ ಎಚ್ಚರಿಕೆ ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: A warning that one shouldn't greedily eye the house or property one's elder brother built with hardship.*
- **mT0-large** ✓: ನಿಮ್ಮ ಮನೆಯಲ್ಲಿ ಆಹಾರ ಹಾಕುವವರಾದರೆ, ಆಹಾರವನ್ನು ನಿಮ್ಮ ಮನೆಯಲ್ಲಿ ತೋಡಿದ ಹೊಟ್ಟೆ ತುಂಬಿಸಿಕೊಳ್ಳಿ.
  - *EN: If you are the ones who serve food in your house, fill the stomach you dug with food in your house. (nonsensical)*
- **Qwen3.5-2B** ✓: ಅನ್ನ ಹಾಕಿದ ಮನೆಗೆ ಕನ್ನ ಹಾಕಬೇಡ
- **Sarvam-1** ✓: This means that you shouldn't put a burden on someone else, because it will only make them feel worse. It is better to help others when they need it rather than making things harder for them.

## 24. ಮಾರಿ ಕಣ್ಣು ಹೋರಿ ಮೇಲೆ, ಕಟಕನ ಕಣ್ಣು ಕುರಿ ಮೇಲೆ  (figurative)
*EN: Mari's eye is on the bull, the butcher's eye is on the sheep*

- **Gold:** ಪ್ರತಿಯೊಬ್ಬ ದುರಾಸೆಯ ವ್ಯಕ್ತಿಯೂ ತನ್ನ ಲಾಭ ಯಾವುದರಲ್ಲಿದೆಯೋ ಅದರ ಮೇಲೆಯೇ ಕಣ್ಣಿಡುತ್ತಾನೆ ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: Every greedy person keeps his eye on whatever benefits him.*
- **mT0-large** ✓: ಕಟಕನ ಕಣ್ಣು ಕುರಿ ಮೇಲೆ
  - *EN: The butcher's eye is on the sheep*
- **Qwen3.5-2B** ✓: ಮಾರಿ ಕಣ್ಣು ಹೋರಿ ಮೇಲೆ, ಕಟಕನ ಕಣ್ಣು ಕುರಿ ಮೇಲೆ
- **Sarvam-1** ✓: This means that you should not look at what is wrong with someone else but instead focus on your own problems and issues.

## 25. ಪಾಲಿಗೆ ಬಂದದ್ದು ಪರಮಾನ್ನ  (figurative)
*EN: What comes to one's lot is paramanna (sweet rice pudding)*

- **Gold:** ತನ್ನ ಪಾಲಿಗೆ ಬಂದದ್ದು ಏನೇ ಇರಲಿ ಅದನ್ನು ಸಂತೋಷದಿಂದ ಸ್ವೀಕರಿಸಬೇಕು ಎಂಬ ಅರ್ಥ ಇರಬಹುದು (ಪಾಲಿಗೆ ಬಂದದ್ದು ಪರಮಾನ್ನ).
  - *EN: Whatever comes to one's share, one should accept it happily (what comes to one's lot is paramanna).*
- **mT0-large** ✓: 'இந்த ಕಾಯಿಲೆ எனக்கு புதிது'
  - *EN: [Tamil+Kannada mix] 'This illness is new to me'*
- **Qwen3.5-2B** ✓: ಪಾಲಿಗೆ ಬಂದದ್ದು ಪರಮಾನ್ನ
- **Sarvam-1** ✓: This means that if you get something good, it is better to use it than keep it for yourself. It's like a saying about getting something valuable and using it instead of keeping it for yourself.

## 26. ಸಾವಿರ ಸುಳ್ಳು ಹೇಳಿ ಒಂದು ಮದುವೆ ಮಾಡು  (figurative)
*EN: Tell a thousand lies and perform one wedding*

- **Gold:** ಒಳ್ಳೆಯ ಉದ್ದೇಶದ ಕೆಲಸವಾದ ಮದುವೆ ನೆರವೇರಿಸಲು ಸ್ವಲ್ಪ ಉತ್ಪ್ರೇಕ್ಷೆ ಅಥವಾ ಸುಳ್ಳು ಹೇಳಿದರೂ ತಪ್ಪಿಲ್ಲ ಎಂಬ ಮಾತು.
  - *EN: A saying that a little exaggeration or even a lie is no sin if it brings about a wedding, which is a good-intentioned act.*
- **mT0-large** ✓: ಸಾವಿರ ಸುಳ್ಳು ಹೇಳುತ್ತಾ ಒಂದು ಮದುವೆ ಮಾಡು
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಸಾವಿರ ಸುಳ್ಳು ಹೇಳಿ ಒಂದು ಮದುವೆ ಮಾಡು
- **Sarvam-1** ✓: This means that it is better to be honest than to try and deceive someone into believing you are something you're not. [/INST]

## 27. ಕಳ್ಳನನ್ನು ನಂಬಿದರೂ ಕುಳ್ಳನನ್ನು ನಂಬಬೇಡ  (figurative)
*EN: Even if you trust a thief, don't trust a short man*

- **Gold:** ಚಾಣಾಕ್ಷ ಮತ್ತು ಕುತಂತ್ರಿ ವ್ಯಕ್ತಿಯನ್ನು ನಂಬಬಾರದು ಎಂಬ ಎಚ್ಚರಿಕೆ; ಇದು ಕುಳ್ಳರ ಬಗ್ಗೆ ಇರುವ ಹಳೆಯ ರೂಢಿಗತ ಪೂರ್ವಾಗ್ರಹದ ಮಾತೂ ಹೌದು.
  - *EN: A warning not to trust a shrewd and scheming person; it is also an old, conventional prejudice against short people.*
- **mT0-large** ✓: When you believe a devil, you should not believe a devil.
- **Qwen3.5-2B** ✓: ಕಳ್ಳನನ್ನು ನಂಬಿದರೂ ಕುಳ್ಳನನ್ನು ನಂಬಬೇಡ (If you believe a thief, do not believe a thief)
- **Sarvam-1** ✓: This means that you should not trust someone who is trying to cheat or deceive you, because they might be very small and weak compared to you.

## 28. ನೆಲಕ್ಕೆ ಬಿದ್ದರೂ ಮೀಸೆ ಮಣ್ಣಾಗಿಲ್ಲ  (figurative)
*EN: Though he fell to the ground, his moustache didn't get dirty*

- **Gold:** ಸೋತರೂ ಅಥವಾ ಅವಮಾನವಾದರೂ ತನ್ನ ಸೋಲನ್ನು ಒಪ್ಪಿಕೊಳ್ಳದೆ ಜಂಭ ತೋರಿಸುವುದು ಎಂದು ಈ ಗಾದೆಯ ಅರ್ಥ.
  - *EN: Not admitting one's defeat and showing off even after losing or being humiliated.*
- **mT0-large** ✗: """ఆమె కూడా కిందకు రావడానికి ప్రయత్నించింది."""
  - *EN: [Telugu] "She also tried to come down."*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✗: This means that even if you are not successful or have failed, it does not mean that your efforts were wasted. You can still learn from them and move on to try again.

## 29. ಯಾವ ಹುತ್ತದಲ್ಲಿ ಯಾವ ಹಾವಿರುತ್ತೋ  (figurative)
*EN: Which snake is in which anthill*

- **Gold:** ಒಬ್ಬರ ಹೊರನೋಟದಿಂದ ಅವರ ಒಳಗಿನ ಸ್ವಭಾವ ಅಥವಾ ಅಡಗಿರುವ ಅಪಾಯ ತಿಳಿಯುವುದಿಲ್ಲ; ಯಾರಲ್ಲಿ ಏನು ಅಡಗಿದೆಯೋ ಹೇಳಲಾಗದು ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: One cannot know a person's inner nature or hidden danger from outward appearance; one can't say what is hidden in whom.*
- **mT0-large** ✓: ಯಾವ ಹುತ್ತದಲ್ಲಿ ಯಾವ ಹಾವಿರುತ್ತೋ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: The proverb means that wherever there is a snake, there is a snake, and wherever there is a tiger, there is a tiger.
- **Sarvam-1** ✓: The proverb means that you can't judge a book by its cover, or to say it another way, don't make assumptions about something based on what you see at first glance. [/INST]

## 30. ದೇವರಿಗೆ ಒಲಿದರೂ ಪೂಜಾರಿ ಒಲಿಯಲ್ಲ  (figurative)
*EN: Even if the god is pleased, the priest isn't*

- **Gold:** ಮೇಲಿನ ಅಧಿಕಾರಿ ಅಥವಾ ದೇವರೇ ಒಪ್ಪಿದರೂ ನಡುವೆ ಇರುವ ಮಧ್ಯವರ್ತಿ ಅಥವಾ ಕೆಳಗಿನವನು ಅಡ್ಡಿ ಮಾಡುತ್ತಾನೆ ಎಂಬ ಅರ್ಥ.
  - *EN: Even if the higher authority or the god himself agrees, the intermediary or subordinate in between creates obstacles.*
- **mT0-large** ✓: 'దేవుడికి ಒలిచిన వారు కూడా 'పోరాడే'
  - *EN: [Telugu+Kannada mix] 'Even those who peeled(?) for God 'fight'' (broken)*
- **Qwen3.5-2B** ✗: ದೇವರಿಗೆ ಒಲಿದರೂ ಪೂಜಾರಿ ಒಲಿಯಲ್ಲ
- **Sarvam-1** ✗: This means that even if you have something valuable, it is not guaranteed to be yours. It can also mean that no matter how much effort or sacrifice you put into something, there are still things beyond your control.

## 31. ನಮ್ಮ ದೇವರ ಸತ್ಯ ನಮಗೆ ಗೊತ್ತು  (figurative)
*EN: We know the truth of our own god*

- **Gold:** ತಮ್ಮದೇ ಮನೆ ಅಥವಾ ತಮ್ಮದೇ ವಿಷಯದ ಒಳಗಿನ ಸತ್ಯ ತಮಗೇ ಚೆನ್ನಾಗಿ ತಿಳಿದಿರುತ್ತದೆ, ಹೊರಗಿನವರ ಮಾತು ಬೇಕಿಲ್ಲ ಎಂಬ ಅರ್ಥ ಇರಬಹುದು.
  - *EN: The meaning may be that people know the inner truth of their own house or matter well enough themselves and have no need of outsiders' talk.*
- **mT0-large** ✗: Our God is known to us.
- **Qwen3.5-2B** ✗: ನಮ್ಮ ದೇವರ ಸತ್ಯ ನಮಗೆ ಗೊತ್ತು (Our Lord's Truth is Known to Us)
- **Sarvam-1** ✓: The proverb means that we know what is right and wrong, even if others don't.

## 32. ಹಾಗಲಕಾಯಿಗೆ ಬೇವಿನಕಾಯಿ ಸಾಕ್ಷಿ  (figurative)
*EN: For the bitter gourd, the neem fruit is the witness*

- **Gold:** ಮಾತಿನ ಪದಗಳು ಸ್ಪಷ್ಟವಿಲ್ಲ; ಒಂದು ಸಂಶಯಾಸ್ಪದ ವಿಷಯಕ್ಕೆ ಅಷ್ಟೇ ಸಂಶಯಾಸ್ಪದ ಇನ್ನೊಬ್ಬನ ಸಾಕ್ಷಿ ಎಂಬ ಅರ್ಥ ಇರಬಹುದು.
  - *EN: The wording is unclear; it may mean that one dubious matter is backed by an equally dubious witness.*
- **mT0-large** ✗: సన్నని కాయలు, సన్నని కాయలు, సన్నని కాయలు, సన్నని కాయలు, సన్నని కాయలు, సన్నని కాయలు, సన్నని కాయలు, సన్నని కాయలు, సన్నని
  - *EN: [Telugu] Thin pods, thin pods, thin pods... (repetitive)*
- **Qwen3.5-2B** ✓: ಹಾಗಲಕಾಯಿಗೆ ಬೇವಿನಕಾಯಿ ಸಾಕ್ಷಿ
- **Sarvam-1** ✗: This means that if you want to get something done, then it is important to have a good plan and follow through with your actions. If you don't do this, then you will not achieve what you set out to do.

## 33. ಕೈಗೆ ಬಂದ ತುತ್ತು ಬಾಯಿಗೆ ಬರಲಿಲ್ಲ  (figurative)
*EN: The morsel that came to the hand didn't reach the mouth*

- **Gold:** ಇನ್ನೇನು ಕೈಗೆ ಸಿಕ್ಕಿತು ಎನ್ನುವಾಗಲೇ ಕೊನೆಯ ಕ್ಷಣದಲ್ಲಿ ಅವಕಾಶ ಅಥವಾ ಲಾಭ ಕೈತಪ್ಪಿ ಹೋಗುವುದು ಎಂದು ಈ ಗಾದೆಯ ಅರ್ಥ.
  - *EN: An opportunity or gain slips away at the last moment, just as it was about to be obtained.*
- **mT0-large** ✗: The spoon came out of the mouth.
- **Qwen3.5-2B** ✗: ಕೈಗೆ ಬಂದ ತುತ್ತು ಬಾಯಿಗೆ ಬರಲಿಲ್ಲ
- **Sarvam-1** ✗: This means that if you try to get something for free, it will not be worth your time or effort. It is better to pay a little bit more than to waste your time and energy trying to get something for nothing. [/INST]

## 34. ರೋಗಿ ಬಯಸಿದ್ದು ಹಾಲು ಅನ್ನ ವೈದ್ಯ ಹೇಳಿದ್ದು ಹಾಲು ಅನ್ನ  (figurative)
*EN: What the patient wanted was milk-rice; what the doctor prescribed was milk-rice*

- **Gold:** ತಾನು ಬಯಸಿದ್ದನ್ನೇ ಬೇರೆಯವರು ಸಲಹೆ ಅಥವಾ ಆದೇಶವಾಗಿ ಹೇಳಿದಾಗ ಆಗುವ ಅನಿರೀಕ್ಷಿತ, ಸಂತೋಷದ ಹೊಂದಾಣಿಕೆ ಎಂದು ಈ ಗಾದೆಯ ಅರ್ಥ.
  - *EN: The unexpected, happy coincidence when what one wanted is exactly what others say as advice or orders.*
- **mT0-large** ✗: ರೋಗಿ ಬಯಸಿದ್ದು ಹಾಲು ಅನ್ನ ವೈದ್ಯ ಹೇಳಿದ್ದು ಹಾಲು
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: Here is the explanation in one short sentence:
- **Sarvam-1** ✗: This means that sometimes what you want is not always what you need, and it's better to listen to others than to be stubborn about your own desires. </s>

## 35. ಕಳ್ಳನಿಗೊಂದು ಪಿಳ್ಳೆ ನೆವ  (figurative)
*EN: A thief always has a petty excuse*

- **Gold:** ತಪ್ಪು ಮಾಡಿದವನು ಯಾವಾಗಲೂ ತಪ್ಪಿಸಿಕೊಳ್ಳಲು ಒಂದಲ್ಲ ಒಂದು ಸಣ್ಣ ನೆಪ ಹುಡುಕಿಕೊಂಡಿರುತ್ತಾನೆ ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: One who has done wrong always finds some small excuse to escape.*
- **mT0-large** ✗: ನೆವ - ನೆವ
  - *EN: Excuse - excuse*
- **Qwen3.5-2B** ✓: ಕಳ್ಳನಿಗೊಂದು ಪಿಳ್ಳೆ ನೆವ
- **Sarvam-1** ✓: This means that if you want to get something, it is better to ask for help than try and do everything yourself. It's easier to ask someone else for help when you need it, rather than trying to figure out how to solve a problem on your own.

## 36. ಕುಣಿಯಲಾರದವಳು ನೆಲ ಡೊಂಕು ಅಂದಳಂತೆ  (figurative)
*EN: The woman who couldn't dance said the floor is crooked*

- **Gold:** ತನ್ನ ಅಸಾಮರ್ಥ್ಯ ಅಥವಾ ಕೊರತೆಯನ್ನು ಒಪ್ಪಿಕೊಳ್ಳದೆ ಸಲಕರಣೆ ಅಥವಾ ಪರಿಸ್ಥಿತಿಯನ್ನು ದೂಷಿಸುವುದು ಎಂದು ಈ ಗಾದೆಯ ಅರ್ಥ.
  - *EN: Blaming equipment or circumstances instead of accepting one's own incompetence or shortcoming.*
- **mT0-large** ✗: ಡೊಂಕು ಬಿದ್ದ ಜಾಗವನ್ನು ಡೊಂಕು ಎಂದು ತಾಯಿ ತಿಳಿಸಿದ್ದಾಳೆ.
  - *EN: Mother has informed that the place where the crookedness fell is crooked. (nonsensical)*
- **Qwen3.5-2B** ✓: ಕುಣಿಯಲಾರದವಳು ನೆಲ ಡೊಂಕು ಅಂದಳಂತೆ
- **Sarvam-1** ✓: This means that if you can't do something, it is like saying "I am not good at this". It is a way to say that someone who cannot do something has no right to complain about it.

## 37. ಹೋದ ಪುಟ್ಟ ಬಂದ ಪುಟ್ಟ  (figurative)
*EN: Putta went, Putta came back.*

- **Gold:** ಯಾವುದೇ ಲಾಭವಿಲ್ಲದೆ, ಹೋದ ಹಾಗೆಯೇ ಬರಿಗೈಯಲ್ಲಿ ವ್ಯರ್ಥವಾಗಿ ಹಿಂತಿರುಗುವುದು ಎಂದು ಈ ಗಾದೆಯ ಅರ್ಥ.
  - *EN: Returning in vain, empty-handed just as one went, without any gain.*
- **mT0-large** ✗: The boy came back.
- **Qwen3.5-2B** ✓: ಹೋದ ಪುಟ್ಟ ಬಂದ ಪುಟ್ಟ
- **Sarvam-1** ✗: This means that small things can have a big impact on us, and we should not underestimate them.

## 38. ಶಿವಪೂಜೆಯಲ್ಲಿ ಕರಡಿ ಬಿಟ್ಟಂಗೆ  (figurative)
*EN: Like letting a bear loose during Shiva worship*

- **Gold:** ಪವಿತ್ರ ಅಥವಾ ಶಿಸ್ತಿನ ಕಾರ್ಯಕ್ರಮದ ನಡುವೆ ಅಸಂಬದ್ಧ ಗೊಂದಲ ಉಂಟುಮಾಡುವವರ ಬಗ್ಗೆ ಹೇಳುವ ಮಾತು.
  - *EN: A saying about people who cause absurd disruption in the middle of a sacred or orderly event.*
- **mT0-large** ✓: ಕರಡಿ ಬಿಟ್ಟಂಗೆ
  - *EN: Like a bear letting go*
- **Qwen3.5-2B** ✓: The meaning of the proverb is:
- **Sarvam-1** ✓: This means that if you are too eager to please someone, then they will take advantage of your kindness and do whatever they want without considering what is right or wrong.

## 39. ಕುಂಬಳಕಾಯಿ ಕಳ್ಳ ಅಂದರೆ ಹೆಗಲು ಮುಟ್ಟಿ ನೋಡಿಕೊಂಡ  (figurative)
*EN: Say 'pumpkin thief' and he felt his own shoulder*

- **Gold:** ತಪ್ಪು ಮಾಡಿದವನು ಬೇರೆಯವರ ಸಾಮಾನ್ಯ ಮಾತನ್ನೂ ತನ್ನ ಬಗ್ಗೆಯೇ ಎಂದು ಭಾವಿಸಿ ತನ್ನ ಅಪರಾಧವನ್ನು ತಾನೇ ಬಯಲು ಮಾಡಿಕೊಳ್ಳುವುದು.
  - *EN: A guilty person takes others' ordinary words as being about himself and gives away his own crime.*
- **mT0-large** ✗: ಚೆಂಡಿನ ಚೆಂಡು
  - *EN: ball of ball*
- **Qwen3.5-2B** ✗: ಕುಂಬಳಕಾಯಿ ಕಳ್ಳ ಅಂದರೆ ಹೆಗಲು ಮುಟ್ಟಿ ನೋಡಿಕೊಂಡ
- **Sarvam-1** ✓: This means that if you are trying to get something from someone, but they don't want it or can't give it to you, then you should try not to bother them too much about it. You shouldn't make a big fuss over it because they might just say no

## 40. ಮಲ್ಲಿ ಮಲ್ಲಿ ಮಂಚಕ್ಕೆ ಎಷ್ಟು ಕಾಲೂ ಅಂದರೆ ಮೂರು ಮತ್ತೊಂದು ಅಂದ್ಲಂತೆ  (figurative)
*EN: 'Malli, Malli, how many legs does the cot have?' 'Three and one more,' she said*

- **Gold:** ಸರಳವಾದ ಪ್ರಶ್ನೆಗೆ ಸುತ್ತಿ ಬಳಸಿ, ಅನಗತ್ಯವಾಗಿ ತಿರುಗಿಸಿ ಉತ್ತರ ಕೊಡುವುದು ಅಥವಾ ಸ್ಪಷ್ಟವಾದುದನ್ನೇ ಬೇರೆ ರೀತಿ ಹೇಳುವುದು.
  - *EN: Giving a roundabout, needlessly twisted answer to a simple question, or saying something obvious in another way.*
- **mT0-large** ✓: """ఇది కూడా చదవండి."""
  - *EN: [Telugu] "Also read this." (web boilerplate)*
- **Qwen3.5-2B** ✓: ಮಲ್ಲಿ ಮಲ್ಲಿ ಮಂಚಕ್ಕೆ ಎಷ್ಟು ಕಾಲೂ ಅಂದರೆ ಮೂರು ಮತ್ತೊಂದು ಅಂದ್ಲಂತೆ
- **Sarvam-1** ✓: This means that if you have a lot of things to do, it is better to divide them into smaller tasks and then complete each task than trying to do everything at once.

## 41. ಕಳ್ಳನ ಮನಸ್ಸು ಹುಳ್ಳು ಹುಳ್ಳಗೆ  (figurative)
*EN: A thief's mind is jittery*

- **Gold:** ತಪ್ಪು ಮಾಡಿದವನ ಮನಸ್ಸು ಸದಾ ಭಯ ಮತ್ತು ಸಂಶಯದಿಂದ ಕೂಡಿ ಸಣ್ಣ ಸದ್ದಿಗೂ ಬೆಚ್ಚುತ್ತದೆ ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb says a wrongdoer's mind is always full of fear and suspicion and startles at the slightest sound.*
- **mT0-large** ✗: a sheep's mind is a sheep's
- **Qwen3.5-2B** ✓: ಕಳ್ಳನ ಮನಸ್ಸು ಹುಳ್ಳು ಹುಳ್ಳಗೆ
- **Sarvam-1** ✓: This means that a person who is always thinking about stealing will never be able to get away with it, because they are constantly being watched and followed by someone or something. It's like trying to hide your tracks when you know you shouldn't be doing something wrong. [/INST]

## 42. ಬೀಸೋ ದೊಣ್ಣೆ ತಪ್ಪಿದರೆ ನೂರು ವರ್ಷ ಆಯುಷ್ಯ  (figurative)
*EN: If the swinging club misses, a hundred years of life*

- **Gold:** ಮೈಮೇಲೆ ಬರಬೇಕಿದ್ದ ದೊಡ್ಡ ಅಪಾಯ ಕೂದಲೆಳೆಯಲ್ಲಿ ತಪ್ಪಿದರೆ ಅದು ಹೊಸ ಜೀವ ಸಿಕ್ಕಂತೆ, ಇನ್ನು ಬಹಳ ಕಾಲ ಬದುಕುತ್ತೇವೆ ಎಂಬ ಸಮಾಧಾನದ ಮಾತು.
  - *EN: If a great danger that was about to strike narrowly misses, it is like getting a new life; a consoling word that one will live long.*
- **mT0-large** ✓: ದೊಣ್ಣೆ ತಪ್ಪಿದರೆ ನೂರು ವರ್ಷ ಆಯಷ್ಯ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: ಬೀಸೋ ದೊಣ್ಣೆ ತಪ್ಪಿದರೆ ನೂರು ವರ್ಷ ಆಯುಷ್ಯ
- **Sarvam-1** ✓: This means that if you make a mistake, it is better to correct it than to keep doing something wrong for a long time.

## 43. ನಾರಿ ಒಲಿದರೆ ನಾರಿ, ಮುನಿದರೆ ಮಾರಿ  (figurative)
*EN: If a woman is won over she is a woman, if angered she is a fearsome goddess.*

- **Gold:** ಹೆಣ್ಣು ಪ್ರೀತಿಯಿಂದ ಒಲಿದರೆ ಮಮತೆಯ ಹೆಣ್ಣಾಗಿರುತ್ತಾಳೆ, ಕೋಪಗೊಂಡರೆ ಭಯಂಕರ ರೂಪ ತಾಳುತ್ತಾಳೆ ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: A woman who is won over with love is an affectionate woman; if angered she takes a terrifying form.*
- **mT0-large** ✓: """కొడుకును గట్టిగా దూసుకుపోతుంటే, నాన్నను గట్టిగా దూసుకుపోతుంటే, నాన్నను గట్టిగా దూసుకుపోతుంటే, నాన్నను గట్టిగా దూసుకుపోతుంటే, నాన్నను గట్టిగా దూసుకుపో
  - *EN: [Telugu] "When pushing hard at the son, pushing hard at the father, pushing hard at the father..." (repetitive)*
- **Qwen3.5-2B** ✗: ನಾರಿ ಒಲಿದರೆ ನಾರಿ, ಮುನಿದರೆ ಮಾರಿ
- **Sarvam-1** ✓: If you are not careful with your words and actions, then you will suffer consequences.

## 44. ಎತ್ತು ಏರಿಗೆಳೆದರೆ ಕೋಣ ನೀರಿಗೆಳೆಯಿತು  (figurative)
*EN: When the ox pulled uphill, the buffalo pulled into the water*

- **Gold:** ಇಬ್ಬರು ಜೊತೆಗೂಡಿ ಕೆಲಸ ಮಾಡುವಾಗ ಒಬ್ಬರು ಒಂದು ದಿಕ್ಕಿಗೆ, ಇನ್ನೊಬ್ಬರು ಉಲ್ಟಾ ದಿಕ್ಕಿಗೆ ಎಳೆದು ಕೆಲಸ ಹಾಳಾಗುವುದು ಎಂದು ಈ ಗಾದೆಯ ಅರ್ಥ.
  - *EN: When two people work together, one pulls in one direction and the other in the opposite direction, spoiling the work.*
- **mT0-large** ✓: A man took a horse to the river.
- **Qwen3.5-2B** ✗: Proverb: ಎತ್ತು ಏರಿಗೆಳೆದರೆ ಕೋಣ ನೀರಿಗೆಳೆಯಿತು
- **Sarvam-1** ✓: If you try to do something that is beyond your abilities, it will not work out well for you.

## 45. ಮುತ್ತು ಕೊಡುವವಳು ಬಂದಳು ಅಂತ, ತುತ್ತು ಕೊಟ್ಟವಳನ್ನು ಮರೆಯಬಾರದು  (figurative)
*EN: Though the one who gives kisses has come, don't forget the one who gave you morsels*

- **Gold:** ಹೊಸ ಆಕರ್ಷಣೆ ಅಥವಾ ಸಂಬಂಧ ಬಂದಾಗ, ಕಷ್ಟಕಾಲದಲ್ಲಿ ಅನ್ನ ಹಾಕಿ ಸಾಕಿದವರನ್ನು ಅಥವಾ ಉಪಕಾರ ಮಾಡಿದವರನ್ನು ಮರೆಯಬಾರದು ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: When a new attraction or relationship comes along, one should not forget those who fed and raised one in hard times or did one favors.*
- **mT0-large** ✓: """ఇది మంచి రోజు."""
  - *EN: [Telugu] "This is a good day."*
- **Qwen3.5-2B** ✓: The user wants a one-sentence explanation of the provided Kannada proverb.
- **Sarvam-1** ✓: ಈ proverb ಹೇಳೋದೇನೆಂದರೆ, ಯಾರಾದ್ರೂ ನಿಮಗೆ ಒಳ್ಳೆಯದನ್ನು ಮಾಡಿದ್ರೆ, ಅವರು ಹೋದ ಮೇಲೆ ನೀವು ಅವರನ್ನ ಮರೆತುಬಿಡಬಾರದು.

## 46. ಸಿಂಧಘಟ್ಟದ ದೇವರು ಹಿಂದ್ ಮುಂದ್ ಆಡ  (figurative)
*EN: The god of Sindhaghatta wavers back and forth*

- **Gold:** ಸ್ಥಳೀಯ ಉಪಭಾಷೆಯ ಗಾದೆ, ಪದಗಳು ಸ್ಪಷ್ಟವಿಲ್ಲ; ಒಂದು ಮಾತಿಗೆ ನಿಂತಿರದೆ ಹಿಂದೆ ಮುಂದೆ ತೂಗಾಡುವ, ಅನಿಶ್ಚಿತ ವರ್ತನೆ ಎಂದು ಊಹೆ (ಖಚಿತವಿಲ್ಲ).
  - *EN: A proverb in a local dialect whose words are unclear; guessed to mean wavering, uncertain behavior and not standing by one's word (uncertain).*
- **mT0-large** ✓: The god of the mountains went back and forth.
- **Qwen3.5-2B** ✓: ಸಿಂಧಘಟ್ಟದ ದೇವರು ಹಿಂದ್ ಮುಂದ್ ಆಡ
- **Sarvam-1** ✓: This means that sometimes you have to do things your way, even if it is not what others think or want.

## 47. ಗೋಕುಲಾಷ್ಟಮಿಗೂ ಇಮಾಮ್ ಸಾಬಿಗೂ ಏನ್ ಸಂಬಂಧ  (figurative)
*EN: What relation is there between Gokulashtami and Imam Saab?*

- **Gold:** ಸಂಬಂಧವೇ ಇಲ್ಲದ ವಿಷಯವನ್ನು ಸಂಬಂಧವಿಲ್ಲದ ಜಾಗದಲ್ಲಿ ತಂದು ಸೇರಿಸುವುದು, ಅಂದರೆ ಅಪ್ರಸ್ತುತ ಮಾತು ಎಂದು ಈ ಗಾದೆಯ ಅರ್ಥ.
  - *EN: Bringing an unrelated matter into an unrelated place; that is, an irrelevant remark.*
- **mT0-large** ✗: They are related to a temple
- **Qwen3.5-2B** ✓: ಗೋಕುಲಾಷ್ಟಮಿಗೂ ಇಮಾಮ್ ಸಾಬಿಗೂ ಏನ್ ಸಂಬಂಧ
- **Sarvam-1** ✓: Goosebumps are a natural response to fear or excitement, and they can be triggered by many things, including stories about Imam Sadiq (a famous Islamic scholar). However, it's important to remember that goosebumps don't necessarily mean you have

## 48. ಇಂದು ಆಳಾಗಿ ಬದುಕುವವನೇ ಮುಂದೆ ಅರಸಾಗುವ  (literal)
*EN: One who lives as a servant today will be a king tomorrow*

- **Gold:** ಇಂದು ಸೇವಕನಂತೆ ವಿನಯದಿಂದ ದುಡಿಯುವವನು ಮುಂದೊಂದು ದಿನ ಮೇಲಿನ ಸ್ಥಾನಕ್ಕೆ ಏರುತ್ತಾನೆ ಎಂಬುದು ಇದರ ಅರ್ಥ.
  - *EN: One who works humbly like a servant today will one day rise to a higher position.*
- **mT0-large** ✓: ದೀರ್ಘ జీవితం గడపడానికి ಶಕ್ತಿಯನ್ನು ನೀಡುವ
  - *EN: [Kannada+Telugu mix] Which gives strength to lead a long life*
- **Qwen3.5-2B** ✓: ಇಂದು ಆಳಾಗಿ ಬದುಕುವವನೇ ಮುಂದೆ ಅರಸಾಗುವ
- **Sarvam-1** ✓: This means that if you want to be successful, you have to work hard and not just rely on luck or good fortune. You need to take action and make things happen for yourself.

## 49. ಎಲ್ಲರ ಮನೆ ದೋಸೆ ತೂತು  (figurative)
*EN: Everyone's house has holes in the dosa*

- **Gold:** ಎಲ್ಲರ ಮನೆಯಲ್ಲೂ ಒಂದಲ್ಲ ಒಂದು ಸಮಸ್ಯೆ ಅಥವಾ ಕೊರತೆ ಇರುತ್ತದೆ, ಪರಿಪೂರ್ಣ ಮನೆ ಯಾರದೂ ಇಲ್ಲ ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: Every house has some problem or shortcoming; nobody's house is perfect.*
- **mT0-large** ✓: All the houses are empty.
- **Qwen3.5-2B** ✓: All people's houses are filled with dough.
- **Sarvam-1** ✓: This means that everyone has problems and difficulties, so don't worry about other people's problems because they are your own problem too. [/INST]

## 50. ಅಳಿಯ ಅಲ್ಲ ಮಗಳ ಗಂಡ  (figurative)
*EN: Not a son-in-law, just the daughter's husband*

- **Gold:** ಅಳಿಯ ತನ್ನ ಸ್ವಂತ ಮಗನಂತೆ ಅಲ್ಲ, ಕೇವಲ ಮಗಳ ಗಂಡ ಎಂಬ ಸಂಬಂಧದಿಂದ ಮಾತ್ರ ಬಂದವನು ಎಂದು ಹೇಳುವ ಮಾತು ಎಂದು ತೋರುತ್ತದೆ
  - *EN: A remark that the son-in-law is not like one's own son but has come only through the relationship of being the daughter's husban.*
- **mT0-large** ✓: A husband is not a mother.
- **Qwen3.5-2B** ✓: ಅಳಿಯ ಅಲ್ಲ ಮಗಳ ಗಂಡ (Alyi aall maa gaand) translates to "A son is not a daughter's husband." This proverb means that a man cannot marry a woman who is his daughter's sister, as it would be incestuous.
- **Sarvam-1** ✓: This means that a son-in-law is not always like his father-in-law, and vice versa.

## 51. ಆಡಿದರೆ ಅರಗಿಣಿ, ಕಾಡಿದರೆ ನಾಗರಕಾಟ  (figurative)
*EN: If played with, a parrot; if provoked, a cobra*

- **Gold:** ಪ್ರೀತಿಯಿಂದ ಆಡಿಸಿದರೆ ಮುದ್ದಾದ ಗಿಳಿಯಂತೆ, ಕೆಣಕಿದರೆ ಕಾಡುವ ನಾಗರಹಾವಿನಂತೆ ಆಗುವವರ ಬಗ್ಗೆ ಹೇಳುವ ಮಾತು ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: A saying about those who are like a sweet parrot when treated lovingly and like a tormenting cobra when provoked .*
- **mT0-large** ✗: ಕಾಡಿದರೆ ಅರಗಿಣಿ, ಕಾಡಿದರೆ ನಾಗರಕಾಟ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: ಆಡಿದರೆ ಅರಗಿಣಿ, ಕಾಡಿದರೆ ನಾಗರಕಾಟ (If you run, you will be lost; if you walk, you will be trapped)
- **Sarvam-1** ✓: This means that if you try to do something and fail, it is better to give up than keep trying and possibly get hurt or worse.

## 52. ಅಳುವ ಗಂಡಸನ್ನು, ನಗುವ ಹೆಂಗಸನ್ನು ನಂಬಬಾರದು  (figurative)
*EN: Don't trust a weeping man or a laughing woman*

- **Gold:** ಅತಿಯಾಗಿ ಅಳುವ ಗಂಡಸಿನ ಅಥವಾ ಅತಿಯಾಗಿ ನಗುವ ಹೆಂಗಸಿನ ಭಾವನೆ ತೋರಿಕೆಯಾಗಿರಬಹುದು, ಆದ್ದರಿಂದ ಅಂಥವರ ಮಾತನ್ನು ಕಣ್ಣು ಮುಚ್ಚಿ ನಂಬಬಾರದು ಎಂದು ಅರ್ಥ.
  - *EN: The emotion of a man who weeps excessively or a woman who laughs excessively may be put on, so one should not blindly trust such people's words.*
- **mT0-large** ✓: A loud noise, a loud smile, and a loud smile.
- **Qwen3.5-2B** ✓: ಅಳುವ ಗಂಡಸನ್ನು, ನಗುವ ಹೆಂಗಸನ್ನು ನಂಬಬಾರದು ಎಂದರೆ, ಅಳುವ ಗಂಡಸನ್ನು ನಂಬಬಾರದು.
- **Sarvam-1** ✓: This means that if someone is crying or upset, you should not believe them when they say something will be good for them because it might just make things worse. It's better to listen to what they are saying and think carefully before making a decision.

## 53. ಅಯ್ಯೋ ಪಾಪ ಅಂದರೆ ಅರ್ಧ ಆಯುಷ್ಯ  (figurative)
*EN: Saying 'oh, poor thing' is half a lifespan*

- **Gold:** ಕಷ್ಟದಲ್ಲಿರುವವರಿಗೆ ಸಹಾನುಭೂತಿಯ ಒಂದು ಮಾತು ಕೂಡ ಅಪಾರ ಧೈರ್ಯ ಮತ್ತು ಸಮಾಧಾನ ಕೊಡುತ್ತದೆ ಎಂದು ಅರ್ಥ.
  - *EN: Even one word of sympathy gives great courage and comfort to those in trouble.*
- **mT0-large** ✓: 'ಪಾಪ' ಅಂದರೆ ಅರ್ಧ ಆಯುಷ್ಯ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: ಅಯ್ಯೋ ಪಾಪ ಅಂದರೆ ಅರ್ಧ ಆಯುಷ್ಯ
- **Sarvam-1** ✗: This means that if you do something wrong, it will affect your life for a long time. It is like saying "the longer you live, the more you learn". If you make mistakes when young, they can have serious consequences later on.

## 54. ಆಡುವವ ಆಡಿದರೆ ನೋಡುವವನಿಗೆ ಸಿಗ್ಗು  (figurative)
*EN: If the performer performs, the onlooker feels shame*

- **Gold:** ತಪ್ಪು ಮಾಡುವವನಿಗೆ ನಾಚಿಕೆ ಇರುವುದಿಲ್ಲ, ಆದರೆ ಅದನ್ನು ನೋಡುವವರಿಗೆ ಮುಜುಗರವಾಗುತ್ತದೆ ಎಂದು ಅರ್ಥ.
  - *EN: The one who does wrong has no shame, but those who watch it feel embarrassed.*
- **mT0-large** ✗: ಆಡುವವ ಆಡಿದರೆ ನೋಡುವವನಿಗೆ ಸಿಗ್ಗಾ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಆಡುವವ ಆಡಿದರೆ ನೋಡುವವನಿಗೆ ಸಿಗ್ಗು
- **Sarvam-1** ✓: This means that if you are playing, then others will be watching and enjoying what you do. If you don't play well or make mistakes, they won't be happy to see it. [/INST]

## 55. ಅಂಜಿರುವವನ ಮೇಲೆ ಕಪ್ಪೆ ಹಾರಿದಂಗೆ  (figurative)
*EN: Like a frog jumping on one who is already frightened*

- **Gold:** ಈಗಾಗಲೇ ಭಯ ಅಥವಾ ಕಷ್ಟದಲ್ಲಿರುವವನಿಗೆ ಇನ್ನೊಂದು ಸಣ್ಣ ತೊಂದರೆ ಬಂದು ಅವನನ್ನು ಇನ್ನಷ್ಟು ಕಂಗಾಲು ಮಾಡುತ್ತದೆ ಎಂದು ಅರ್ಥ.
  - *EN: Another small trouble comes to one already in fear or hardship and unnerves him further.*
- **mT0-large** ✓: ತನ್ನ ಮಗುವಿನ ಮೇಲೆ ಕಪ್ಪೆ ಹಾರಿಸಿದನು
  - *EN: He threw a frog on his child*
- **Qwen3.5-2B** ✓: ಅಂಜಿರುವವನ ಮೇಲೆ ಕಪ್ಪೆ ಹಾರಿದಂಗೆ
- **Sarvam-1** ✓: This means that someone who is already in a difficult situation will not be able to help themselves, and they need others' assistance.

## 56. ಅಲ್ಲದ ಕನಸು ಕಂಡರೆ ಎದ್ದು ಕುಂಡ್ರು  (figurative)
*EN: If you see a bad dream, get up and sit*

- **Gold:** ಅಪಶಕುನ ಅಥವಾ ಅಪಾಯದ ಸೂಚನೆ ಕಂಡರೆ ಮಲಗಿ ನಿರ್ಲಕ್ಷಿಸದೆ ಎಚ್ಚೆತ್ತು ಜಾಗರೂಕರಾಗಬೇಕು ಎಂದು ಅರ್ಥ ಇರಬಹುದು.
  - *EN: It may mean that on seeing a bad omen or sign of danger, one should wake up and be alert rather than lie down and ignore it.*
- **mT0-large** ✓: 'ಅವನು ತನ್ನ ಕನಸು ಕಾಣುತ್ತಾ '
  - *EN: 'He, dreaming his dream' (truncated)*
- **Qwen3.5-2B** ✓: ಅಲ್ಲದ ಕನಸು ಕಂಡರೆ ಎದ್ದು ಕುಂಡ್ರು
- **Sarvam-1** ✓: This means that if you don't try to achieve something, then it will never happen. It is a way of saying that if you want something badly enough and work hard at achieving it, then you can do it. If you just sit around waiting for things to happen without trying, then

## 57. ಅಡ್ಡ ಗೋಡೆಯ ಮೇಲೆ ದೀಪ ಇಟ್ಟ ಹಾಗೆ  (figurative)
*EN: Like placing a lamp on the dividing wall*

- **Gold:** ಎರಡು ಬದಿಯವರಿಗೂ ಸಮಾನವಾಗಿ ಉಪಯೋಗವಾಗುವ ಅಥವಾ ಯಾರ ಪರವೂ ಅಲ್ಲದ ಏರ್ಪಾಡು ಎಂದು ಅರ್ಥ ಇರಬಹುದು.
  - *EN: It may mean an arrangement that is equally useful to both sides, or one that favors neither side.*
- **mT0-large** ✓: ಅಡ್ಡ ಗೋಡೆ ಮೇಲೆ ದೀಪ ಇಟ್ಟಂತೆ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಅಡ್ಡ ಗೋಡೆಯ ಮೇಲೆ ದೀಪ ಇಟ್ಟ ಹಾಗೆ
- **Sarvam-1** ✓: This means that you should not put a lot of effort into something if it is unlikely to be successful or worthwhile. It's like putting up a light on an exterior wall, which will only waste energy and money without providing any benefit. </s>

## 58. ಆರು ಕೊಟ್ಟರೆ ಅತ್ತೆ ಕಡೆ, ಮೂರು ಕೊಟ್ಟರೆ ಸೊಸೆ ಕಡೆ  (figurative)
*EN: If you give six, he's on the mother-in-law's side; if you give three, on the daughter-in-law's side*

- **Gold:** ಹೆಚ್ಚು ಕೊಟ್ಟವರ ಪರ ವಹಿಸುವವನು ನ್ಯಾಯ ನೋಡದೆ ಲಾಭ ನೋಡುತ್ತಾನೆ ಎಂದು ಅರ್ಥ.
  - *EN: One who sides with whoever gives more looks for profit, not justice.*
- **mT0-large** ✓: ಆರು ಕೊಟ್ಟರೆ ಅತ್ತೆ ಕಡೆ, ಮೂರು ಕೊಟ್ಟರೆ ಸೊಸೆ ಕಡೆ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: ಆರು ಕೊಟ್ಟರೆ ಅತ್ತೆ ಕಡೆ, ಮೂರು ಕೊಟ್ಟರೆ ಸೊಸೆ ಕಡೆ
- **Sarvam-1** ✗: This means that if you give someone something they will expect more than what was given to them. It is a way of saying that people are greedy and always want more. </s>

## 59. ಅಡಿಕೆಗೆ ಹೋದ ಮಾನ ಆನೆ ಕೊಟ್ಟರೂ ಬಾರದು  (figurative)
*EN: Honor lost over a betel nut won't return even if an elephant is given*

- **Gold:** ಸಣ್ಣ ವಿಷಯಕ್ಕೆ ಒಮ್ಮೆ ಮರ್ಯಾದೆ ಕಳೆದುಕೊಂಡರೆ ಎಷ್ಟೇ ದೊಡ್ಡ ಬೆಲೆ ಕೊಟ್ಟರೂ ಅದನ್ನು ಮರಳಿ ಪಡೆಯಲಾಗುವುದಿಲ್ಲ ಎಂದು ಅರ್ಥ.
  - *EN: Once one loses honor over a small matter, it cannot be regained however high a price is paid.*
- **mT0-large** ✓: ಮಾನವನ್ನು காற்றில் లోపలికి రావడానికి ಕಲ್ಲುಗಳು లేక ಕಲ್ಲುಗಳು లేక ಕಲ್ಲುಗಳು లేక ಕಲ್ಲುಗಳು లేక ಕಲ್ಲುಗಳು లేక ಕಲ್ಲುಗಳು లేక ಕಲ್ಲುಗಳು లేక ಕಲ್ಲುಗಳು లేక ಕಲ್ಲುಗಳು లేక ಕಲ್ಲುಗಳು
  - *EN: [Kannada+Telugu+Tamil mix] Honour in the wind, to come inside, without stones, without stones, without stones... (repetitive, nonsensical)*
- **Qwen3.5-2B** ✓: ಅಡಿಕೆಗೆ ಹೋದ ಮಾನ ಆನೆ ಕೊಟ್ಟರೂ ಬಾರದು
- **Sarvam-1** ✓: This means that if you try to do something difficult or impossible, no matter how much help you get from others, it will not work out well for you.

## 60. ಅಜ್ಜಿಗೆ ಅರಿವೆ ಚಿಂತೆ, ಮಗಳಿಗೆ ಮದುವೆ ಚಿಂತೆ  (literal)
*EN: The grandmother worries about cloth, the daughter worries about marriage*

- **Gold:** ಒಬ್ಬೊಬ್ಬರಿಗೂ ತಮ್ಮ ವಯಸ್ಸು ಮತ್ತು ಸ್ಥಿತಿಗೆ ತಕ್ಕಂತೆ ಬೇರೆ ಬೇರೆ ಚಿಂತೆಗಳಿರುತ್ತವೆ ಎಂದು ಅರ್ಥ.
  - *EN: Each person has different worries according to their age and situation.*
- **mT0-large** ✗: ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು
  - *EN: children children children children... (repetitive)*
- **Qwen3.5-2B** ✓: ಅಜ್ಜಿಗೆ ಅರಿವೆ ಚಿಂತೆ, ಮಗಳಿಗೆ ಮದುವೆ ಚಿಂತೆ
- **Sarvam-1** ✓: This means that when you worry about something for your grandmother or mother, it is likely to affect them as well. It's like a chain reaction. [/INST]

## 61. ಅಕ್ಕಿ ಮೇಲೆ ಆಸೆ, ನೆಂಟರ ಮೇಲೆ ಪ್ರೀತಿ  (literal)
*EN: Desire for the rice, love for the relatives*

- **Gold:** ಸಂಬಂಧಿಕರ ಮೇಲೆ ಪ್ರೀತಿ ಇದೆ ಎನ್ನುವವರ ನಿಜವಾದ ಆಸೆ ಅಲ್ಲಿ ಸಿಗುವ ಊಟ, ಲಾಭದ ಮೇಲಿರುತ್ತದೆ ಎಂದು ಅರ್ಥ ಇರಬಹುದು.
  - *EN: It may mean that the real desire of those who claim love for relatives is for the food and benefit they get there.*
- **mT0-large** ✗: A few dogs love a rabbit.
- **Qwen3.5-2B** ✓: ಅಕ್ಕಿ ಮೇಲೆ ಆಸೆ, ನೆಂಟರ ಮೇಲೆ ಪ್ರೀತಿ
- **Sarvam-1** ✓: This means that when you have something very important to do or want, it is easy to forget about other things and people who are more important.

## 62. ಅಂಬಲಿ ಕುಡಿಯುವವನಿಗೆ ಮೀಸೆ ತಿದ್ದುವನೊಬ್ಬ  (figurative)
*EN: One to trim the moustache of the man who drinks gruel*

- **Gold:** ಬಡತನದಲ್ಲೂ ತಮ್ಮ ಸ್ಥಿತಿಗೆ ಮೀರಿದ ಆಡಂಬರ ಮತ್ತು ಶೋಕಿ ಮಾಡುವವರನ್ನು ಗೇಲಿ ಮಾಡುವ ಮಾತು.
  - *EN: A mocking saying about those who indulge in show and luxury beyond their means even in poverty.*
- **mT0-large** ✓: An angel is a snake
- **Qwen3.5-2B** ✓: ಅಂಬಲಿ ಕುಡಿಯುವವನಿಗೆ ಮೀಸೆ ತಿದ್ದುವನೊಬ್ಬ
- **Sarvam-1** ✓: This means that someone who is always trying to be perfect will never succeed because perfection is impossible.

## 63. ಅಂತು ಇಂತು ಕುಂತಿ ಮಕ್ಕಳಿಗಿಲ್ಲ ಎಂಟು ರಾಜ್ಯ  (figurative)
*EN: One way or another, the sons of Kunti don't have eight kingdoms*

- **Gold:** ಎಷ್ಟೆಲ್ಲಾ ಪ್ರಯತ್ನಪಟ್ಟರೂ ಕೊನೆಗೆ ನಿರೀಕ್ಷಿಸಿದ ಲಾಭ ಸಿಗಲಿಲ್ಲ ಎಂದು ಅರ್ಥ ಇರಬಹುದು.
  - *EN: It may mean that after so much effort, they didn't get the expected gain in the end.*
- **mT0-large** ✗: ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು
  - *EN: children children children children... (repetitive)*
- **Qwen3.5-2B** ✓: ಅಂತು ಇಂತು ಕುಂತಿ ಮಕ್ಕಳಿಗಿಲ್ಲ ಎಂಟು ರಾಜ್ಯ
- **Sarvam-1** ✓: This means that if you don't have a good relationship with your children, then you will not be able to get any other state or position.

## 64. ಅತ್ತೆಗೊಂದು ಕಾಲ, ಸೊಸೆಗೊಂದು ಕಾಲ  (figurative)
*EN: A time for the mother-in-law, a time for the daughter-in-law*

- **Gold:** ಪ್ರತಿಯೊಬ್ಬರಿಗೂ ತಮ್ಮದೇ ಆದ ಅಧಿಕಾರದ ಸಮಯ ಇರುತ್ತದೆ, ಅದು ಶಾಶ್ವತವಲ್ಲ, ಕಾಲ ಬದಲಾದಂತೆ ಅಧಿಕಾರ ಕೈ ಬದಲಾಗುತ್ತದೆ ಎಂದು ಅರ್ಥ.
  - *EN: Everyone has their own time of authority; it is not permanent, and as time changes, authority changes hands.*
- **mT0-large** ✓: A mother and a son have a different time.
- **Qwen3.5-2B** ✓: ಅತ್ತೆಗೊಂದು ಕಾಲ, ಸೊಸೆಗೊಂದು ಕಾಲ (Ate-godun kaal, soose-godun kaal) means that a son's life is dedicated to his father, while a daughter's life is dedicated to her mother.
- **Sarvam-1** ✓: This means that there are times when you have to take care of your own family and other times when you need to help others.

## 65. ಆಸೆಯೇ ದುಃಖಕ್ಕೆ ಮೂಲ  (literal)
*EN: Desire is the root of sorrow*

- **Gold:** ಬಯಕೆಗಳು ಹೆಚ್ಚಿದಷ್ಟೂ ದುಃಖವೂ ಹೆಚ್ಚುತ್ತದೆ, ಆಸೆಯೇ ದುಃಖಕ್ಕೆ ಕಾರಣ ಎಂದು ಅರ್ಥ.
  - *EN: The more desires grow, the more sorrow grows; desire is the cause of sorrow.*
- **mT0-large** ✗: ದುಃಖದ ಮೂಲವು ಆಸೆಗಳು.
  - *EN: Desires are the root of sorrow.*
- **Qwen3.5-2B** ✗: ಆಸೆಯೇ ದುಃಖಕ್ಕೆ ಮೂಲ (Hope is the root of sorrow) is a proverb that suggests that **hopelessness or despair is often the direct result of a lack of hope or optimism.**
- **Sarvam-1** ✓: This means that if you are always thinking about something, it will make you unhappy. It is a way to say that worrying can cause problems and make things worse.

## 66. ಆಳ್ ಮೇಲ್ ಆಳ್ ಬಿದ್ದು ಗೋಣು ಬರಿದಾಯ್ತು  (figurative)
*EN: People fell upon people and the neck became empty*

- **Gold:** ಅನೇಕರು ಒಬ್ಬರ ಮೇಲೊಬ್ಬರು ನುಗ್ಗಿ ಬಿದ್ದ ಕಾರಣ ಕೊನೆಗೆ ಏನೂ ಉಳಿಯಲಿಲ್ಲ ಎಂದು ಅರ್ಥ ಇರಬಹುದು.
  - *EN: It may mean that since many people rushed and fell over one another, nothing was left in the end.*
- **mT0-large** ✗: గోను మీద ఆల్ మీద ఆల్ ಬಿದ್ದాయి.
  - *EN: [Telugu+Kannada mix] Banyan trees fell on top of banyan trees on the sack(?). (nonsensical)*
- **Qwen3.5-2B** ✓: ಆಳ್ ಮೇಲ್ ಆಳ್ ಬಿದ್ದು ಗೋಣು ಬರಿದಾಯ್ತು
- **Sarvam-1** ✓: This means that if you try to do something too hard or difficult, it will not work out well for you. It is better to take things step by step and be patient.

## 67. ಅರಿಯದೆ ಮಾಡಿದ ಪಾಪ ಅರಿದಂತು ಪರಿಹಾರ  (literal)
*EN: Sin done unknowingly has a remedy once known*

- **Gold:** ತಿಳಿಯದೆ ಮಾಡಿದ ತಪ್ಪನ್ನು ತಿಳಿದ ಮೇಲೆ ಒಪ್ಪಿಕೊಂಡು ಪಶ್ಚಾತ್ತಾಪಪಟ್ಟರೆ ಅದಕ್ಕೆ ಪರಿಹಾರ ಸಿಗುತ್ತದೆ.
  - *EN: If one admits and repents of a mistake done unknowingly once one knows of it, there is a remedy for it.*
- **mT0-large** ✓: A mistake that is a mistake that is a mistake that is a mistake.
- **Qwen3.5-2B** ✓: ಅರಿಯದೆ ಮಾಡಿದ ಪಾಪ ಅರಿದಂತು ಪರಿಹಾರ
- **Sarvam-1** ✓: This means that if you do something without knowing it is wrong, then there will be no way to fix it later on. It's like trying to put out a fire with water - it won't work! You need to know what you are doing before you start so that you can make

## 68. ಅಕ್ಕರೆಯಿದ್ದಲ್ಲಿ ದುಃಖವುಂಟು  (figurative)
*EN: Where there is affection, there is sorrow*

- **Gold:** ಯಾರ ಮೇಲೆ ಪ್ರೀತಿ ಹೆಚ್ಚೋ ಅವರ ಬಗ್ಗೆಯೇ ಚಿಂತೆ ಮತ್ತು ನೋವೂ ಹೆಚ್ಚಿರುತ್ತದೆ ಎಂದು ಅರ್ಥ.
  - *EN: The more one loves someone, the more worry and pain there is about them.*
- **mT0-large** ✓: A sheep is a sheep.
- **Qwen3.5-2B** ✓: ಅಕ್ಕರೆಯಿದ್ದಲ್ಲಿ ದುಃಖವುಂಟು
- **Sarvam-1** ✓: This means that if you are kind to others, then they will be kind to you too. If you are mean or unkind to others, then they may not want to be your friend.

## 69. ಅಕ್ಕನ ಚಿನ್ನವಾದರೂ ಅಕ್ಕಸಾಲಿಗ ಕದಿಯದೆ ಬಿಡಾ  (figurative)
*EN: Even if it is his sister's gold, the goldsmith won't leave without stealing*

- **Gold:** ವೃತ್ತಿಯ ಲಾಭ ನೋಡುವವನು ಸ್ವಂತ ಸಂಬಂಧಿಕರ ಕೆಲಸದಲ್ಲೂ ತನ್ನ ಪಾಲು ತೆಗೆಯದೆ ಬಿಡುವುದಿಲ್ಲ ಎಂದು ಅರ್ಥ.
  - *EN: One who looks to professional profit won't leave without taking his cut even from his own relatives' work.*
- **mT0-large** ✓: 'ఆಕೆ ತನ್ನ ಚಿನ್ನವನ್ನು 'ఆಕೆ' ಗೆ ಕದಿಯುವುದಿಲ್ಲ.
  - *EN: [Kannada+Telugu mix] 'She' does not steal her gold for 'she'. (nonsensical)*
- **Qwen3.5-2B** ✓: ಅಕ್ಕನ ಚಿನ್ನವಾದರೂ ಅಕ್ಕಸಾಲಿಗ ಕದಿಯದೆ ಬಿಡಾ
- **Sarvam-1** ✓: This means that even if someone has something valuable, like gold or money, they should not steal it because their family will be hurt by it.

## 70. ಐಕಟ್ಟು ಇಲ್ಲದವನಿಗೆ ಆರು ಕಟ್ಟು ವಿಭೂತಿ  (figurative)
*EN: Six bundles of sacred ash for one who doesn't have five bundles*

- **Gold:** ಅರ್ಥ ಸ್ಪಷ್ಟವಿಲ್ಲ; ಅಗತ್ಯ ವಸ್ತು ಇಲ್ಲದವನಿಗೆ ಅನಗತ್ಯ ಹೆಚ್ಚುವರಿ ವಸ್ತು ಸಿಕ್ಕುವ ವಿಪರ್ಯಾಸವನ್ನು ಹೇಳುವ ಮಾತು ಇರಬಹುದು.
  - *EN: The meaning is not clear; it may be a saying about the irony of someone lacking a necessity getting an unnecessary extra.*
- **mT0-large** ✗: ಕಲ್ಲುಗಳನ್ನು ಹಿಡಿದಿಡಲು ಐದು ಕಟ್ಟುಗಳಷ್ಟು ವಿಭೂತಿ
  - *EN: Five bundles' worth of sacred ash to hold the stones (nonsensical)*
- **Qwen3.5-2B** ✓: ಐಕಟ್ಟು ಇಲ್ಲದವನಿಗೆ ಆರು ಕಟ್ಟು ವಿಭೂತಿ
- **Sarvam-1** ✓: This means that if you have no money, then it is better to be poor than rich because a person with money can easily get into trouble and lose everything.

## 71. ಬಯಸಿ ಬಯಸಿ ಮದುವೆಯಾದ್ರೆ ಬಡಿಯೋ ಗಂಡ ಸಿಕ್ಕಿದ  (figurative)
*EN: If you marry the one you wanted and wanted, you got a husband who beats*

- **Gold:** ತುಂಬಾ ಆಸೆಪಟ್ಟು ಪಡೆದದ್ದೇ ಕೊನೆಗೆ ತೊಂದರೆಯಾಗಿ ಪರಿಣಮಿಸುವುದು ಎಂದು ಅರ್ಥ.
  - *EN: What one desired so much turns out in the end to be a trouble.*
- **mT0-large** ✓: 'ಬಡಿಯೋ ಗಂಡ' - 'ಬಡಿಯೋ'
  - *EN: 'The beating husband' - 'beating'*
- **Qwen3.5-2B** ✗: ಬಯಸಿ ಬಯಸಿ ಮದುವೆಯಾದ್ರೆ ಬಡಿಯೋ ಗಂಡ ಸಿಕ್ಕಿದ
- **Sarvam-1** ✓: This means that if you want something badly enough, it will come to you eventually. It's like a saying about how hard work and determination can lead to success. </s>

## 72. ಬೇಲಿಯೇ ಎದ್ದು ಹೊಲ ಮೇಯ್ದ ಹಾಗೆ  (figurative)
*EN: Like the fence rising up and grazing the field*

- **Gold:** ರಕ್ಷಿಸಬೇಕಾದವನೇ ನಂಬಿಕೆಗೆ ದ್ರೋಹ ಮಾಡಿ ಹಾನಿ ಮಾಡುವುದು ಎಂದು ಅರ್ಥ.
  - *EN: The one who should protect betrays the trust and causes harm.*
- **mT0-large** ✓: ತೋಳಗಳು ರಸ್ತೆ ದಾಟುತ್ತವೆ
  - *EN: Wolves cross the road*
- **Qwen3.5-2B** ✓: ಬೇಲಿಯೇ ಎದ್ದು ಹೊಲ ಮೇಯ್ದ ಹಾಗೆ
- **Sarvam-1** ✓: This means that if you want to get something done, then you have to work hard and not give up easily. If you are lazy or do not try very hard, then it will be difficult for you to achieve your goal.

## 73. ಭಂಗಿ ದೇವರಿಗೆ ಹೆಂಡ ಕುಡುಕ ಪೂಜಾರಿ  (figurative)
*EN: A hemp god, a toddy-drinking priest*

- **Gold:** ಯಜಮಾನ ಮತ್ತು ಸೇವಕ ಇಬ್ಬರೂ ಒಂದೇ ರೀತಿಯ ಕೆಟ್ಟ ಗುಣದವರಾಗಿ ಚೆನ್ನಾಗಿ ಜೋಡಿಯಾಗಿರುವುದು ಎಂದು ಅರ್ಥ.
  - *EN: Master and servant are both of the same kind of bad quality and are well matched.*
- **mT0-large** ✓: దేవునికి భక్తులకు మంచి భోజనం ఇచ్చే వారు.
  - *EN: [Telugu] Those who give a good meal to God's devotees.*
- **Qwen3.5-2B** ✓: Here is the meaning of the proverb in one short sentence:
- **Sarvam-1** ✓: This means that a person who is not good at his job or does not do it well will be looked down upon by others, and may even face punishment from God.

## 74. ಬಯಕೆಗೆ ಬಡವರಿಲ್ಲ  (literal)
*EN: There are no poor in desire*

- **Gold:** ಆಸೆಗಳ ವಿಷಯದಲ್ಲಿ ಯಾರೂ ಬಡವರಲ್ಲ; ಶ್ರೀಮಂತರಿಗೂ ಬಯಕೆಗಳು ಇದ್ದೇ ಇರುತ್ತವೆ.
  - *EN: In the matter of desires nobody is poor; even the rich have desires.*
- **mT0-large** ✓: desire is not a poor person
- **Qwen3.5-2B** ✓: The meaning of the proverb is:
- **Sarvam-1** ✓: This means that if you want something badly enough, then it will come to you eventually. It doesn't matter how much money or resources you have - if you really need something, someone will give it to you.

## 75. ಚೇಳಿಗೆ ಪಾರುಪತ್ಯ ಕೊಟ್ಟ ಹಾಗೆ  (figurative)
*EN: Like giving charge to a scorpion*

- **Gold:** ಹಾನಿ ಮಾಡುವ ಸ್ವಭಾವದವನಿಗೆ ಅಧಿಕಾರ ಅಥವಾ ಜವಾಬ್ದಾರಿ ಕೊಡುವುದು ಅಪಾಯಕಾರಿ ಎಂದು ಅರ್ಥ.
  - *EN: Giving authority or responsibility to someone of a harmful nature is dangerous.*
- **mT0-large** ✗: ಚೆಲ್ಲಿಗೆ ಪಾರುಪತ್ಯ ఇచ్చారు
  - *EN: [Kannada+Telugu mix] They gave authority to a spendthrift*
- **Qwen3.5-2B** ✓: The meaning of the proverb is:
- **Sarvam-1** ✓: This means that if you give someone a chance to do something, they will probably not be able to do it very well or at all. It is like giving a snake its freedom and expecting it to fly! [/INST]

## 76. ಚಿಂತೆ ಇಲ್ಲದವನಿಗೆ ಸಂತೆಯಲ್ಲೂ ನಿದ್ರೆ  (figurative)
*EN: One without worries sleeps even in the marketplace*

- **Gold:** ಯಾವ ಚಿಂತೆಯೂ ಇಲ್ಲದವನಿಗೆ ಎಂಥ ಗದ್ದಲದ ಸ್ಥಳದಲ್ಲೂ ನೆಮ್ಮದಿಯ ನಿದ್ರೆ ಬರುತ್ತದೆ ಎಂದು ಅರ್ಥ.
  - *EN: One who has no worry at all sleeps peacefully even in the noisiest place.*
- **mT0-large** ✓: ಶಾಂತಿಪಾಲಕನಿಗೆ ಸಂತೆಯಲ್ಲೂ ನಿದ್ರೆಯ ಸಮಯ
  - *EN: For the peacekeeper, it is sleep time even in the market*
- **Qwen3.5-2B** ✓: The meaning of the proverb is:
- **Sarvam-1** ✓: This means that if you are not worried about anything, then you will be able to sleep well at night.

## 77. ದಾನಕ್ಕಿಂತ ನಿಧಾನ ದೊಡ್ಡದು  (literal)
*EN: Patience is greater than charity*

- **Gold:** ದಾನ ಕೊಡುವುದಕ್ಕಿಂತಲೂ ತಾಳ್ಮೆ ಮತ್ತು ಸಮಾಧಾನದಿಂದ ಇರುವುದು ದೊಡ್ಡ ಗುಣ ಎಂಬ ಅರ್ಥ ಇರಬಹುದು.
  - *EN: It may mean that patience and calmness are a greater virtue than giving charity.*
- **mT0-large** ✗: ದಾನಕ್ಕಿಂತ ನಿಧಾನವಾಗಿ
  - *EN: Slower than charity*
- **Qwen3.5-2B** ✓: The proverb means that giving money is more important than being slow, implying that speed is more valuable than wealth.
- **Sarvam-1** ✓: This means that giving money or other things to someone is better than just expecting something back from them, because it shows you care about their well-being and want to help them without any strings attached. </s>

## 78. ದಿಕ್ಕು ದಿಕ್ಕಿಗೆ ಹೋದರೂ ದುಃಖ ತಪ್ಪದು  (literal)
*EN: Wherever you go, in whichever direction, sorrow doesn't go away*

- **Gold:** ಎಲ್ಲಿಗೆ ಹೋದರೂ ಕಷ್ಟ-ದುಃಖಗಳಿಂದ ತಪ್ಪಿಸಿಕೊಳ್ಳಲಾಗದು, ಅವನ್ನು ಎದುರಿಸಬೇಕು.
  - *EN: Wherever one goes, one cannot escape hardships and sorrows; they must be faced.*
- **mT0-large** ✓: ದಿಕ್ಕು ದಿಕ್ಕಕ್ಕೆ ಹೋದರೆ ದುಃಖ ತಪ್ಪುವುದಿಲ್ಲ
  - *EN: If you go from direction to direction, sorrow does not escape you*
- **Qwen3.5-2B** ✓: The proverb means that no matter how far one travels or goes in any direction, they will inevitably encounter sorrow or misfortune.
- **Sarvam-1** ✓: This means that no matter how hard you try to avoid something, it will still happen eventually. It's like trying to stop a river from flowing - you can't do it! The phrase is often used when someone tries to change their behavior but finds out later that they weren'

## 79. ದುಡ್ಡೇ ದೊಡ್ಡಪ್ಪ  (literal)
*EN: Money is the big uncle (money is supreme)*

- **Gold:** ಜಗತ್ತಿನಲ್ಲಿ ಹಣಕ್ಕೇ ಹೆಚ್ಚು ಬೆಲೆ ಮತ್ತು ಮರ್ಯಾದೆ, ಹಣ ಇದ್ದವನನ್ನು ಎಲ್ಲರೂ ಗೌರವಿಸುತ್ತಾರೆ ಎಂದು ಅರ್ಥ.
  - *EN: In the world money carries the most value and respect; everyone honors one who has money.*
- **mT0-large** ✓: The wealthy are a great father.
- **Qwen3.5-2B** ✗: ದುಡ್ಡೇ ದೊಡ್ಡಪ್ಪ
- **Sarvam-1** ✓: This means that money is a big problem for most people, and it can be very difficult to get rid of. It's like having an old grandfather who always wants more things, even if you have enough already.

## 80. ದೇವರು ವರ ಕೊಟ್ಟರೂ ಪೂಜಾರಿ ವರ ಕೊಡ  (figurative)
*EN: Even if the god gives a boon, the priest won't*

- **Gold:** ಮೇಲಿನವರು ಮಂಜೂರು ಮಾಡಿದರೂ ಮಧ್ಯದಲ್ಲಿರುವ ಅಧಿಕಾರಿ ಅಥವಾ ಮಧ್ಯವರ್ತಿ ಅಡ್ಡಿ ಮಾಡಿ ಕೆಲಸ ಆಗದಂತೆ ತಡೆಯುತ್ತಾನೆ ಎಂದು ಅರ್ಥ.
  - *EN: Even if the higher-ups sanction it, the officer or middleman in between creates obstacles and prevents the work from being done.*
- **mT0-large** ✗: 'దేవుడు కూడా 'భూమి' అని 'భూమి' అని 'భూమి' అని 'భూమి' అని 'భూమి' అని 'భూమి' అని 'భూమి' అని 'భూమి' అని 'భూమి' అని
  - *EN: [Telugu] 'Even God says 'earth', 'earth', 'earth', 'earth'...' (repetitive)*
- **Qwen3.5-2B** ✓: ದೇವರು ವರ ಕೊಟ್ಟರೂ ಪೂಜಾರಿ ವರ ಕೊಡ
- **Sarvam-1** ✓: This means that even if you have something good, like a blessing from God, it is still up to you how you use it and what you do with it. If you don't use your blessings wisely or make bad choices, then they won't be as helpful as they

## 81. ದೂರದ ಬೆಟ್ಟ ಕಣ್ಣಿಗೆ ನುಣ್ಣಗೆ  (figurative)
*EN: The distant hill looks smooth to the eye*

- **Gold:** ದೂರದಲ್ಲಿರುವ ವಸ್ತು ಅಥವಾ ಸ್ಥಳ ಚೆನ್ನಾಗಿ ಕಾಣುತ್ತದೆ, ಹತ್ತಿರ ಹೋದಾಗಲೇ ಅದರ ಕಷ್ಟ ಗೊತ್ತಾಗುತ್ತದೆ ಎಂದು ಅರ್ಥ.
  - *EN: A distant object or place looks good; its hardships are known only when one goes near.*
- **mT0-large** ✓: தூரದ ಬೆಟ್ಟ ಕಣ್ಣಿಗೆ ನುಣ್ಣಗೆ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ದೂರದ ಬೆಟ್ಟ ಕಣ್ಣಿಗೆ ನುಣ್ಣಗೆ
- **Sarvam-1** ✓: This means that something is hard to see or understand when it's far away, but if you get closer, it becomes clearer and easier to understand. </s>

## 82. ಧರ್ಮಕ್ಕೆ ದತ್ತಿ ಕೊಟ್ಟರೆ ಹಿತ್ತಲಿಗೆ ಹೋಗಿ ಮೊಳ ಹಾಕಿದರು  (figurative)
*EN: When given as charity for dharma, they went to the backyard and measured it by the cubit*

- **Gold:** ಉಚಿತವಾಗಿ ಕೊಟ್ಟದ್ದನ್ನೂ ಕೃತಜ್ಞತೆ ಇಲ್ಲದೆ ಅಳೆದು ಕುಂದು ಹುಡುಕುವ ಸ್ವಭಾವದವರನ್ನು ಹೇಳುವ ಮಾತು ಇರಬಹುದು.
  - *EN: It may refer to people who ungratefully measure and find fault even with what was given for free.*
- **mT0-large** ✗: ದತ್ತಿ వేయడం కోసం ಹಿತ್ತಲಿಗೆ ಹೋಗಿ ಮೊಳ ಹಾಕಿದರು
  - *EN: [Kannada+Telugu mix] To give a donation, they went to the backyard and measured by cubits*
- **Qwen3.5-2B** ✓: ಧರ್ಮಕ್ಕೆ ದತ್ತಿ ಕೊಟ್ಟರೆ ಹಿತ್ತಲಿಗೆ ಹೋಗಿ ಮೊಳ ಹಾಕಿದರು
- **Sarvam-1** ✓: This means that if you give money to a charity, it will not make much difference because there are many other people who need help too. It is like planting seeds in your backyard - they may grow into something big or small depending on how well they are cared for and nurtured

## 83. ಎಲ್ಲರೂ ಮಾಡುವುದು ಹೊಟ್ಟೆಗಾಗಿ, ಗೇಣು ಬಟ್ಟೆಗಾಗಿ  (literal)
*EN: Everyone does it for the belly, for a span of cloth*

- **Gold:** ಎಲ್ಲರೂ ದುಡಿಯುವುದು ಹೊಟ್ಟೆ ಮತ್ತು ಬಟ್ಟೆಗಾಗಿ, ಅಂದರೆ ಜೀವನೋಪಾಯಕ್ಕಾಗಿಯೇ ಎಂದು ಅರ್ಥ.
  - *EN: Everyone works for food and clothing, that is, for a livelihood.*
- **mT0-large** ✓: All people do things for their bodies.
- **Qwen3.5-2B** ✗: All people do it for their stomach, for their clothes.
- **Sarvam-1** ✓: This means that people do things for their own benefit and not because they want to help others or be kind.

## 84. ಎಲ್ಲಾ ಬೆಳಕು ಬೆಳಕಲ್ಲ ಸತ್ಯದ ನುಡಿಯೇ ಬೆಳಕು  (figurative)
*EN: Not all light is light; the word of truth is the light*

- **Gold:** ಹೊಳಪು ಮತ್ತು ಆಡಂಬರವೆಲ್ಲ ನಿಜವಾದ ದಾರಿ ತೋರಿಸುವುದಿಲ್ಲ, ಸತ್ಯವಾದ ಮಾತೇ ನಿಜವಾದ ಬೆಳಕು ಎಂದು ಅರ್ಥ.
  - *EN: Glitter and show don't point the true path; truthful speech is the real light.*
- **mT0-large** ✓: ಜಗತ್ತಿನ ಎಲ್ಲಾ ಬೆಳಕು ಬೆಳಕು
  - *EN: All the light of the world is light*
- **Qwen3.5-2B** ✓: All light is not light, the truth is the light.
- **Sarvam-1** ✓: This means that not all light is good or true, and some people may use their own lights to deceive others.

## 85. ಎಡದ ನೆತ್ತಿಗೆ ಬಡಿದರೆ ಬಲದ ನೆತ್ತಿಗೆ ತಾಕಿತು  (figurative)
*EN: If it hits the left crown of the head, it touched the right crown*

- **Gold:** ಅರ್ಥ ಸ್ಪಷ್ಟವಿಲ್ಲ; ಒಬ್ಬರಿಗೆ ಮಾಡಿದ ಕ್ರಿಯೆ ಅಥವಾ ಹೇಳಿದ ಮಾತು ಇನ್ನೊಬ್ಬರಿಗೆ ತಟ್ಟಿ ಅವರ ಮೇಲೆ ಪರಿಣಾಮ ಬೀರುವುದು ಎಂದು ಇರಬಹುದು.
  - *EN: The meaning is unclear; it may be that an action or word directed at one person touches another and affects them.*
- **mT0-large** ✓: ನೆತ್ತಿಗೆ ಬಡಿದರೆ ಬಲದ ನೆತ್ತಿಗೆ ತಾಕಿತು
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: The proverb means that if you are weak and defeated, you will be defeated by the strong, but if you are strong and victorious, you will be victorious by the strong.
- **Sarvam-1** ✓: This means that if you do something wrong, it will come back to haunt you later on. It is a warning against making mistakes and not learning from them. </s>

## 86. ಎಡವಿದ ಕಾಲು ಎಡವುದು ಹೆಚ್ಚು  (figurative)
*EN: A foot that has stumbled stumbles more*

- **Gold:** ಒಮ್ಮೆ ಅಪಘಾತ ಅಥವಾ ಕಷ್ಟಕ್ಕೆ ಸಿಲುಕಿದವನು ಮತ್ತೆ ಮತ್ತೆ ಅದೇ ತೊಂದರೆಗೆ ಸಿಲುಕುವ ಸಾಧ್ಯತೆ ಹೆಚ್ಚು ಎಂದು ಇದರ ಅರ್ಥ.
  - *EN: One who has once met with an accident or trouble is more likely to meet the same trouble again and again.*
- **mT0-large** ✗: a broken foot is a very weak
- **Qwen3.5-2B** ✓: The meaning of the proverb is that the person who is the most vulnerable to the pain of the injury is the one who is most likely to suffer from the pain of the injury.
- **Sarvam-1** ✓: This means that if you make a mistake, it is better to correct it than to keep making mistakes and getting worse. [/INST]

## 87. ಎಂಟು ವರ್ಷಕ್ಕೆ ನನ್ನ ಮಗ ದಂಟಾದ  (figurative)
*EN: At eight years, my son turned into a stalk*

- **Gold:** ಚಿಕ್ಕ ವಯಸ್ಸಿನಲ್ಲೇ ಮಗ ಯಾವ ಪ್ರಯೋಜನಕ್ಕೂ ಬಾರದ, ಹೇಳಿದ ಮಾತು ಕೇಳದ ಸ್ಥಿತಿಗೆ ಬಂದ ಎಂದು ಪೋಷಕರು ಬೇಸರಪಡುವ ಮಾತು ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: It seems to be a parent's lament that at a young age the son has become good for nothing and doesn't listen to what he's told.*
- **mT0-large** ✗: ತನ್ನ ಮಗನು ಎಂಟು ವರ್ಷలకు చేరాడు.
  - *EN: [Kannada+Telugu mix] His son reached eight years.*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that if you do something for a long time, it will become part of your life and be difficult to change or stop doing it.

## 88. ಎಂತೆಂಥ ದೇವರಿಗೆ ಅಂತರಾಟ ಆಗಿರುವಾಗ ಕಾಲುಮುರುಕ ದೇವರಿಗೆ ಕೈಲಾಸವೇ!  (figurative)
*EN: When even such gods are in distress, will a leg-broken god get Kailasa?*

- **Gold:** ದೊಡ್ಡ ದೇವರುಗಳಿಗೇ ಕಷ್ಟವಾಗಿರುವಾಗ ಕುಂಟ ದೇವರಿಗೆ ಕೈಲಾಸ ಸಿಗುವುದುಂಟೇ ಎಂದರೆ, ಬಲಿಷ್ಠರಿಗೇ ಕಷ್ಟವಿರುವಾಗ ದುರ್ಬಲರಿಗೆ ಸುಖ ಸಿಗುವುದು ಕಷ್ಟ ಎಂದು ಅರ್ಥ.
  - *EN: When even great gods are in difficulty, would a lame god get Kailasa? That is, when even the mighty face hardship, it is hard for the weak to get happiness.*
- **mT0-large** ✓: ಪಾದಮುರುಕ ದೇವರಿಗೆ ಕೈಲಾಸವೇ!
  - *EN: For a broken-footed god, Kailasa (heaven) itself!*
- **Qwen3.5-2B** ✓: Proverb: ಎಂತೆಂಥ ದೇವರಿಗೆ ಅಂತರಾಟ ಆಗಿರುವಾಗ ಕಾಲುಮುರುಕ ದೇವರಿಗೆ ಕೈಲಾಸವೇ!
- **Sarvam-1** ✗: This means that when you are so busy with something else, then it is impossible to do anything about your problems or issues. It's like trying to build a house on top of an elephant - it just doesn't work. You need to focus on what really matters first before worrying

## 89. ಎಲ್ಲಾ ಬಣ್ಣ ಮಸಿ ನುಂಗಿತು  (figurative)
*EN: All the colors were swallowed by the soot*

- **Gold:** ಒಂದು ಕಪ್ಪು ಮಸಿ ಎಲ್ಲಾ ಬಣ್ಣಗಳನ್ನು ಮುಚ್ಚಿಬಿಡುವಂತೆ, ಒಂದು ದೊಡ್ಡ ತಪ್ಪು ಅಥವಾ ಕೆಟ್ಟ ವಿಷಯ ಉಳಿದ ಎಲ್ಲ ಒಳ್ಳೆಯದನ್ನೂ ಮರೆಮಾಡುತ್ತದೆ.
  - *EN: Just as one black smudge covers all colors, one big mistake or bad thing hides all the rest of the good.*
- **mT0-large** ✓: All colours were mixed
- **Qwen3.5-2B** ✓: All colors were eaten.
- **Sarvam-1** ✓: This means that if you try to do too much, or take on more than you can handle, then it will all come crashing down around you. It's like trying to drink a whole gallon of water when you only need half a glass. You might be able to hold your head

## 90. ಎಲ್ಲರೂ ಪಾಲಕಿಯಲ್ಲಿ ಕುತರೆ ಹೊರೋರು ಯಾರು  (figurative)
*EN: If everyone sits in the palanquin, who will carry it?*

- **Gold:** ಎಲ್ಲರೂ ಪಲ್ಲಕ್ಕಿಯಲ್ಲಿ ಕುಳಿತುಕೊಂಡರೆ ಅದನ್ನು ಹೊರುವವರು ಯಾರು ಎಂದರೆ, ಎಲ್ಲರೂ ಯಜಮಾನರಾಗಲು ಬಯಸಿದರೆ ಕೆಲಸ ಮಾಡುವವರು ಯಾರು ಎಂದು ಅರ್ಥ.
  - *EN: If everyone sits in the palanquin, who carries it? That is, if everyone wants to be the boss, who will do the work?*
- **mT0-large** ✗: ಎಲ್ಲರೂ ಪಾಲಕಿಯಲ್ಲಿ ಕುತರೇ ಹೊರನೋರು ఎవరు?
  - *EN: [Kannada+Telugu mix] If everyone sits in the palanquin, who will carry it?*
- **Qwen3.5-2B** ✓: All people are like a pot of water, and they are all in a state of being a pot of water.
- **Sarvam-1** ✓: Everyone who is trying to be a good parent will eventually fail, because no matter how hard you try, there are always things that can go wrong.

## 91. ಎರಡು ಕೈ ತಟ್ಟಿದರೆ ಸದ್ದು  (figurative)
*EN: When two hands clap, there's a sound*

- **Gold:** ಚಪ್ಪಾಳೆಗೆ ಎರಡು ಕೈ ಬೇಕು; ಹಾಗೆಯೇ ಜಗಳ ಅಥವಾ ಸಮಸ್ಯೆಗೆ ಇಬ್ಬರ ಪಾತ್ರವೂ ಇರುತ್ತದೆ, ಒಬ್ಬರೇ ಕಾರಣರಲ್ಲ.
  - *EN: Clapping needs two hands; likewise a quarrel or problem involves both persons; one alone is not the cause.*
- **mT0-large** ✓: Two hands touching each other.
- **Qwen3.5-2B** ✓: ಎರಡು ಕೈ ತಟ್ಟಿದರೆ ಸದ್ದು
- **Sarvam-1** ✓: If you do something twice, it is usually better than doing it once. [/INST]

## 92. ಎರಡು ದಾಸರ ನಂಬಿ ಕುರುಡು ದಾಸ ಕೆಟ್ಟ  (figurative)
*EN: Trusting two Dasas, the blind Dasa was ruined*

- **Gold:** ಇಬ್ಬರು ದಾಸರನ್ನು ನಂಬಿದ ಕುರುಡು ದಾಸ ಕೆಟ್ಟ ಎಂದರೆ, ಇಬ್ಬರ ಮೇಲೆ ಅವಲಂಬಿಸಿದರೆ ಪ್ರತಿಯೊಬ್ಬರೂ ಇನ್ನೊಬ್ಬರು ನೋಡಿಕೊಳ್ಳುತ್ತಾರೆ ಎಂದು ನಿರ್ಲಕ್ಷ್ಯ ಮಾಡಿ ನಂಬಿದವನಿಗೆ ನಷ್ಟವಾಗುತ್ತದೆ.
  - *EN: 'The blind Dasa who trusted two Dasas was ruined' means that if you rely on two people, each neglects the task thinking the other will see to it, and the one who trusted suffers the loss.*
- **mT0-large** ✗: ಎರಡು ದಾಸರ ನಂಬಿ ಕುರುಡು ದಾಸ ಕೆಟ್ಟ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that if you rely on two people to do something for you, then you will end up with a bad result because they may not be able to do it properly or at all.

## 93. ಏರಿದವ ಇಳಿದಾನು  (figurative)
*EN: One who has climbed will come down*

- **Gold:** ಎತ್ತರಕ್ಕೆ ಏರಿದವನು ಒಂದು ದಿನ ಕೆಳಗೆ ಇಳಿಯಲೇಬೇಕು; ಅಂದರೆ ಅಧಿಕಾರ ಅಥವಾ ಸಂಪತ್ತು ಶಾಶ್ವತವಲ್ಲ.
  - *EN: One who has risen high must come down one day; that is, power or wealth is not permanent.*
- **mT0-large** ✗: climber rises
- **Qwen3.5-2B** ✓: ಏರಿದವ ಇಳಿದಾನು
- **Sarvam-1** ✓: This means that people who are successful or have achieved something will eventually face failure and difficulties, but they can learn from their mistakes and try again to succeed.

## 94. ಗಂಡ ಹೆಂಡಿರ ಜಗಳ ಉಂಡು ಮಲಗುವ ತನಕ  (literal)
*EN: A husband-and-wife quarrel lasts only until they've eaten and gone to sleep*

- **Gold:** ಗಂಡ ಹೆಂಡತಿಯ ಜಗಳ ಊಟ ಮಾಡಿ ಮಲಗುವ ವೇಳೆಗೆ ಮುಗಿದುಹೋಗುತ್ತದೆ, ಅದು ಹೆಚ್ಚು ಕಾಲ ಉಳಿಯುವುದಿಲ್ಲ.
  - *EN: A husband-and-wife quarrel ends by the time they have eaten and gone to bed; it doesn't last long.*
- **mT0-large** ✗: మగవారి మధ్య చీలికలు, చీలికలు, చీలికలు, చీలికలు, చీలికలు, చీలికలు, చీలికలు, చీలికలు, చీలికలు, చీలికలు, చీలికలు,
  - *EN: [Telugu] Splits among men, splits, splits, splits... (repetitive)*
- **Qwen3.5-2B** ✗: The proverb means that a marriage is a source of conflict and discord, and it is only when the couple has successfully overcome their arguments and resolved their differences that they can truly rest and find peace.
- **Sarvam-1** ✓: This means that when a couple is fighting, they should stop and try to resolve their differences before going to bed.

## 95. ಗೆದ್ದೆತ್ತಿನ ಬಾಲ ಹಿಡಿದ ಹಾಗೆ  (figurative)
*EN: Like holding the tail of the winning ox*

- **Gold:** ಗೆದ್ದ ಎತ್ತಿನ ಬಾಲ ಹಿಡಿದುಕೊಂಡು ಹೋಗುವಂತೆ, ಯಶಸ್ವಿಯಾದವರ ಹಿಂದೆ ಸೇರಿಕೊಂಡು ತಾನೂ ಲಾಭ ಪಡೆಯುವ ಅವಕಾಶವಾದದ ಸ್ವಭಾವ.
  - *EN: Like holding on to the tail of the winning ox, an opportunistic nature of joining those who have succeeded and profiting oneself.*
- **mT0-large** ✓: ಗೆದ್ದೆತ್ತಿನ ಬಾಲ ಹಿಡಿದ ಹಾಗೆ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: The meaning of the proverb is:
- **Sarvam-1** ✗: This means that if you try to do something difficult, it will be hard for you and you may fail. But if you give up easily, then you won't have a chance to succeed at all.

## 96. ಗುಬ್ಬಿ ಮೇಲೆ ಬ್ರಹ್ಮಾಸ್ತ್ರವೇ?  (figurative)
*EN: A Brahmastra on a sparrow?*

- **Gold:** ಗುಬ್ಬಚ್ಚಿಯನ್ನು ಕೊಲ್ಲಲು ಬ್ರಹ್ಮಾಸ್ತ್ರ ಬಳಸುವುದು ಅತಿರೇಕ; ಅಂದರೆ ಸಣ್ಣ ವಿಷಯಕ್ಕೆ ಅತಿ ದೊಡ್ಡ ಕ್ರಮ ತೆಗೆದುಕೊಳ್ಳುವುದು ಸರಿಯಲ್ಲ.
  - *EN: Using the Brahmastra to kill a sparrow is excessive; that is, it is not right to take a very big step for a small matter.*
- **mT0-large** ✗: ಬ್ರಹ್ಮಾಂಡದ ಮೇಲೆ ಗುಬ್ಬಿ ಬಿದ್ದಿದೆ.
  - *EN: A sparrow has fallen on the universe. (nonsensical)*
- **Qwen3.5-2B** ✓: The proverb asks whether the power of the Supreme Being (Brahma) is sufficient to defeat the evil demon (Gubbi) or if the demon's strength is too great for even the highest spiritual power to overcome.
- **Sarvam-1** ✓: This means that if you are too proud to admit your mistakes, then you will be punished by them.

## 97. ಗಾಳಿ ಬಂದಾಗ ತೂರಿಕೋ, ಧಾರಣೆ ಬಂದಾಗ ಮಾರಿಕೋ  (figurative)
*EN: Winnow when the wind comes, sell when the price comes*

- **Gold:** ಗಾಳಿ ಬೀಸುವಾಗಲೇ ಧಾನ್ಯ ತೂರಿಕೊಳ್ಳಬೇಕು, ಬೆಲೆ ಚೆನ್ನಾಗಿರುವಾಗಲೇ ಮಾರಬೇಕು; ಅಂದರೆ ಅವಕಾಶ ಬಂದಾಗ ತಕ್ಷಣ ಬಳಸಿಕೊಳ್ಳಬೇಕು.
  - *EN: One must winnow grain only while the wind blows and sell when the price is good; that is, use an opportunity at once when it comes.*
- **mT0-large** ✓: ಧಾರಣೆ ಬಂದಾಗ ಮಾರಿಕೋ
  - *EN: Sell when the price comes*
- **Qwen3.5-2B** ✓: ಗಾಳಿ ಬಂದಾಗ ತೂರಿಕೋ, ಧಾರಣೆ ಬಂದಾಗ ಮಾರಿಕೋ
- **Sarvam-1** ✓: This means that when you are going through a difficult time or something bad is happening to you, it's best to take things easy and not try too hard because then your problems will get worse. But if good things happen to you, don't be afraid to celebrate them!

## 98. ಗವುಜಿ ಗದ್ದಲ ಏನೂ ಇಲ್ಲ, ಗೋವಿಂದ ಭಟ್ಟ ಬಾವಿಯಲ್ಲಿ ಬಿದ್ದ  (figurative)
*EN: No fuss or noise at all, Govinda Bhatta fell into the well*

- **Gold:** ಯಾವ ಗದ್ದಲ ಗೊಂದಲವೂ ಇಲ್ಲದೆ, ಯಾವ ಸೂಚನೆಯೂ ಇಲ್ಲದೆ ಅನಿರೀಕ್ಷಿತವಾಗಿ ಒಂದು ಘಟನೆ ನಡೆದುಹೋಗುವುದನ್ನು ಈ ಮಾತು ಹೇಳುತ್ತದೆ.
  - *EN: This saying describes an event that happens unexpectedly, without any fuss or confusion and without any warning.*
- **mT0-large** ✓: బొగ్గు మీద నుంచి వచ్చిన బొగ్గు మీద నుంచి వచ్చిన బొగ్గు మీద నుంచి వచ్చిన బొగ్గు మీద నుంచి వచ్చిన బొగ్గు మీద నుంచి వచ్చిన బొగ్గు మీద నుంచి వచ్చిన బొగ్గు మీద
  - *EN: [Telugu] Coming from on the coal, coming from on the coal... (repetitive)*
- **Qwen3.5-2B** ✓: The proverb is a humorous and satirical statement about the situation of the protagonist.
- **Sarvam-1** ✓: This means that if you don't make a fuss about something or someone, they won't bother you.

## 99. ಹೆಸರಿಗೆ ಹೆಂಡತಿ ಕಾಣೆ ಮಗನ ಹೆಸರು ನಂಜುಂಡ  (figurative)
*EN: In name the wife is missing, the son's name is Nanjunda*

- **Gold:** ಹೆಸರಿಗೆ ಮಾತ್ರ ಒಂದು ಸಂಬಂಧ ಅಥವಾ ಸ್ಥಾನ ಇದೆ, ವಾಸ್ತವದಲ್ಲಿ ಏನೂ ಇಲ್ಲ ಎಂಬ ಬರೀ ಹೆಸರಿನ ಆಡಂಬರವನ್ನು ಹೇಳುವ ಮಾತು ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: It seems to be a saying about empty show of name only: a relationship or position exists only in name, with nothing in reality.*
- **mT0-large** ✓: ಮಗುವಿನ ಹೆಸರು ನಂಜುಂಡ
  - *EN: The child's name is Nanjunda*
- **Qwen3.5-2B** ✓: ಹೆಸರಿಗೆ ಹೆಂಡತಿ ಕಾಣೆ ಮಗನ ಹೆಸರು ನಂಜುಂಡ
- **Sarvam-1** ✓: This means that a person's name is not always what it seems to be, and sometimes people are misled by appearances or assumptions about someone based on their name alone.

## 100. ಹೋದ್ಯಾ ಪಿಶಾಚಿ ಅಂದರೆ ಬಂದೆ ಗವಾಕ್ಷಿಲಿ ಅಂತಂತೆ  (figurative)
*EN: When told 'Gone, ghost?', it said 'I came back through the window'*

- **Gold:** ಹೋದೆಯಾ ಪಿಶಾಚಿ' ಎಂದರೆ 'ಗವಾಕ್ಷಿಯಲ್ಲಿ ಬಂದೆ' ಎಂದಂತೆ; ಕಿರಿಕಿರಿ ಕೊಡುವವರನ್ನು ಓಡಿಸಿದರೂ ಬೇರೆ ದಾರಿಯಿಂದ ಮತ್ತೆ ಬರುತ್ತಾರೆ.
  - *EN: Like saying 'I came through the window' when told 'Have you gone, ghost?'; even if you drive off nuisances, they come back by another route.*
- **mT0-large** ✗: ಹೋದ್ಯಾ ಪಿಶೋಚಿ అంటే వచ్చిన ಗವಾಕ್ಷಿಲಿ
  - *EN: [Kannada+Telugu mix] 'Gone, you demon' means the window that came (nonsensical)*
- **Qwen3.5-2B** ✓: ಹೋದ್ಯಾ ಪಿಶಾಚಿ ಅಂದರೆ ಬಂದೆ ಗವಾಕ್ಷಿಲಿ ಅಂತಂತೆ
- **Sarvam-1** ✓: This means that if you do something wrong, then it is better to wait for a while before doing anything else about it. If you act too quickly without thinking things through, you might make more problems than solutions.

## 101. ಹಾಳೂರಿನಲ್ಲಿ ಉಳಿದವನೇ ಗೌಡ  (figurative)
*EN: In a ruined village, whoever remains is the headman (Gowda)*

- **Gold:** ಊರೇ ಹಾಳಾಗಿ ಯಾರೂ ಇಲ್ಲದಿದ್ದಾಗ ಉಳಿದುಕೊಂಡವನೇ ಗೌಡ (ಯಜಮಾನ) ಆಗುತ್ತಾನೆ; ಬೇರೆ ಯೋಗ್ಯರಿಲ್ಲದಿದ್ದಾಗ ಸಾಮಾನ್ಯನಿಗೂ ಮುಖ್ಯ ಸ್ಥಾನ ಸಿಗುತ್ತದೆ.
  - *EN: When a village is ruined and no one is left, whoever remains becomes the Gowda (headman); when no worthy people are left, even an ordinary person gets a main position.*
- **mT0-large** ✗: ಗೌಡನ ಮಗ
  - *EN: The village headman's (Gowda's) son*
- **Qwen3.5-2B** ✗: ಹಾಳೂರಿನಲ್ಲಿ ಉಳಿದವನೇ ಗೌಡ
- **Sarvam-1** ✓: This means that if you are not doing anything to help yourself, then others will take advantage of your situation and make a fool out of you.

## 102. ಹನಿ ಹನಿಗೂಡಿದರೆ ಹಳ್ಳ ತೆನೆಗೂಡಿದರೆ ಬತ್ತ  (figurative)
*EN: Drop by drop becomes a stream, ear by ear becomes paddy*

- **Gold:** ಹನಿಹನಿ ಸೇರಿ ಹಳ್ಳವಾಗುತ್ತದೆ, ತೆನೆತೆನೆ ಸೇರಿ ಭತ್ತದ ರಾಶಿಯಾಗುತ್ತದೆ; ಸಣ್ಣ ಸಣ್ಣ ಪ್ರಯತ್ನ ಅಥವಾ ಉಳಿತಾಯ ಸೇರಿ ದೊಡ್ಡದಾಗುತ್ತದೆ.
  - *EN: Drops join into a stream, ears of grain join into a heap of paddy; small efforts or savings add up into something big.*
- **mT0-large** ✓: The snake stood on the slope and stood on the slope.
- **Qwen3.5-2B** ✗: ಹನಿ ಹನಿಗೂಡಿದರೆ ಹಳ್ಳ ತೆನೆಗೂಡಿದರೆ ಬತ್ತ
- **Sarvam-1** ✓: This means that if you want something to happen, then make sure it is easy and simple for others to do as well. If they can't help but follow your lead, then you have a good chance of success. </s>

## 103. ಹಾಡಿದ್ದೆ ಹಾಡೋ ಕಿಸುಬಾಯಿ ದಾಸ  (figurative)
*EN: The wide-mouthed Dasa who sings the same song again and again*

- **Gold:** ಬಾಯಿ ಕಿಸಿದ ದಾಸ ಹಾಡಿದ ಹಾಡನ್ನೇ ಮತ್ತೆ ಮತ್ತೆ ಹಾಡುವಂತೆ, ಹೇಳಿದ್ದನ್ನೇ ಪದೇ ಪದೇ ಹೇಳುವ ಅಥವಾ ಮಾಡುವ ಬೇಸರದ ಅಭ್ಯಾಸ.
  - *EN: Like a grinning Dasa singing the song he already sang again and again; a boring habit of repeating or doing the same thing over and over.*
- **mT0-large** ✗: I'm a singer
- **Qwen3.5-2B** ✓: ಹಾಡಿದ್ದೆ ಹಾಡೋ ಕಿಸುಬಾಯಿ ದಾಸ
- **Sarvam-1** ✓: This is a very old saying that means to be careful with what you say or do because it can have serious consequences. It's like being careful when you cross a busy street, so you don't get hit by a car. The same idea applies here - if you speak carelessly

## 104. ಹೆತ್ತವರಿಗೆ ಹೆಗ್ಗಣ ಮುದ್ದು, ಕೂಡಿದವರಿಗೆ ಕೋಡಗ ಮುದ್ದು  (figurative)
*EN: To the parents the bandicoot is a darling, to the companions the monkey is a darling*

- **Gold:** ಹೆತ್ತವರಿಗೆ ತಮ್ಮ ಮಕ್ಕಳು ಹೇಗಿದ್ದರೂ ಮುದ್ದು ಎಂಬುದು ಮೊದಲ ಭಾಗದ ಅರ್ಥ; ಎರಡನೇ ಭಾಗ ಸ್ಪಷ್ಟವಿಲ್ಲ.
  - *EN: The first half means parents find their children dear however they are; the second half is unclear.*
- **mT0-large** ✓: The dogs are very shy and the dogs are very shy.
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that children should respect their parents and elders because they are responsible for them. They have to take care of them when they were young.

## 105. ಹಿರಿಯಣ್ಣನ ಚಾಳಿ ಮನೆ ಮಂದಿಗೆಲ್ಲಾ  (figurative)
*EN: The eldest brother's habit goes to everyone in the house*

- **Gold:** ಮನೆಯ ಹಿರಿಯ ಅಣ್ಣನ ಅಭ್ಯಾಸವನ್ನು ಮನೆಯ ಉಳಿದ ಎಲ್ಲರೂ ಅನುಕರಿಸುತ್ತಾರೆ; ಹಿರಿಯರ ನಡತೆ ಕಿರಿಯರ ಮೇಲೆ ಪರಿಣಾಮ ಬೀರುತ್ತದೆ.
  - *EN: Everyone else in the house imitates the habit of the eldest brother; elders' conduct affects the younger ones.*
- **mT0-large** ✗: ಹಿರಿಯಣ್ಣನ ಚಾಳಿ ಮನೆ ಮಂದಿಲ್ಲಾ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಹಿರಿಯಣ್ಣನ ಚಾಳಿ ಮನೆ ಮಂದಿಗೆಲ್ಲಾ
- **Sarvam-1** ✓: This means that people who are older than you will try to take advantage of your good nature and make things difficult for you.

## 106. ಹಿತ್ತಲ ಗಿಡ ಮದ್ದಲ್ಲ  (figurative)
*EN: A backyard plant is not medicine*

- **Gold:** ಮನೆಯ ಹಿತ್ತಲಲ್ಲಿರುವ ಗಿಡವನ್ನು ಔಷಧಿ ಎಂದು ಯಾರೂ ಪರಿಗಣಿಸುವುದಿಲ್ಲ; ಹತ್ತಿರದಲ್ಲಿರುವ ಪರಿಚಿತರ ಅಥವಾ ವಸ್ತುವಿನ ಮೌಲ್ಯ ಗೊತ್ತಾಗುವುದಿಲ್ಲ.
  - *EN: No one considers the plant in one's own backyard to be medicine; the value of nearby acquaintances or things isn't recognized.*
- **mT0-large** ✗: The trees are not a weapon.
- **Qwen3.5-2B** ✓: ಹಿತ್ತಲ ಗಿಡ ಮದ್ದಲ್ಲ
- **Sarvam-1** ✗: This means that you can't rely on something small or insignificant to solve a big problem, because it won't work. It is like trying to cure cancer with a tiny plant. The proverb comes from an old English saying which was used for hundreds of years before computers and

## 107. ಹೊಳೆ ನೀರಿಗೆ ದೊಣ್ಣೆ ನಾಯಕನ ಅಪ್ಪಣೆ ಯಾಕೆ?  (figurative)
*EN: Why the club-wielding chief's permission for river water?*

- **Gold:** ಎಲ್ಲರಿಗೂ ಸೇರಿದ ಹೊಳೆ ನೀರನ್ನು ಬಳಸಲು ಯಜಮಾನನ ಅನುಮತಿ ಬೇಕಿಲ್ಲ; ಎಲ್ಲರಿಗೂ ಮುಕ್ತವಾಗಿರುವ ವಿಷಯಕ್ಕೆ ಯಾರ ಅನುಮತಿಯೂ ಅನಗತ್ಯ.
  - *EN: To use river water that belongs to everyone, the headman's permission isn't needed; for what is open to all, no one's permission is necessary.*
- **mT0-large** ✗: ದೊಣ್ಣೆ ನಾಯಕನ ಅಪ್ಪಣೆ ಯಾಕೆಂದರೆ?
  - *EN: Why the permission of Donne Nayaka (the stick-wielding chief)?*
- **Qwen3.5-2B** ✓: ಹೊಳೆ ನೀರಿಗೆ ದೊಣ್ಣೆ ನಾಯಕನ ಅಪ್ಪಣೆ ಯಾಕೆ?
- **Sarvam-1** ✓: The proverb is a play on words, as "lead" can also mean to guide or direct someone towards something. It's saying that sometimes you need to be led by others, even if it means going against your own desires. </s>

## 108. ಹೊಸತರಲ್ಲಿ ಅಗಸ ಗೋಣಿ ಎತ್ತಿ ಎತ್ತಿ ಒಗೆದ  (figurative)
*EN: In the beginning the washerman lifted the sack again and again and beat it on the stone*

- **Gold:** ಹೊಸತರಲ್ಲಿ ಅಗಸ ಗೋಣಿಯನ್ನು ಎತ್ತಿ ಎತ್ತಿ ಒಗೆದಂತೆ, ಹೊಸ ಕೆಲಸದಲ್ಲಿ ಆರಂಭದಲ್ಲಿ ಅತಿಯಾದ ಉತ್ಸಾಹ ತೋರಿಸುವುದು, ಅದು ಹೆಚ್ಚು ಕಾಲ ಉಳಿಯುವುದಿಲ್ಲ.
  - *EN: As the washerman at first lifted and beat the sack again and again, one shows excessive enthusiasm at the start of a new task, which doesn't last long.*
- **mT0-large** ✓: ಹೊಸತರಲ್ಲಿ ಅಗಸ ಗೋಣಿ ಎತ್ತಿ ಎತ್ತಿ ಒಗೆದ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: ಹೊಸತರಲ್ಲಿ ಅಗಸ ಗೋಣಿ ಎತ್ತಿ ಎತ್ತಿ ಒಗೆದ
- **Sarvam-1** ✓: This means that you should not judge something or someone too quickly, because there is always more to it than meets the eye. </s>

## 109. ಹೊಸ ವೈದ್ಯನಿಗಿಂತ ಹಳೆ ರೋಗಿಯೇ ಮೇಲು  (figurative)
*EN: An old patient is better than a new doctor*

- **Gold:** ಅನುಭವಿ ಹಳೆಯ ರೋಗಿಗೆ ರೋಗದ ಬಗ್ಗೆ ಹೊಸದಾಗಿ ಬಂದ ವೈದ್ಯನಿಗಿಂತ ಹೆಚ್ಚು ತಿಳಿದಿರುತ್ತದೆ; ಅಂದರೆ ಅನುಭವ ಹೊಸ ಪುಸ್ತಕ ಜ್ಞಾನಕ್ಕಿಂತ ಮೇಲು.
  - *EN: An experienced old patient knows more about the disease than a newly arrived doctor; that is, experience is better than fresh book knowledge.*
- **mT0-large** ✓: ಹೊಸ ವೈದ್ಯನಿಗಿಂತ ಹಳೆಯ ರೋಗಿಯೇ ಮೇಲೆ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: ಹೊಸ ವೈದ್ಯನಿಗಿಂತ ಹಳೆ ರೋಗಿಯೇ ಮೇಲು
- **Sarvam-1** ✓: The proverb means that old people are often more experienced and knowledgeable than younger ones, so they can be better at their jobs or tasks. </s>

## 110. ಹೊಟ್ಟೆಗೆ ಹಿಟ್ಟಿಲ್ಲ ಜುಟ್ಟಿಗೆ ಮಲ್ಲಿಗೆ ಹೂವು  (figurative)
*EN: No flour for the belly, jasmine flowers for the hair knot*

- **Gold:** ತಿನ್ನಲು ಹಿಟ್ಟಿಲ್ಲದಿದ್ದರೂ ತಲೆಗೆ ಮಲ್ಲಿಗೆ ಹೂವು ಮುಡಿಯುವಂತೆ, ಮೂಲ ಅಗತ್ಯಕ್ಕೇ ಹಣವಿಲ್ಲದಿದ್ದರೂ ಆಡಂಬರಕ್ಕೆ ಖರ್ಚು ಮಾಡುವುದು.
  - *EN: Like wearing jasmine flowers on the head though there is no flour to eat; spending on show though there is no money even for basic needs.*
- **mT0-large** ✗: ಜುಟ್ಟಿಗೆ ಮಲ್ಲಿಗೆ ಹೂವು
  - *EN: Jasmine flower for the tuft of hair*
- **Qwen3.5-2B** ✗: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that you can't have everything, and if you try to do too much or get too many things at once, it will not work out well for you. It is like trying to plant a lot of flowers on your lawn without enough water or fertilizer - they won't grow

## 111. ಹುಟ್ಟಿಸಿದ ದೇವರು ಹುಲ್ಲು ಮೇಯಿಸುತ್ತಾನೆ  (figurative)
*EN: The god who gave birth will make you graze grass*

- **Gold:** ಹುಟ್ಟಿಸಿದ ದೇವರು ನಮ್ಮನ್ನು ಹುಲ್ಲು ಮೇಯಿಸಿ ಬದುಕಿಸುವುದಿಲ್ಲ; ಅಂದರೆ ಜೀವ ಕೊಟ್ಟವನು ಬದುಕಲು ದಾರಿಯನ್ನೂ ತೋರಿಸುತ್ತಾನೆ, ಹೆಚ್ಚು ಚಿಂತೆ ಬೇಡ.
  - *EN: The god who created us will not let us live by grazing grass; that is, the one who gave life also shows the way to live, so there is no need to worry too much.*
- **mT0-large** ✗: God is eating eggs.
- **Qwen3.5-2B** ✓: ಹುಟ್ಟಿಸಿದ ದೇವರು ಹುಲ್ಲು ಮೇಯಿಸುತ್ತಾನೆ
- **Sarvam-1** ✓: This means that God will not punish you for something you did when you were a child, but He may still be angry with you if you do bad things now.

## 112. ಹುಚ್ಚು ಮುಂಡೆ ಮದುವೆಯಲ್ಲಿ ಉಂಡವನೇ ಜಾಣ  (figurative)
*EN: At a mad widow's wedding, the one who ate is the clever one*

- **Gold:** ಗೊಂದಲದ ಹುಚ್ಚು ಮದುವೆಯಲ್ಲಿ ಊಟ ಮಾಡಿ ಹೋದವನೇ ಜಾಣ; ಅಂದರೆ ಅವ್ಯವಸ್ಥೆಯ ಸಂದರ್ಭದಲ್ಲಿ ತನಗೆ ಬೇಕಾದ ಲಾಭ ಪಡೆದುಕೊಂಡವನು ಬುದ್ಧಿವಂತ.
  - *EN: At a chaotic, crazy wedding, the one who ate and left is clever; that is, one who took the benefit he wanted in a disorderly situation is smart.*
- **mT0-large** ✓: ಹುಚ್ಚು ಮುಂಡೆ திருமணం కోసం సన్నాహాలు
  - *EN: [Kannada+Tamil+Telugu mix] Mad widow (insult) - preparations for a wedding*
- **Qwen3.5-2B** ✓: ಹುಚ್ಚು ಮುಂಡೆ ಮದುವೆಯಲ್ಲಿ ಉಂಡವನೇ ಜಾಣ
- **Sarvam-1** ✓: This means that someone who is not very smart can still get married, but they will have a hard time being successful because their partner won't be able to help them out with important things like money or work.

## 113. ಹೂವಿನ ಜೊತೆ ನಾರು ಸ್ವರ್ಗ ಸೇರಿತು  (figurative)
*EN: Along with the flower, the fiber reached heaven*

- **Gold:** ಹೂವಿನ ಜೊತೆ ಸೇರಿದ ನಾರು ಸಹ ದೇವರ ಪಾದ ಸೇರಿತು; ಒಳ್ಳೆಯವರ ಸಹವಾಸದಿಂದ ಸಾಮಾನ್ಯರಿಗೂ ಒಳ್ಳೆಯ ಫಲ ಸಿಗುತ್ತದೆ.
  - *EN: The fiber (thread) joined with the flower also reached the god's feet; through the company of good people, even ordinary ones get good results.*
- **mT0-large** ✓: ಚೆಂಡಿನ ಜೊತೆ ನಾರು ಸ್ವರ್ಗ ಸೇರಿಕೊಂಡಿದ್ದಾರೆ.
  - *EN: They have reached heaven along with the ball and fibre. (nonsensical)*
- **Qwen3.5-2B** ✓: ಹೂವಿನ ಜೊತೆ ನಾರು ಸ್ವರ್ಗ ಸೇರಿತು
- **Sarvam-1** ✗: ಈ proverb ನ ಅರ್ಥ ಏನಂದ್ರೆ, ಒಂದು ಸುಂದರವಾದ ಮತ್ತು ಅಮೂಲ್ಯವಾದ ವಸ್ತುವನ್ನು ಕಳೆದುಕೊಳ್ಳುವುದು ತುಂಬಾ ಕಷ್ಟ.

## 114. ಹಬ್ಬ ಹಸನಾಗಲಿ, ಗೋಡಿ ಜತನಾಗಲಿ, ಬಂದ ಬೀಗರು ಉಂಡು ಹೋಗಲಿ  (figurative)
*EN: Let the festival go well, let the wall be safe, let the visiting in-laws eat and go*

- **Gold:** ಹಬ್ಬ ಯಾವ ತೊಂದರೆಯೂ ಇಲ್ಲದೆ ಚೆನ್ನಾಗಿ ನಡೆಯಲಿ, ಮನೆಗೆ ಹಾನಿಯಾಗದಿರಲಿ, ಬಂದ ನೆಂಟರು ಊಟ ಮಾಡಿ ಸಂತೋಷವಾಗಿ ಹೋಗಲಿ ಎಂಬ ಹಾರೈಕೆ.
  - *EN: A wish that the festival go well without any trouble, that the house suffer no damage, and that the visiting relatives eat and leave happy.*
- **mT0-large** ✓: తమ ಊರಿನಲ್ಲಿ తమ ಊರಿನಲ್ಲಿ తమ ಊರಿನಲ್ಲಿ తమ ಊರಿನಲ್ಲಿ తమ ಊರಿನಲ್ಲಿ తమ ಊರಿನಲ್ಲಿ తమ ಊರಿನಲ್ಲಿ తమ ಊರಿನಲ್ಲಿ తమ ಊರಿನಲ್ಲಿ తమ ಊರಿನಲ್ಲಿ
  - *EN: [Telugu+Kannada mix] In their village, in their village, in their village... (repetitive)*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that if you are not careful about how things look or appear on the outside, then people will take advantage of your good nature and use it to their own ends.

## 115. ಇರುಳು ಚಿಂತೆ ನಿದ್ರೆಗೇಡು, ಹಗಲು ಚಿಂತೆ ಕೆಲಸಗೇಡು  (literal)
*EN: Worry at night ruins sleep, worry in the day ruins work*

- **Gold:** ರಾತ್ರಿ ಚಿಂತೆ ಮಾಡಿದರೆ ನಿದ್ರೆ ಹಾಳಾಗುತ್ತದೆ, ಹಗಲು ಚಿಂತೆ ಮಾಡಿದರೆ ಕೆಲಸ ಹಾಳಾಗುತ್ತದೆ.
  - *EN: If you worry at night, sleep is ruined; if you worry in the day, work is ruined.*
- **mT0-large** ✓: ರಾತ್ರಿಯಲ್ಲಿ ಕೆಲಸ ಮಾಡುವಾಗ, ಹಗಲು ಕೆಲಸ ಮಾಡುವಾಗ, ಇರುಳು ಚಿಂತೆ ನಿದ್ರೆಗೆಡು.
  - *EN: While working at night, while working by day, at night worry ruins sleep.*
- **Qwen3.5-2B** ✓: ಇರುಳು ಚಿಂತೆ ನಿದ್ರೆಗೇಡು, ಹಗಲು ಚಿಂತೆ ಕೆಲಸಗೇಡು
- **Sarvam-1** ✓: This means that worrying about things at night is a waste of time and energy because you will not be able to do anything about them when you wake up. It's better to deal with problems during the day so they can be solved. [/INST]

## 116. ಇದ್ದದ್ದು ಇದ್ದ ಹಾಗೆ ಹೇಳಿದರೆ ಸಿದ್ದಪ್ಪನಿಗೆ ಸಿಡಿಲು ಹೊಡೆಯಿತು  (figurative)
*EN: Say it as it is and thunder strikes Siddappa*

- **Gold:** ಇದ್ದದ್ದನ್ನು ಇದ್ದಂತೆ ಹೇಳಿದರೆ ಕೆಲವರಿಗೆ ಸಿಟ್ಟು ಬರುತ್ತದೆ; ನೇರ ಸತ್ಯ ಎಲ್ಲರಿಗೂ ಇಷ್ಟವಾಗುವುದಿಲ್ಲ.
  - *EN: Telling things as they are angers some people; the plain truth isn't liked by everyone.*
- **mT0-large** ✓: 'ಇದು ಇದ್ದದ್ದು ಇದ್ದಂತೆ' ಎಂದು ಸಿದ್ದಪ್ಪ ಹೇಳಿದರೆ, ಸಿಡಿಲು ಹೊಡೆಯಿತು.
  - *EN: If Siddappa says 'it is as it is', lightning struck.*
- **Qwen3.5-2B** ✓: ಇದ್ದದ್ದು ಇದ್ದ ಹಾಗೆ ಹೇಳಿದರೆ ಸಿದ್ದಪ್ಪನಿಗೆ ಸಿಡಿಲು ಹೊಡೆಯಿತು ಎಂಬ ಪ್ರಭಾವಕ ಪ್ರಾಥಮಿಕ ಅರ್ಥವೆಂದರೆ, "ಸಿದ್ದಪ್ಪ
- **Sarvam-1** ✓: ಈ proverb ನ ಅರ್ಥ ಏನಂದ್ರೆ, ನೀವು ಏನು ಹೇಳ್ತೀರ ಅಂತ ಅಲ್ಲ, ಹೇಗೆ ಹೇಳ್ತೀರ ಅನ್ನೋದು ಮುಖ್ಯ.

## 117. ಇರುಳು ಕಂಡ ಬಾವಿಯಲ್ಲಿ ಹಗಲು ಬಿದ್ದ ಹಾಗೆ  (figurative)
*EN: Like falling in the daytime into a well you saw at night*

- **Gold:** ರಾತ್ರಿ ಕಂಡಿದ್ದ ಬಾವಿಯಲ್ಲಿ ಹಗಲು ಬೀಳುವಂತೆ, ಅಪಾಯ ಅಥವಾ ತಪ್ಪು ಗೊತ್ತಿದ್ದೂ ಅದಕ್ಕೇ ಸಿಲುಕಿಕೊಳ್ಳುವ ಮೂರ್ಖತನ.
  - *EN: Like falling by day into a well one saw at night; the folly of getting caught in a danger or mistake despite knowing of it.*
- **mT0-large** ✗: ರಾತ್ರಿಯಲ್ಲಿ ಬಿದ್ದ ಹನಿಮಳೆ
  - *EN: Drizzle that fell in the night*
- **Qwen3.5-2B** ✓: The meaning of the proverb is:
- **Sarvam-1** ✓: ಈ proverb ಅಂದ್ರೆ, ಒಂದು situation ಅಲ್ಲಿ ನೀವು ತುಂಬಾ late ಆಗಿ action ತಗೊಂಡ್ರೆ, ಅದು ನಿಮ್ಮನ್ನ ಇನ್ನೂ worse situation ಗೆ ತಳ್ಳುತ್ತೆ ಅಂತ.

## 118. ಇಡಿ ಮುಳುಗಿದರೂ ಮೂಗು ಮೇಲೆ  (figurative)
*EN: Even if the whole body sinks, the nose stays up*

- **Gold:** ಇಡೀ ದೇಹ ನೀರಲ್ಲಿ ಮುಳುಗಿದರೂ ಮೂಗನ್ನು ಮೇಲೆತ್ತಿ ಹಿಡಿಯುವಂತೆ, ಸಂಪೂರ್ಣ ಹಾಳಾದರೂ ತನ್ನ ಜಂಭ, ಹೆಮ್ಮೆ ಬಿಡದಿರುವುದು.
  - *EN: Like holding the nose up even when the whole body sinks in water; not giving up one's arrogance and pride even when completely ruined.*
- **mT0-large** ✗: """ಇಡಿ ಮುಳುಗಿದರೂ ಮೂಗು ಮೇಲೆ""
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: ಇಡಿ ಮುಳುಗಿದರೂ ಮೂಗು ಮೇಲೆ
- **Sarvam-1** ✗: This means that even if something is not successful or has failed, you should still try to keep going and do your best. It's like trying to swim against a strong current - it might be difficult, but if you don't give up, you can eventually make progress. </s>

## 119. ಇಟ್ಟುಕೊಂಡಾಕಿ ಇರುತ್ತಾನಾ ಕಟ್ಟಿಕೊಂಡಾಕಿ ಕಡಿತಾನಾ  (figurative)
*EN: Will the one who was merely kept stay? Will the one who was wedded be cut off?*

- **Gold:** ತಾತ್ಕಾಲಿಕವಾಗಿ ಇಟ್ಟುಕೊಂಡವರು ಶಾಶ್ವತವಲ್ಲ, ಕಟ್ಟಿಕೊಂಡವರನ್ನು ಸುಲಭವಾಗಿ ಕೈಬಿಡಲಾಗದು ಎಂಬ ಅರ್ಥ ಇರಬಹುದು; ಆದರೆ ಪಠ್ಯದ ಲಿಂಗ ಮತ್ತು ಸ್ವರೂಪ ಸ್ಪಷ್ಟವಿಲ್ಲ.
  - *EN: It may mean that those kept temporarily are not permanent and those wedded cannot easily be abandoned; but the gender and form of the text are unclear.*
- **mT0-large** ✗: The container is kept in the fridge.
- **Qwen3.5-2B** ✓: ಇಟ್ಟುಕೊಂಡಾಕಿ ಇರುತ್ತಾನಾ ಕಟ್ಟಿಕೊಂಡಾಕಿ ಕಡಿತಾನಾ
- **Sarvam-1** ✓: This means that if you keep something to yourself, it will eventually be taken away from you. It is a warning against hoarding things and being greedy. [/INST]

## 120. ಇದ್ದ ಊರ ಸುದ್ದಿ ಇದ್ದಲ್ಲಿ ತೆಗೆಯಬಾರದು, ಹೋದ ಊರ ಸುದ್ದಿ ಹೋದಲ್ಲಿ ತೆಗೆಯಬಾರದು.  (figurative)
*EN: News of the town you are in shouldn't be raised where you are; news of the town you have left shouldn't be raised where you have gone*

- **Gold:** ಇರುವ ಊರಿನ ಸುದ್ದಿಯನ್ನು ಅಲ್ಲೇ ಹರಡಬಾರದು, ಬೇರೆ ಊರಿನ ಸುದ್ದಿಯನ್ನು ಹೋದ ಕಡೆ ಹೇಳಬಾರದು ಎಂದು ಹೇಳುವ ಮಾತು ಎಂದು ತೋರುತ್ತದೆ; ಪಠ್ಯ ಅಪೂರ್ಣವಾಗಿದೆ.
  - *EN: It seems to be a saying that news of the town where one lives shouldn't be spread there, and news of another town shouldn't be told where one has gone; the text is incomplete.*
- **mT0-large** ✗: ಊರ ಸುದ್ದಿ ಇದ್ದಲ್ಲಿ ತೆಗೆಯಬಾರದು, ಊರ ಸುದ್ದಿ ಹೋದಲ್ಲಿ ತೆಗೆಯಬಾರದು.
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಇದ್ದ ಊರ ಸುದ್ದಿ ಇದ್ದಲ್ಲಿ ತೆಗೆಯಬಾರದು, ಹೋದ ಊರ ಸುದ್ದಿ ಹೋದಲ್ಲಿ ತೆಗೆಯಬಾರದು.
- **Sarvam-1** ✓: This means that you shouldn't try to change or fix something that is already done well. If it has been successful and good, then don't try to make it worse by trying to improve it.

## 121. ಇದ್ದದ್ದು ಹೇಳಿದರೆ ಹದ್ದಿನಂತೆ ಮೊರೆ ಆಯಿತು  (figurative)
*EN: Said it as it was, and the face turned hawk-like*

- **Gold:** ಇದ್ದದ್ದನ್ನು ಇದ್ದಂತೆ ಹೇಳಿದರೆ ಕೇಳಿದವನು ಹದ್ದಿನಂತೆ ಸಿಟ್ಟಿನ ಮುಖ ಮಾಡುತ್ತಾನೆ; ಸತ್ಯ ಹೇಳಿದರೆ ಕೆಲವರಿಗೆ ಅಸಮಾಧಾನವಾಗುತ್ತದೆ.
  - *EN: When you say things as they are, the listener makes an angry, hawk-like face; telling the truth displeases some people.*
- **mT0-large** ✓: When you say something, you will be angry.
- **Qwen3.5-2B** ✓: ಇದ್ದದ್ದು ಹೇಳಿದರೆ ಹದ್ದಿನಂತೆ ಮೊರೆ ಆಯಿತು
- **Sarvam-1** ✗: This means that if you say something, people will believe it and take action to make sure it happens.

## 122. ಇದ್ದದ್ದು ಹೋಯಿತು ಮದ್ದಿನ ಗುಣದಿಂದ  (figurative)
*EN: What existed was lost through the medicine's effect*

- **Gold:** ಔಷಧಿಯ ಪರಿಣಾಮದಿಂದ ಇದ್ದ ಆರೋಗ್ಯವೂ ಹೋಯಿತು ಎಂದರೆ, ಸರಿಪಡಿಸಲು ಹೋದ ಪರಿಹಾರವೇ ಇದ್ದ ಒಳ್ಳೆಯದನ್ನೂ ಹಾಳು ಮಾಡಿತು.
  - *EN: Even the health one had was lost through the effect of the medicine; the remedy tried to fix things and ruined even the good that existed.*
- **mT0-large** ✓: 'ಅವನು 'ಮದ್ದಿನ ಗುಣದಿಂದ' 'ಅವನು 'ಮದ್ದಿನ ಗುಣದಿಂದ'
  - *EN: 'He 'by the quality of the medicine'' 'He 'by the quality of the medicine'' (repetitive, broken)*
- **Qwen3.5-2B** ✓: ಇದ್ದದ್ದು ಹೋಯಿತು ಮದ್ದಿನ ಗುಣದಿಂದ
- **Sarvam-1** ✓: This means that once something has happened, it cannot be changed or undone. It is like a curse - you can't get rid of what already happened.

## 123. ಇದ್ದಲ್ಲಿ ಗೌಡ ಹೋದಲ್ಲಿ ಕಿವುಡ  (figurative)
*EN: A headman (Gowda) where he is, deaf where he goes*

- **Gold:** ತನ್ನ ಜಾಗದಲ್ಲಿ ದೊಡ್ಡಸ್ತಿಕೆ ತೋರಿಸಿ, ಬೇರೆ ಕಡೆ ಹೋದರೆ ಮಾತೇ ಇಲ್ಲದಂತೆ ಸುಮ್ಮನಿರುವ ವ್ಯಕ್ತಿಯನ್ನು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb describes a person who acts big in his own place and stays silent, as if speechless, when he goes elsewhere.*
- **mT0-large** ✓: ಗೌಡರು ಇದ್ದಲ್ಲಿ ಗೌಡರು ಹೋದಲ್ಲಿ ಕಿವುಡ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಇದ್ದಲ್ಲಿ ಗೌಡ ಹೋದಲ್ಲಿ ಕಿವುಡ
- **Sarvam-1** ✓: If you are not willing to listen, then you will never learn anything new.

## 124. ಇಕ್ಕೇರಿ ತನಕ ಬಳಗ, ಮಾನ ಮುಚ್ಚಲಿಕ್ಕೆ ಅರಿವೆ ಇಲ್ಲ  (figurative)
*EN: Kin as far as Ikkeri, but no cloth to cover his shame*

- **Gold:** ಹೊರಗೆ ಊರೆಲ್ಲ ಹೆಸರು ಹರಡಿದ್ದರೂ ಒಳಗೆ ಮೂಲಭೂತ ಸೌಕರ್ಯವೂ ಇಲ್ಲದ ಸ್ಥಿತಿಯನ್ನು ಈ ಮಾತು ಸೂಚಿಸುತ್ತದೆ.
  - *EN: This saying suggests a state where one's name is spread all over town outside but inside there isn't even basic comfort.*
- **mT0-large** ✓: ಮಾನ ಮುಚ್ಚಲಿಕ್ಕೆ ಅರಿವಿಲ್ಲ
  - *EN: No cloth to cover one's shame (modesty)*
- **Qwen3.5-2B** ✓: The proverb is a metaphorical expression that conveys a specific message about human behavior and social dynamics. It suggests that when someone is in a state of distress or emotional turmoil, they may not be able to think clearly or make rational decisions. This is because their emotions take precedence over their logic and
- **Sarvam-1** ✓: This means that if you are too busy trying to get ahead or keep up with others, you will never have time for yourself and your own needs.

## 125. ಇಲಿ ಹೆಚ್ಚಿದವೆಂದು, ಮನೆಗೆ ಉರಿ ಇಡಬಾರದು  (figurative)
*EN: Don't set the house on fire because the rats have increased*

- **Gold:** ಸಣ್ಣ ತೊಂದರೆಗೆ ಹೆದರಿ ಇಡೀ ಮನೆಗೇ ಬೆಂಕಿ ಇಡುವಂತೆ ಅತಿರೇಕದ ಕ್ರಮ ತೆಗೆದುಕೊಳ್ಳಬಾರದು ಎಂದು ಈ ಮಾತು ಹೇಳುತ್ತದೆ.
  - *EN: This saying says one shouldn't take an extreme step like setting fire to the whole house out of fear of a small trouble.*
- **mT0-large** ✗: ಇಲಿ ಹೆಚ್ಚಿದೆ ಎಂದು, ಮನೆ ಉರಿ ಇಡಬಾರದು
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: ಇಲಿ ಹೆಚ್ಚಿದವೆಂದು ಮನೆಗೆ ಉರಿ ಇಡಬಾರದು ಎಂದರೆ, ಹೆಚ್ಚಿನ ಸಂಖ್ಯೆಯಲ್ಲಿರುವ ಒಣಗಿರುವ ವಸ್ತುಗಳನ್ನು (ಉರಿ) ಮನೆ
- **Sarvam-1** ✓: This means that if you are trying to get rid of something bad (like an "elephant" problem), it's better not to try and do too much at once - otherwise you might make things worse!

## 126. ಇಲಿಯ ವ್ಯಾಜ್ಯಕ್ಕೆ ಬೆಕ್ಕು ಸಾಕ್ಷಿ  (figurative)
*EN: A cat as witness in the rat's dispute*

- **Gold:** ದುರ್ಬಲನ ವಿವಾದದಲ್ಲಿ ಅವನ ವೈರಿಯೇ ಸಾಕ್ಷಿ ಅಥವಾ ನ್ಯಾಯಾಧೀಶನಾದರೆ ನ್ಯಾಯ ಸಿಗುವುದಿಲ್ಲ ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb says there is no justice when the weak person's enemy is the witness or judge in his dispute.*
- **mT0-large** ✓: Iliana is a merchant of a wealthy family.
- **Qwen3.5-2B** ✓: ಇಲಿಯ ವ್ಯಾಜ್ಯಕ್ಕೆ ಬೆಕ್ಕು ಸಾಕ್ಷಿ
- **Sarvam-1** ✗: This means that if you try to get rid of a problem by getting someone else involved, it will only make things worse.

## 127. ಇಲಿಯಾಗಿ ನೂರು ದಿನ ಬಾಳುವುದಕ್ಕಿಂತ ಹುಲಿಯಾಗಿ ಮೂರು ದಿನ ಬಾಳುವುದು ಲೇಸು  (figurative)
*EN: Better to live three days as a tiger than a hundred days as a rat*

- **Gold:** ಭಯದಿಂದ ಅವಮಾನದಲ್ಲಿ ಬಹುಕಾಲ ಬದುಕುವುದಕ್ಕಿಂತ ಸ್ವಾಭಿಮಾನದಿಂದ ಸ್ವಲ್ಪ ಕಾಲ ಬದುಕುವುದೇ ಲೇಸು ಎಂಬುದು ಇದರ ಅರ್ಥ.
  - *EN: Better to live a short time with self-respect than a long time in fear and humiliation.*
- **mT0-large** ✓: 'హాలి' లాగా మూడు நாட்లు గడపటానికి మంచిది.
  - *EN: [Telugu+Tamil mix] Good for spending three days like a 'Hali'.*
- **Qwen3.5-2B** ✓: ಇಲಿಯಾಗಿ ನೂರು ದಿನ ಬಾಳುವುದಕ್ಕಿಂತ ಹುಲಿಯಾಗಿ ಮೂರು ದಿನ ಬಾಳುವುದು ಲೇಸು ಎಂದರೆ, ಹುಲಿಯಂತೆ ಕೆಲಸ ಮಾಡಿದರೆ ನೂರು ದ
- **Sarvam-1** ✓: This means that it is better to be safe than sorry, and if you are going to take a risk, do so with caution.

## 128. ಇತ್ತಿತ್ತಾ ಬಾ ಅಂದ್ರೆ ಇದ್ದ ಮನೆಯೂ ಕಿತ್ತುಕೊಂಡ  (figurative)
*EN: Said 'come here, come here' and he snatched even the house that was there*

- **Gold:** ಸ್ವಲ್ಪ ಆಶ್ರಯ ಕೊಟ್ಟರೆ ಕೊಟ್ಟವನ ಇರುವ ಜಾಗವನ್ನೇ ಕಸಿದುಕೊಳ್ಳುವ ಮೋಸಗಾರನನ್ನು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb describes a cheat who, if given a little shelter, grabs the very place the giver has.*
- **mT0-large** ✓: 'అది కూడా కాదు, దానిని కూడా 'ఆ' అని పిలుచుకునేవాడే.
  - *EN: [Telugu] 'That is not it either; he is the one who calls even that 'that'.' (nonsensical)*
- **Qwen3.5-2B** ✓: ಇತ್ತಿತ್ತಾ ಬಾ ಅಂದ್ರೆ ಇದ್ದ ಮನೆಯೂ ಕಿತ್ತುಕೊಂಡ
- **Sarvam-1** ✓: This means that if you try to change something about someone or something, it will be difficult and may even cause more problems than before.

## 129. ಜಟ್ಟಿ ಬಿದ್ದರೂ ಮೀಸೆ ಮಣ್ಣಾಗಲಿಲ್ಲ  (literal)
*EN: Though the wrestler fell, his moustache didn't get dirty*

- **Gold:** ಸೋತರೂ ಸೋಲನ್ನು ಒಪ್ಪಿಕೊಳ್ಳದೆ ತನ್ನ ಜಂಬವನ್ನು ಉಳಿಸಿಕೊಳ್ಳುವ ವ್ಯಕ್ತಿಯ ಬಗ್ಗೆ ಹೇಳುವ ಮಾತು ಇದು.
  - *EN: A saying about a person who doesn't admit defeat even after losing and keeps up his arrogance.*
- **mT0-large** ✗: """జట్టు ಬಿದ್ದರೂ ಮೀಸೆ సన్నగా సన్నగా కాదు."""
  - *EN: [Telugu+Kannada mix] "Even if the topknot falls, the moustache is not thin, thin." (broken)*
- **Qwen3.5-2B** ✗: ಜಟ್ಟಿ ಬಿದ್ದರೂ ಮೀಸೆ ಮಣ್ಣಾಗಲಿಲ್ಲ
- **Sarvam-1** ✗: This means that even if you are not successful, your efforts will still be remembered and valued by others.

## 130. ಜನ ಮರುಳೋ ಜಾತ್ರೆ ಮರುಳೋ  (figurative)
*EN: Are the people mad or is the fair mad?*

- **Gold:** ಜನರು ವಿವೇಚನೆ ಇಲ್ಲದೆ ಗುಂಪಿನ ಹುಚ್ಚಿನಲ್ಲಿ ಹೋಗುವುದನ್ನು ಈ ಮಾತು ಸೂಚಿಸುತ್ತದೆ.
  - *EN: This saying suggests people going mindlessly in the frenzy of the crowd.*
- **mT0-large** ✗: ಜನರು ಮರುಳೋ ಜಾತ್ರೆ ಮರುಳೋ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: The meaning of the proverb is:
- **Sarvam-1** ✓: This means that if you do something wrong, it will come back to haunt you. It is a warning against repeating mistakes and taking unnecessary risks.

## 131. ಕಾಸಿದ್ರೆ ಕೈಲಾಸ ಇಲ್ಲದಿದ್ದರೆ ವನವಾಸ  (literal)
*EN: If there's money, Kailasa; if not, exile in the forest*

- **Gold:** ಹಣವಿದ್ದರೆ ಸುಖ, ಇಲ್ಲದಿದ್ದರೆ ಕಷ್ಟ ಎಂದು ಹಣದ ಮಹತ್ವವನ್ನು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb says the importance of money: with money, happiness; without it, hardship.*
- **mT0-large** ✓: వాయిద్యం లేని వనవాస
  - *EN: [Telugu] Exile in the forest without a musical instrument*
- **Qwen3.5-2B** ✗: ಕಾಸಿದ್ರೆ ಕೈಲಾಸ ಇಲ್ಲದಿದ್ದರೆ ವನವಾಸ
- **Sarvam-1** ✓: If you don't work hard, you won't get what you want.

## 132. ಕಷ್ಟ - ಸುಖ ಜೀವನದ ಎರಡು ಮುಖ  (literal)
*EN: Hardship and happiness are the two faces of life*

- **Gold:** ಜೀವನದಲ್ಲಿ ಕಷ್ಟ ಮತ್ತು ಸುಖ ಎರಡೂ ಒಂದರ ಹಿಂದೆ ಒಂದು ಬರುವುದು ಸಹಜ ಎಂದು ಈ ಮಾತು ಹೇಳುತ್ತದೆ.
  - *EN: This saying says that in life both hardship and happiness naturally come one after the other.*
- **mT0-large** ✓: ' ಕಷ್ಟ - ಸುಖ' ಎಂಬುದು ಜೀವನದ ಎರಡು ಮುಖಗಳು.
  - *EN: 'Hardship - happiness' are the two faces of life.*
- **Qwen3.5-2B** ✓: ಕಷ್ಟ - ಸುಖ ಜೀವನದ ಎರಡು ಮುಖ
- **Sarvam-1** ✓: This means that life is full of ups and downs, but it's important to keep going no matter what happens.

## 133. ಕೈಯಲ್ಲೇ ಆಗದವನು ಕೊಮ್ಮೆ ಮರಕ್ಕೆ ಗುತ್ತೆಗೆ ತಗೊಂಡ  (figurative)
*EN: One who couldn't manage what was in hand took a lease on a kombe tree*

- **Gold:** ತನ್ನ ಕೈಯಲ್ಲಿರುವುದನ್ನೇ ನಿಭಾಯಿಸಲಾಗದವನು ಅದಕ್ಕಿಂತ ದೊಡ್ಡ ಹೊಣೆಯನ್ನು ಹೊತ್ತುಕೊಳ್ಳುವುದನ್ನು ಈ ಮಾತು ಟೀಕಿಸುತ್ತದೆ.
  - *EN: This saying criticizes someone who can't handle what is in his hands taking on an even bigger responsibility.*
- **mT0-large** ✓: ಕೈಯಲ್ಲಿ ಆಗದವನನ್ನು ಕೊಮ್ಮೆ ಮರಕ್ಕೆ గుತ್ತೆಗೆ ತಗೊಂಡ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: ಕೈಯಲ್ಲೇ ಆಗದವನು ಕೊಮ್ಮೆ ಮರಕ್ಕೆ ಗುತ್ತೆಗೆ ತಗೊಂಡ
- **Sarvam-1** ✓: This means that if you can't do something, then it is better to give up and not waste your time trying.

## 134. ಕೊಂದ ಪಾಪ ತಿಂದು ಪರಿಹಾರ  (figurative)
*EN: The sin of killing is remedied by eating*

- **Gold:** ತಪ್ಪಿನಿಂದ ಆದ ಹಾನಿಯನ್ನು ಅದರಿಂದಲೇ ಲಾಭ ಪಡೆದು ಸರಿಪಡಿಸುತ್ತೇನೆ ಎನ್ನುವ ಅರ್ಥಹೀನ ಸಮರ್ಥನೆಯನ್ನು ಈ ಮಾತು ಸೂಚಿಸುತ್ತದೆ.
  - *EN: This saying points to the senseless justification of claiming to fix the damage from a mistake by profiting from it.*
- **mT0-large** ✗: The killer would have a solution.
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✗: This means that if you do something wrong, then it is better to face the consequences than try to hide or cover up your mistake.

## 135. ಕನ್ನಡಿಯೊಳಗಿನ ಗಂಟಿಗಿಂತ ಕೈಯೊಳಗಿನ ದಂಟೇ ಮೇಲು  (figurative)
*EN: A stalk in the hand is better than the bundle inside the mirror*

- **Gold:** ಸಿಗುವುದೋ ಇಲ್ಲವೋ ಗೊತ್ತಿಲ್ಲದ ದೊಡ್ಡ ಲಾಭಕ್ಕಿಂತ ಈಗ ಕೈಯಲ್ಲಿರುವ ಸಣ್ಣದೇ ಉತ್ತಮ ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb says a small thing in hand now is better than a big gain that may or may not come.*
- **mT0-large** ✓: ಕನ್ನಡಿಯ ಒಳಗಿನ ಗಂಟಿಗಿಂತ ಕೈಯ ಒಳಗಿನ ದಂಟೇ ಮೇಲೆ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಕನ್ನಡಿಯೊಳಗಿನ ಗಂಟಿಗಿಂತ ಕೈಯೊಳಗಿನ ದಂಟೇ ಮೇಲು
- **Sarvam-1** ✓: The proverb means that what you see is not always true, and it's better to look at things from a different perspective.

## 136. ಕೆಟ್ಟ ಮೇಲೆ ಬುದ್ಧಿ ಬಂತು  (literal)
*EN: Wisdom came after being ruined*

- **Gold:** ನಷ್ಟ ಅಥವಾ ಹಾನಿ ಅನುಭವಿಸಿದ ಮೇಲೆಯೇ ಒಬ್ಬನಿಗೆ ವಿವೇಕ ಬರುವುದನ್ನು ಈ ಮಾತು ಹೇಳುತ್ತದೆ.
  - *EN: This saying says that a person gains wisdom only after suffering loss or harm.*
- **mT0-large** ✓: 'ಕೆಟ್ಟ ಮೇಲೆ ಬುದ್ಧಿ ಬಂತು'
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಕೆಟ್ಟ ಮೇಲೆ ಬುದ್ಧಿ ಬಂತು
- **Sarvam-1** ✓: This means that when you are faced with a difficult situation, it is better to think about what you can do than just give up and accept defeat.

## 137. ಕೀಲು ಸಣ್ಣದಾದರೂ ಗಾಳಿ ನಡೆಸುತ್ತದೆ  (figurative)
*EN: Though the pin is small, it runs the wind*

- **Gold:** ಗಾತ್ರದಲ್ಲಿ ಸಣ್ಣದಾದ ವಸ್ತು ಅಥವಾ ವ್ಯಕ್ತಿಯೇ ದೊಡ್ಡ ವ್ಯವಸ್ಥೆಯನ್ನು ನಡೆಸುತ್ತಾನೆ ಎಂಬ ಅರ್ಥದ ಮಾತು ಇದು.
  - *EN: A saying meaning that a thing or person small in size is what runs a big system.*
- **mT0-large** ✗: ಕೀಲು ಸಣ್ಣದಾಗಿದ್ದರೂ ಗಾಳಿ ನಡೆಸುತ್ತದೆ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಕೀಲು ಸಣ್ಣದಾದರೂ ಗಾಳಿ ನಡೆಸುತ್ತದೆ
- **Sarvam-1** ✓: This means that even a small thing can have an impact on something bigger, like how a tiny insect can cause damage to a tree or plant. </s>

## 138. ಕೀರ್ತಿಯೇ ಕೈಲಾಸ ಅಪಕೀರ್ತಿಯೇ ನರಕ  (figurative)
*EN: Fame is Kailasa, infamy is hell*

- **Gold:** ಒಳ್ಳೆಯ ಹೆಸರೇ ಸ್ವರ್ಗ, ಕೆಟ್ಟ ಹೆಸರೇ ನರಕ ಎಂದು ಒಳ್ಳೆಯ ಕೀರ್ತಿಯ ಮಹತ್ವವನ್ನು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb says the importance of a good reputation: a good name is heaven, a bad name is hell.*
- **mT0-large** ✗: ಕೀರ್ತಿಯೇ ಕೈಲಾಸ ಅಪಕೀರ್ತಿಯೇ ನರಕ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಕೀರ್ತಿಯೇ ಕೈಲಾಸ ಅಪಕೀರ್ತಿಯೇ ನರಕ
- **Sarvam-1** ✓: This means that fame is like a mountain, and it can be very difficult to get down from there. It's also like hell, because once you fall off, it's hard to climb back up again. [/INST]

## 139. ಕೋಪದಲ್ಲಿ ಕೊಯ್ದ ಮೂಗು ಶಾಂತಿಯಲ್ಲಿ ಬರುವುದೆ?  (figurative)
*EN: Can a nose cut off in anger be restored in peace?*

- **Gold:** ಕೋಪದಲ್ಲಿ ಮಾಡಿದ ಕೆಲಸದ ಪರಿಣಾಮವನ್ನು ಶಾಂತವಾದ ಮೇಲೆ ಸರಿಪಡಿಸಲಾಗದು ಎಂದು ಈ ಮಾತು ಎಚ್ಚರಿಸುತ್ತದೆ.
  - *EN: This saying warns that the consequences of what is done in anger can't be fixed once one has calmed down.*
- **mT0-large** ✓: ಶಾಂತಿಯ ಕಡೆಗೆ ಶಾಂತಿಯ ಕಡೆಗೆ ಶಾಂತಿಯ ಕಡೆಗೆ ಶಾಂತಿಯ ಕಡೆಗೆ ಶಾಂತಿಯ ಕಡೆಗೆ ಶಾಂತಿಯ ಕಡೆಗೆ ಶಾಂತಿಯ ಕಡೆಗೆ ಶಾಂತಿಯ ಕಡೆಗೆ ಶಾಂತಿಯ ಕಡೆಗೆ ಶಾಂತಿಯ ಕಡೆಗೆ ಶಾಂತಿಯ ಕಡೆಗೆ ಶಾಂತಿಯ ಕಡೆಗೆ
  - *EN: Towards peace, towards peace, towards peace... (repetitive)*
- **Qwen3.5-2B** ✓: ಕೋಪದಲ್ಲಿ ಕೊಯ್ದ ಮೂಗು ಶಾಂತಿಯಲ್ಲಿ ಬರುವುದೆ?
- **Sarvam-1** ✓: This means that when you are angry, it is hard to calm down and make things right again. It takes time and effort to fix problems after they have been made worse by anger. </s>

## 140. ಕೋತಿ ತಾನು ಕೆಡೋದಲ್ಲದೆ ವನವನ್ನೂ ಕೆಡಿಸಿತು  (figurative)
*EN: The monkey not only ruined itself but ruined the forest too*

- **Gold:** ತಾನು ಹಾಳಾಗುವುದಲ್ಲದೆ ಸುತ್ತಲಿನವರನ್ನೂ ಹಾಳು ಮಾಡುವ ವ್ಯಕ್ತಿಯನ್ನು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb describes a person who not only ruins himself but ruins those around him as well.*
- **mT0-large** ✓: ಕೋತಿ ತನ್ನ ಮಗನನ್ನು ಗಾಯಗೊಳಿಸುತ್ತಾ, ತನ್ನ ಮಗನನ್ನು ಗಾಯಗೊಳಿಸುತ್ತಾ, ತನ್ನ ಮಗನನ್ನು ಗಾಯಗೊಳಿಸುತ್ತಾ, ತನ್ನ ಮಗನನ್ನು ಗಾಯಗೊಳಿಸುತ್ತಾ, ತನ್ನ ಮಗನನ್ನು ಗಾಯಗೊಳಿಸುತ್ತಾ, ತನ್ನ ಮಗನನ್ನು ಗಾಯಗೊಳಿಸ
  - *EN: The monkey, while injuring its son, while injuring its son, while injuring its son... (repetitive)*
- **Qwen3.5-2B** ✓: ಕೋತಿ ತಾನು ಕೆಡೋದಲ್ಲದೆ ವನವನ್ನೂ ಕೆಡಿಸಿತು
- **Sarvam-1** ✓: This means that if you do something bad, it will affect not only yourself but also others around you.

## 141. ಕೋತಿಯಂಥೋನು ಕೆಣಕಿದ, ಮುತಿಗೆ ಹೆಟ್ಟಿಸಿಕೊಂಡು ತಿಣುಕಿದ  (figurative)
*EN: A monkey-like fellow provoked, got struck by the pestle, and writhed*

- **Gold:** ತನಗಿಂತ ಬಲಿಷ್ಠರನ್ನು ಕೆಣಕಿ ತಾನೇ ಪೆಟ್ಟು ತಿಂದು ಸಂಕಟ ಪಡುವವನ ಬಗ್ಗೆ ಹೇಳುವ ಮಾತು ಇದು.
  - *EN: A saying about one who provokes those stronger than himself, gets hurt and suffers.*
- **mT0-large** ✓: ಕೋತಿಯಂಥೋನು ಕೆಣಕಿದ, ಮುತಿಗೆ ಹೆಟ್ಟಿಸಿಕೊಂಡು ತಿಣುಕಿದ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಕೋತಿಯಂಥೋನು ಕೆಣಕಿದ, ಮುತಿಗೆ ಹೆಟ್ಟಿಸಿಕೊಂಡು ತಿಣುಕಿದ
- **Sarvam-1** ✓: This means that if you are too proud or arrogant about something, people will make fun of you and try to get back at you by making a fool out of you.

## 142. ಕೂಸು ಹುಟ್ಟೋಕೆ ಮುಂಚೆ ಕುಲಾವಿ ಹೊಲಿಸಿದಳು  (figurative)
*EN: She had the baby's gown stitched before the baby was born*

- **Gold:** ಫಲಿತಾಂಶ ಗೊತ್ತಾಗುವ ಮೊದಲೇ ಅವಸರದಿಂದ ತಯಾರಿ ಮಾಡುವುದನ್ನು ಈ ಗಾದೆ ಗೇಲಿ ಮಾಡುತ್ತದೆ.
  - *EN: This proverb mocks hasty preparation made before the result is known.*
- **mT0-large** ✗: 'కొడుకు పుట్టುವ ಮುಂಚೆ తల్లిదండ్రులు 'కొడుకు' కోసం ಹೊಲದ మీద నుంచి 'కొడుకు' కోసం ಹೊಲದ మీద నుంచి ಹೊಲದ మీద నుంచి ಹೊಲದ మీద నుంచి ಹೊಲದ మీద నుంచి ಹೊಲದ
  - *EN: [Telugu+Kannada mix] 'Before the son is born, parents from on the field for the 'son', from on the field, from on the field...' (repetitive)*
- **Qwen3.5-2B** ✓: ಕೂಸು ಹುಟ್ಟೋಕೆ ಮುಂಚೆ ಕುಲಾವಿ ಹೊಲಿಸಿದಳು
- **Sarvam-1** ✗: This means that you should not worry about things before they happen, because it is better to do something now than later when it might be too late.

## 143. ಕೂತು ಉಣ್ಣೋಳಿಗೆ ಕುಡಿಕೆ ಹೊನ್ನು ಸಾಲದು  (figurative)
*EN: A pot of gold is not enough for one who sits and eats*

- **Gold:** ದುಡಿಯದೆ ಕೂತು ತಿನ್ನುವವರಿಗೆ ಎಷ್ಟು ಸಂಪತ್ತಿದ್ದರೂ ಖರ್ಚಾಗಿ ಮುಗಿದುಹೋಗುತ್ತದೆ ಎಂದು ಈ ಮಾತು ಹೇಳುತ್ತದೆ.
  - *EN: This saying says that however much wealth there is, it gets spent and runs out for those who sit and eat without working.*
- **mT0-large** ✗: a few feet away from the stove
- **Qwen3.5-2B** ✗: ಕೂತು ಉಣ್ಣೋಳಿಗೆ ಕುಡಿಕೆ ಹೊನ್ನು ಸಾಲದು
- **Sarvam-1** ✓: This means that if you are not working hard, then you will not get anything out of your efforts. It is a reminder to work hard and be productive. </s>

## 144. ಕಡು ಕೋಪ ಬಂದಾಗ ತಡಕೊಂಡವನೇ ಜಾಣ  (literal)
*EN: One who holds back when great anger comes is the wise one*

- **Gold:** ತುಂಬಾ ಕೋಪ ಬಂದಾಗಲೂ ತಾಳ್ಮೆಯಿಂದ ಸಹಿಸಿಕೊಂಡವನೇ ನಿಜವಾದ ಬುದ್ಧಿವಂತ.
  - *EN: One who patiently bears it even when very angry is truly wise.*
- **mT0-large** ✓: ದೈನಂದಿನ ದೈನಂದಿನ ದೈನಂದಿನ ದೈನಂದಿನ ದೈನಂದಿನ ದೈನಂದಿನ ದೈನಂದಿನ ದೈನಂದಿನ ದೈನಂದಿನ ದೈನಂದಿನ ದೈನಂದಿನ ದೈನಂದಿನ
  - *EN: Daily daily daily daily... (repetitive)*
- **Qwen3.5-2B** ✓: ಕಡು ಕೋಪ ಬಂದಾಗ ತಡಕೊಂಡವನೇ ಜಾಣ
- **Sarvam-1** ✓: This means that when you are angry, it is better to wait before acting on your anger because if you act too quickly and without thinking about what you're doing, you might make a mistake or do something bad. It's like waiting for the right time to cut down a tree - if

## 145. ಕಂಡದ್ದು ಕಾಣೆ ಉತ್ತಮ, ಕಂಡದ್ದು ಕಂಡೆ ಮಧ್ಯಮ, ಕಾಣದ್ದು ಕಂಡೆ ಅಧಮ  (literal)
*EN: Not seeing what you saw is best, seeing what you saw is middling, claiming to see what you didn't see is lowest*

- **Gold:** ಇತರರ ತಪ್ಪನ್ನು ಕಂಡರೂ ಕಾಣದಂತೆ ಇರುವುದು ಉತ್ತಮ, ಕಂಡದ್ದನ್ನು ಹೇಳುವುದು ಮಧ್ಯಮ, ಕಾಣದ್ದನ್ನು ಕಂಡೆನೆನ್ನುವುದು ಕೆಟ್ಟದ್ದು.
  - *EN: It is best to pretend not to see others' faults even when you have seen them; telling what you saw is middling; claiming to have seen what you didn't is bad.*
- **mT0-large** ✓: ಯಾವುದಾದರೊಂದು ಉತ್ತಮ, ಯಾವುದಾದರೊಂದು ಮಧ್ಯಮ, ಯಾವುದಾದರೊಂದು ಅಧಮ
  - *EN: Some one is best, some one is middling, some one is worst*
- **Qwen3.5-2B** ✓: The meaning of the proverb is:
- **Sarvam-1** ✓: This means that if you see something good but don't do anything about it, then it is better than doing nothing at all and not seeing any good thing. If you only look for bad things, then you will never find anything good.

## 146. ಕಂಡವರ ಮಕ್ಕಳನ್ನು ಬಾವಿಯಲ್ಲಿ ದೂಡಿ ಆಳ ನೋಡಿದ ಹಾಗೆ  (figurative)
*EN: Like pushing other people's children into a well to see how deep it is*

- **Gold:** ತನ್ನ ಪರೀಕ್ಷೆ ಅಥವಾ ಕುತೂಹಲಕ್ಕಾಗಿ ಬೇರೆಯವರನ್ನು ಅಪಾಯಕ್ಕೆ ಸಿಲುಕಿಸುವುದನ್ನು ಈ ಗಾದೆ ಟೀಕಿಸುತ್ತದೆ.
  - *EN: This proverb criticizes putting others in danger for one's own test or curiosity.*
- **mT0-large** ✗: ಮಕ್ಕಳು ನೋಡುವಾಗ ಮಕ್ಕಳು ಬಹುಪಾಲು ದೃಶ್ಯವಾಗಿ ಕಾಣುತ್ತಿದ್ದರು.
  - *EN: When the children watch, the children appeared mostly visually. (nonsensical)*
- **Qwen3.5-2B** ✗: ಕಂಡವರ ಮಕ್ಕಳನ್ನು ಬಾವಿಯಲ್ಲಿ ದೂಡಿ ಆಳ ನೋಡಿದ ಹಾಗೆ
- **Sarvam-1** ✓: This means that if you see someone else's problems, it is like seeing a bunch of worms drowning in water. It can be very sad and depressing to watch others suffer. </s>

## 147. ಕಂಗಾಲಾದರೂ ಹಂಗಾಲಾಗಬಾರದು  (literal)
*EN: Even if destitute, one should not become beholden*

- **Gold:** ಎಷ್ಟೇ ಬಡತನ ಅಥವಾ ಕಷ್ಟ ಬಂದರೂ ಇತರರ ಉಪಕಾರದ ಋಣಕ್ಕೆ ಸಿಲುಕಬಾರದು ಎಂದು ಈ ಮಾತು ಹೇಳುತ್ತದೆ.
  - *EN: This saying says that however poor or troubled one is, one shouldn't fall into the debt of obligation to others' favors.*
- **mT0-large** ✓: When you're angry, you'll be angry.
- **Qwen3.5-2B** ✓: ಕಂಗಾಲಾದರೂ ಹಂಗಾಲಾಗಬಾರದು
- **Sarvam-1** ✓: This means that you should not be upset or worried about something when it is out of your control, because this will only make things worse for you.

## 148. ಕಣ ಕಾಯಬಹುದು, ಹೆಣ ಕಾಯಕಾಗುವುದಿಲ್ಲ  (literal)
*EN: One can guard the threshing floor, but one cannot guard a corpse*

- **Gold:** ಧಾನ್ಯದ ರಾಶಿಯನ್ನು ಕಾಯಬಹುದು, ಆದರೆ ಸತ್ತ ದೇಹವನ್ನು ಬಹುಕಾಲ ಕಾಯಲಾಗದು ಎಂದು ಈ ಮಾತು ಹೇಳುವಂತೆ ತೋರುತ್ತದೆ.
  - *EN: This saying seems to say that a heap of grain can be guarded, but a dead body cannot be kept waiting for long.*
- **mT0-large** ✗: ಕಣలు ಕಾಯಬಹುದು, కాని పక్షులు ಕಾಯవు.
  - *EN: [Kannada+Telugu mix] Threshing floors can wait, but birds don't wait.*
- **Qwen3.5-2B** ✗: ಕಣ ಕಾಯಬಹುದು, ಹೆಣ ಕಾಯಕಾಗುವುದಿಲ್ಲ
- **Sarvam-1** ✓: This means that if you are not willing to do something, then it is unlikely that you will be able to accomplish it. It's like saying "if you don't want to do something, then you won't be able to do it". [/INST]

## 149. ಕಟ್ಟಿದ ಕೆರೆಗೆ ಕೋಡಿ ತಪ್ಪಲ್ಲ, ಹುಟ್ಟಿದ ಮನೆಗೆ ಬೇರೆ ತಪ್ಪಲ್ಲ  (figurative)
*EN: A built tank can't avoid its spillway; the house one was born in can't avoid parting*

- **Gold:** ಹೆಣ್ಣುಮಗಳು ಮದುವೆಯಾಗಿ ತವರು ಬಿಟ್ಟು ಹೋಗುವುದು ಕೆರೆ ತುಂಬಿ ಕೋಡಿ ಹರಿಯುವಂತೆ ಅನಿವಾರ್ಯ ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb says a daughter leaving her parental home after marriage is as inevitable as a tank overflowing through its spillway.*
- **mT0-large** ✓: ಮನೆಯ ಒಳಗಿನಿಂದ ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳು ಮಕ್ಕಳ
  - *EN: From inside the house, children children children children... (repetitive)*
- **Qwen3.5-2B** ✓: ಕಟ್ಟಿದ ಕೆರೆಗೆ ಕೋಡಿ ತಪ್ಪಲ್ಲ, ಹುಟ್ಟಿದ ಮನೆಗೆ ಬೇರೆ ತಪ್ಪಲ್ಲ (A house built on a foundation is safe, a house born in a good family is safe)
- **Sarvam-1** ✓: This means that if you do something wrong to someone or somewhere, it is not a big deal because everyone makes mistakes and we all come from the same place.

## 150. ಕಾರ್ಯವಾಸಿ ಕತ್ತೆ ಕಾಲು ಹಿಡಿ  (figurative)
*EN: To get the work done, hold the donkey's feet*

- **Gold:** ತನ್ನ ಕೆಲಸ ಆಗಬೇಕಾದರೆ ಯೋಗ್ಯರಲ್ಲದವರ ಮುಂದೆಯೂ ತಗ್ಗಿ ನಡೆಯಬೇಕಾಗುತ್ತದೆ ಎಂದು ಈ ಮಾತು ಹೇಳುತ್ತದೆ.
  - *EN: This saying says that to get one's work done, one must bow even before the unworthy.*
- **mT0-large** ✗: a worker stood on the floor
- **Qwen3.5-2B** ✓: ಕಾರ್ಯವಾಸಿ ಕತ್ತೆ ಕಾಲು ಹಿಡಿ
- **Sarvam-1** ✓: This means that if you are too busy to do something, then it is not worth doing at all. It's like a donkey with a heavy load on its back - it can only carry so much before it breaks down. The same goes for people who are always working and never taking time

## 151. ಕಾಮಾಲೆ ಕಣ್ಣೊನಿಗೆ ಕಂಡಿದ್ದೆಲ್ಲ ಹಳದಿನೇ  (figurative)
*EN: To the jaundiced eye, everything seen is yellow*

- **Gold:** ಪೂರ್ವಾಗ್ರಹ ಅಥವಾ ದೋಷದೃಷ್ಟಿ ಇರುವವನಿಗೆ ಎಲ್ಲವೂ ತಪ್ಪಾಗಿಯೇ ಕಾಣುತ್ತದೆ ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb says that to one who has prejudice or a fault-finding eye, everything looks wrong.*
- **mT0-large** ✓: ಹಳది కాదు
  - *EN: [Kannada+Telugu mix] Not turmeric*
- **Qwen3.5-2B** ✓: ಕಾಮಾಲೆ ಕಣ್ಣೊನಿಗೆ ಕಂಡಿದ್ದೆಲ್ಲ ಹಳದಿನೇ
- **Sarvam-1** ✓: This means that if you see something old, it is probably not worth your time or effort to try and change it. It's better to focus on things that are new and exciting.

## 152. ಕಬ್ಬು ಡೊಂಕಾದರೆ ಸಿಹಿ ಡೊಂಕೇ  (figurative)
*EN: If the sugarcane is crooked, is its sweetness crooked?*

- **Gold:** ಕಬ್ಬು ಡೊಂಕಾಗಿದ್ದರೂ ಅದರ ಸಿಹಿ ಡೊಂಕಾಗಿರುವುದಿಲ್ಲ, ಅಂದರೆ ರೂಪ ಸರಿಯಿಲ್ಲದಿದ್ದರೂ ಗುಣ ಕೆಡುವುದಿಲ್ಲ ಎಂದು ಈ ಮಾತು ಹೇಳುತ್ತದೆ.
  - *EN: Even if sugarcane is crooked, its sweetness is not crooked; that is, though appearance isn't good, quality does not spoil.*
- **mT0-large** ✓: ಡೊಂಕಾದ ಡೊಂಕಾದ ಡೊಂಕಾದ
  - *EN: Crooked crooked crooked*
- **Qwen3.5-2B** ✓: ಕಬ್ಬು ಡೊಂಕಾದರೆ ಸಿಹಿ ಡೊಂಕೇ
- **Sarvam-1** ✓: If something is not going well, it will only get worse.

## 153. ಕಚ್ಚುವ ನಾಯಿ ಬೊಗಳದು, ಬೊಗಳುವ ನಾಯಿ ಕಚ್ಚದು  (figurative)
*EN: A biting dog doesn't bark, a barking dog doesn't bite*

- **Gold:** ಗದ್ದಲ ಮಾಡುವವರಿಂದ ಹೆಚ್ಚು ಹಾನಿಯಿಲ್ಲ, ಸದ್ದಿಲ್ಲದೆ ಇರುವವರೇ ನಿಜವಾಗಿ ಅಪಾಯಕಾರಿ ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: Those who make noise do little harm; it is those who stay silent who are truly dangerous.*
- **mT0-large** ✓: ಕೀಟಗಳು, ಪಕ್ಷಿಗಳು, ಪಕ್ಷಿಗಳು, ಪಕ್ಷಿಗಳು, ಪಕ್ಷಿಗಳು, ಪಕ್ಷಿಗಳು, ಪಕ್ಷಿಗಳು, ಪಕ್ಷಿಗಳು, ಪಕ್ಷಿಗಳು, ಪಕ್ಷಿಗಳು, ಪಕ್ಷಿಗಳು, ಪಕ್ಷಿಗಳು, ಪಕ್ಷಿಗಳು, ಪಕ್ಷಿಗಳು, ಪಕ್ಷಿಗಳು
  - *EN: Insects, birds, birds, birds, birds... (repetitive)*
- **Qwen3.5-2B** ✓: The meaning of the proverb is that a dog that barks at others will be barked at in return, while a dog that barks at nothing will be left alone.
- **Sarvam-1** ✓: This means that if you are not going to do something badly or hurtful, then don't bother doing it at all. If someone is trying to get your attention by making a noise, but they aren't actually causing any harm, then there's no need for them to

## 154. ಕೈಗೆ ಬಂದ ತುತ್ತು ಬಾಯಿಗೆ ಇಲ್ಲ  (figurative)
*EN: The morsel that came to the hand is not for the mouth*

- **Gold:** ಇನ್ನೇನು ಸಿಕ್ಕಿತು ಎನ್ನುವಾಗಲೇ ಕೈಗೆ ಬಂದದ್ದು ಕೈತಪ್ಪಿ ಹೋಗುವ ನಿರಾಸೆಯನ್ನು ಈ ಮಾತು ಹೇಳುತ್ತದೆ.
  - *EN: This saying expresses the disappointment when what came into one's hand slips away just as it seemed obtained.*
- **mT0-large** ✗: The spoon is not in the mouth.
- **Qwen3.5-2B** ✓: ಕೈಗೆ ಬಂದ ತುತ್ತು ಬಾಯಿಗೆ ಇಲ್ಲ
- **Sarvam-1** ✓: This means that if you take something for granted, then it will not be enough to satisfy your needs or desires. It is a reminder to always appreciate what we have and not waste time complaining about things that are beyond our control. </s>

## 155. ಕೈಯಲ್ಲಿ ಶರಣಾರ್ಥಿ, ಕಂಕುಳಲ್ಲಿ ದೊಣ್ಣೆ  (figurative)
*EN: A salutation in the hand, a club under the arm*

- **Gold:** ಮೇಲ್ನೋಟಕ್ಕೆ ವಿನಯ ಮತ್ತು ಗೌರವ ತೋರಿಸುತ್ತಾ, ಒಳಗೊಳಗೇ ಕೇಡು ಅಥವಾ ಮೋಸದ ಉದ್ದೇಶ ಇಟ್ಟುಕೊಂಡಿರುವವನನ್ನು ಈ ಗಾದೆ ವರ್ಣಿಸುತ್ತದೆ.
  - *EN: This proverb describes one who shows humility and respect outwardly while holding harmful or deceitful intentions inside.*
- **mT0-large** ✗: ಕೈಯಲ್ಲಿ ಶರಣಾರ್ಥಿ, ಕಂಕುಳಲ್ಲಿ ದೊಣ್ಣೆ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಕೈಯಲ್ಲಿ ಶರಣಾರ್ಥಿ, ಕಂಕುಳಲ್ಲಿ ದೊಣ್ಣೆ
- **Sarvam-1** ✓: This means that if you give up your rights or power to someone else, they will take advantage of it and use it against you.

## 156. ಕಲ್ಲು ಇದ್ದಾಗ ನಾಯಿ ಇಲ್ಲ ನಾಯಿ ಇದ್ದಾಗ ಕಲ್ಲು ಇಲ್ಲ  (figurative)
*EN: When there's a stone there's no dog; when there's a dog there's no stone*

- **Gold:** ಒಂದು ವಸ್ತು ಬೇಕಾದಾಗ ಅದರ ಜೊತೆಗೆ ಬೇಕಾದ ಇನ್ನೊಂದು ವಸ್ತು ಇರುವುದಿಲ್ಲ, ಎರಡೂ ಒಟ್ಟಿಗೆ ಸಿಗುವುದು ಅಪರೂಪ ಎನ್ನುವುದನ್ನು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb says that when one thing is needed, the other thing needed with it isn't there; it is rare to get both together.*
- **mT0-large** ✗: A dog is not a dog when it is a dog.
- **Qwen3.5-2B** ✓: The meaning of the proverb is:
- **Sarvam-1** ✗: This means that when there is a problem, it's better to deal with it than ignore it. If you don't address the issue, it will only get worse and cause more problems later on.

## 157. ಕಪ್ಪರ ತಿಪ್ಪೆಲಿಟ್ಟರೆ ತನ್ನ ವಾಸನೆ ಬಿಟ್ಟಿತೇ?  (figurative)
*EN: If camphor is put in the dungheap, does it lose its own smell?*

- **Gold:** ಕರ್ಪೂರವನ್ನು ಕಸದ ರಾಶಿಯಲ್ಲಿ ಇಟ್ಟರೂ ಅದು ತನ್ನ ಸುವಾಸನೆ ಕಳೆದುಕೊಳ್ಳುವುದಿಲ್ಲ; ಒಳ್ಳೆಯ ವ್ಯಕ್ತಿ ಕೆಟ್ಟ ಪರಿಸರದಲ್ಲಿದ್ದರೂ ತನ್ನ ಗುಣ ಬಿಡುವುದಿಲ್ಲ.
  - *EN: Even if camphor is put in a garbage heap, it does not lose its fragrance; a good person does not give up his qualities even in a bad environment.*
- **mT0-large** ✓: ತನ್ನ ವಾಸನೆ ಬಿಟ್ಟು ತನ್ನ ಪಾದವನ್ನು ತೋಡಿದ
  - *EN: Leaving his smell, dug his own foot (nonsensical)*
- **Qwen3.5-2B** ✗: ಕಪ್ಪರ ತಿಪ್ಪೆಲಿಟ್ಟರೆ ತನ್ನ ವಾಸನೆ ಬಿಟ್ಟಿತೇ?
- **Sarvam-1** ✓: This means that if you try to hide something, it will eventually come out.

## 158. ಕಥೆ ಹೇಳೋಕೆ ಹ್ಯುಮ್-ಗುಟ್ಟೋರಿರಬೇಕು, ನೆಟ್ಟಗೆ ಬಾಳೋಕೆ ಚಿ-ಗುಟ್ಟೋರಿರಬೇಕು  (figurative)
*EN: To tell a story there must be those who say 'hum'; to live upright there must be those who say 'chee'*

- **Gold:** ಕಥೆ ಹೇಳಲು ಹೂಂ ಗುಟ್ಟುವ ಕೇಳುಗರು ಬೇಕು, ಆದರೆ ಸರಿದಾರಿಯಲ್ಲಿ ಬಾಳಲು ತಪ್ಪಿದಾಗ ಛೀ ಎಂದು ತಿದ್ದುವ ಹಿರಿಯರು ಬೇಕು ಎಂಬ ಅರ್ಥ ಇರಬಹುದು.
  - *EN: It may mean that to tell a story you need listeners who say 'hmm', but to live on the right path you need elders who say 'chee' and correct you when you err.*
- **mT0-large** ✓: ನೆಟ್ಟಗೆ ಬಾಳೋಕೆ ಚಿ-ಗುಟ್ಟೋರಿರಬೇಕು
  - *EN: To live straight there must be people who go 'tsk' (scold)*
- **Qwen3.5-2B** ✓: ಕಥೆ ಹೇಳೋಕೆ ಹ್ಯುಮ್-ಗುಟ್ಟೋರಿರಬೇಕು, ನೆಟ್ಟಗೆ ಬಾಳೋಕೆ ಚಿ-ಗುಟ್ಟೋರಿರಬೇಕು ಎಂದರೆ, ಕಥೆ ಹೇಳ
- **Sarvam-1** ✓: This means that you need to be able to tell a good story and also have some common sense to live your life.

## 159. ಕೆಡುವ ಕಾಲಕ್ಕೆ ಬುದ್ಧಿ ಇಲ್ಲ ಮರಣ ಕಾಲಕ್ಕೆ ಮದ್ದಿಲ್ಲ  (literal)
*EN: No sense at the time of ruin, no medicine at the time of death*

- **Gold:** ಹಾಳಾಗುವ ಕಾಲ ಬಂದಾಗ ಬುದ್ಧಿ ಕೆಲಸ ಮಾಡುವುದಿಲ್ಲ, ಸಾಯುವ ಕಾಲಕ್ಕೆ ಯಾವ ಔಷಧವೂ ಉಳಿಸುವುದಿಲ್ಲ.
  - *EN: When the time of ruin comes, the mind doesn't work; at the time of death, no medicine saves.*
- **mT0-large** ✓: 'ಕೆಡುವ ಕಾಲಕ್ಕೆ ಬುದ್ಧಿ ಇಲ್ಲ, ಮರಣ ಕಾಲಕ್ಕೆ ಮದ್ದಿಲ್ಲ'
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: Here is the explanation:
- **Sarvam-1** ✓: This means that when you are dying, there is no time to think about anything else and it's too late for regrets or trying to fix things. It's like a saying that if you have died, then your life has ended anyway so why waste time on something that can

## 160. ಕಿಡಿಯಿಂದ ಕಾಡ ಸುಡಬಹುದು  (figurative)
*EN: A forest can be burned by a spark*

- **Gold:** ಒಂದು ಸಣ್ಣ ಕಿಡಿ ಇಡೀ ಕಾಡನ್ನು ಸುಡುವಂತೆ, ಸಣ್ಣ ವಿಷಯವೂ ದೊಡ್ಡ ಹಾನಿ ಅಥವಾ ಜಗಳಕ್ಕೆ ಕಾರಣವಾಗಬಹುದು.
  - *EN: Just as one small spark can burn a whole forest, even a small matter can cause great harm or a quarrel.*
- **mT0-large** ✗: The flame can burn the forest.
- **Qwen3.5-2B** ✓: ಕಿಡಿಯಿಂದ ಕಾಡ ಸುಡಬಹುದು
- **Sarvam-1** ✓: This means that you can do something bad to someone, but it will not be as bad as if you had done good things to them.

## 161. ಕೊಡಲಿ ಕಾವೂ ಕುಲಕ್ಕೆ ಸಾವು  (figurative)
*EN: Even the axe's handle is death to its clan*

- **Gold:** ಕೊಡಲಿಗೆ ಕಾವು ಅದೇ ಮರದ ಕುಲದಿಂದ ಬರುವಂತೆ, ತನ್ನವರೇ ಸೇರಿಕೊಂಡು ದ್ರೋಹ ಮಾಡಿದರೆ ಇಡೀ ಬಳಗ ನಾಶವಾಗುತ್ತದೆ.
  - *EN: Just as the handle of an axe comes from the very tree's clan, if one's own people join in betrayal, the whole kin is destroyed.*
- **mT0-large** ✗: 'ಕೆಲವರು తమ ಮಗುವಿನ ಸಾವಿಗೆ తమ తల్లిదండ్రుల ಸಾವಿಗೆ తమ తల్లిదండ్రుల ಸಾವಿಗೆ తమ తల్లిదండ్రుల ಸಾವಿಗೆ తమ తల్లిదండ్రుల ಸಾವಿಗೆ తమ తల్లిదండ్రుల
  - *EN: [Kannada+Telugu mix] 'Some, for the death of their child, for the death of their parents, for the death of their parents...' (repetitive)*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that if you are not careful, your family will suffer because of your actions. It is a warning to be cautious and responsible with others' money or property. </s>

## 162. ಕೋಣನಿಗೆ ಕೊಸೆಯೋ ಸಂಕಟ, ಎಮ್ಮೆಗೆ ಈಯೋ ಸಂಕಟ  (figurative)
*EN: The bull buffalo's pain of kosey, the she-buffalo's pain of giving birth*

- **Gold:** ನಿಜವಾಗಿ ನೋವು ಅನುಭವಿಸುವವರು ಒಬ್ಬರಾದರೆ, ಅದರ ಬಗ್ಗೆ ತನಗೂ ಅಷ್ಟೇ ಸಂಕಟ ಎಂದು ತೋರಿಸಿಕೊಳ್ಳುವವರು ಇನ್ನೊಬ್ಬರು ಎಂದು ಅರ್ಥೈಸಬಹುದು.
  - *EN: It can be taken to mean that while one person truly suffers, another shows that he suffers just as much.*
- **mT0-large** ✓: ಕೋಣನಿಗೆ ಕೊಸೆಯೋ ಸಂಕಟ, ఎమ్మೆಗೆ ఈಯೋ ಸಂಕಟ
  - *EN: For the he-buffalo the agony of castration, for the she-buffalo the agony of calving*
- **Qwen3.5-2B** ✓: ಕೋಣನಿಗೆ ಕೊಸೆಯೋ ಸಂಕಟ, ಎಮ್ಮೆಗೆ ಈಯೋ ಸಂಕಟ
- **Sarvam-1** ✓: This means that a person who is trying to get something will have trouble getting it and someone else may be having more difficulty than he or she is.

## 163. ಕೊಟ್ಟವನು ಕೋಡಂಗಿ, ಇಸ್ಕೊಂಡವನು ವೀರಭದ್ರ  (figurative)
*EN: The giver is a clown, the taker is Veerabhadra*

- **Gold:** ಸಾಲ ಕೊಟ್ಟವನು ಮೆತ್ತಗೆ ಹಾಸ್ಯಾಸ್ಪದನಂತೆ ಆಗುತ್ತಾನೆ, ಸಾಲ ತೆಗೆದುಕೊಂಡವನು ಉಗ್ರ ರೂಪ ತಾಳುತ್ತಾನೆ ಎಂಬುದು ಅರ್ಥ.
  - *EN: It means the lender becomes meek and laughable, while the borrower takes a fierce form.*
- **mT0-large** ✗: 'అతను కోడంగి, ఇతను ವೀರಭದ್ರ'
  - *EN: [Telugu+Kannada mix] 'He is a clown, this one is Veerabhadra (a fierce warrior god)'*
- **Qwen3.5-2B** ✓: ಕೊಟ್ಟವನು ಕೋಡಂಗಿ, ಇಸ್ಕೊಂಡವನು ವೀರಭದ್ರ
- **Sarvam-1** ✓: The proverb means that if you give something to someone, they will not be grateful or appreciative for it. They may even try to take it back from you. This is a common saying and can apply to many situations where people are given things by others without expecting anything in return

## 164. ಕ್ರಮ ಕಾಣದ ನಾಯಿ ಕಪಾಲ ನೆಕ್ತು  (figurative)
*EN: A dog that had seen no order licked the skull*

- **Gold:** ಸರಿಯಾದ ರೀತಿ ನೀತಿ, ಶಿಷ್ಟಾಚಾರ ತಿಳಿಯದವನು ಸ್ಥಳ ಸಂದರ್ಭ ನೋಡದೆ ಅನುಚಿತವಾಗಿ ವರ್ತಿಸುತ್ತಾನೆ.
  - *EN: One who doesn't know proper conduct and etiquette behaves improperly without regard for place and occasion.*
- **mT0-large** ✓: ಕ್ರಮ ಕಾಣದ ನಾಯಿ ಕಪಾಲ ನೆಕ್ಟ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಕ್ರಮ ಕಾಣದ ನಾಯಿ ಕಪಾಲ ನೆಕ್ತು
- **Sarvam-1** ✓: This means that if you don't take action, you will never get what you want. It is a warning to not procrastinate and do something about your problems.

## 165. ಕುಂಬಾರನಿಗೆ ವರುಷ; ದೊಣ್ಣೆಗೆ ನಿಮಿಷ  (figurative)
*EN: A year for the potter; a minute for the club*

- **Gold:** ಒಂದು ವಸ್ತುವನ್ನು ತಯಾರಿಸಲು ತುಂಬಾ ಸಮಯ ಮತ್ತು ಶ್ರಮ ಬೇಕು, ಆದರೆ ಅದನ್ನು ಹಾಳು ಮಾಡಲು ಒಂದು ಕ್ಷಣ ಸಾಕು.
  - *EN: Making a thing takes much time and effort, but a moment is enough to ruin it.*
- **mT0-large** ✗: ದೊಣ್ಣೆಗೆ ವರುಷ; ಕುಂಬಾರನಿಗೆ ನಿಮಿಷ
  - *EN: A year for the stick, a minute for the potter*
- **Qwen3.5-2B** ✓: ಕುಂಬಾರನಿಗೆ ವರುಷ; ದೊಣ್ಣೆಗೆ ನಿಮಿಷ
- **Sarvam-1** ✗: This means that it takes a long time to do something, but you can get it done quickly if you don't care about how much time it takes.

## 166. ಕುರುಡು ಕಣ್ಣಿಗಿಂತ ಮೆಳ್ಳೆಗಣ್ಣು ವಾಸಿ  (figurative)
*EN: A squint eye is better than a blind eye*

- **Gold:** ಏನೂ ಇಲ್ಲದಿರುವುದಕ್ಕಿಂತ ಅಪೂರ್ಣ ಅಥವಾ ಕಡಿಮೆ ಗುಣಮಟ್ಟದ್ದಾದರೂ ಏನಾದರೂ ಇರುವುದು ಲೇಸು.
  - *EN: Having something, even incomplete or of lower quality, is better than having nothing.*
- **mT0-large** ✓: a gray eye is a very healthy eye
- **Qwen3.5-2B** ✓: ಕುರುಡು ಕಣ್ಣಿಗಿಂತ ಮೆಳ್ಳೆಗಣ್ಣು ವಾಸಿ
- **Sarvam-1** ✗: This means that it is better to be a little bit wrong than to be completely right but not know you are wrong.

## 167. ಲೇ ಅನ್ನೋದಕ್ಕೆ ಅವಳೇ ಇಲ್ಲ, ಮಗನ ಹೆಸರು ಮುದ್ದುರಂಗ  (figurative)
*EN: There's no woman to call 'hey', yet the son's name is Muddu-Ranga*

- **Gold:** ಮೂಲಭೂತವಾದದ್ದೇ ಇನ್ನೂ ಇಲ್ಲದಿರುವಾಗ ಮುಂದಿನ ದೊಡ್ಡ ದೊಡ್ಡ ಯೋಜನೆಗಳನ್ನು ಕಟ್ಟಿಕೊಳ್ಳುವವರನ್ನು ಈ ಗಾದೆ ತಮಾಷೆ ಮಾಡುತ್ತದೆ.
  - *EN: This proverb mocks those who build big plans for the future when the basics don't yet exist.*
- **mT0-large** ✓: ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ, ಲೇ,
  - *EN: Le, le, le, le, le... (repetitive gibberish)*
- **Qwen3.5-2B** ✓: ಲೇ ಅನ್ನೋದಕ್ಕೆ ಅವಳೇ ಇಲ್ಲ, ಮಗನ ಹೆಸರು ಮುದ್ದುರಂಗ
- **Sarvam-1** ✓: ಈ proverb ನ ಅರ್ಥ ಏನಂದ್ರೆ, ಒಬ್ಬಳನ್ನ ಬಿಟ್ಟು ಹೋದ್ರೆ ಅವಳು ಹೋಗಿದ್ದಾಳೆ ಅಂತ ಅಲ್ಲ, ಅವಳ ಮಗನೇ ಅವಳನ್ನ ಬಿಟ್ಟು ಹೋದ್ರೆ ಅವಳು ಹೋಗಿದ್ದಾಳೆ ಅಂತ.

## 168. ಲೋಕ ತಿಳಿಯಬೇಕು ಲೆಕ್ಕ ಕಲಿಯಬೇಕು  (literal)
*EN: Know the world, learn accounts*

- **Gold:** ಬದುಕಿನಲ್ಲಿ ಮುಂದೆ ಬರಲು ಜನರ ಮತ್ತು ಜಗತ್ತಿನ ರೀತಿ ತಿಳಿದುಕೊಳ್ಳಬೇಕು ಹಾಗೂ ಹಣದ ಲೆಕ್ಕಾಚಾರ ಕಲಿಯಬೇಕು.
  - *EN: To get ahead in life one must understand the ways of people and the world and learn to account for money.*
- **mT0-large** ✓: ಲೋಕವನ್ನು ತಿಳಿದುಕೊಳ್ಳಲು ಲೆಕ್ಕ ಕಲಿಯಬೇಕು
  - *EN: To understand the world, one must learn arithmetic*
- **Qwen3.5-2B** ✓: ಲೋಕ ತಿಳಿಯಬೇಕು ಲೆಕ್ಕ ಕಲಿಯಬೇಕು
- **Sarvam-1** ✓: This means that people should learn to count and not just rely on their memory. It is a reminder to use logic and reason when making decisions, rather than relying solely on intuition or experience. </s>

## 169. ಲಂಚ ಕೊಟ್ಟು ಮಂಚ ಏರು ವಂಚನೆ ಮಾಡಿ ಕೈಲಾಸ ಏರು  (figurative)
*EN: Give a bribe and climb the cot, cheat and climb Kailasa*

- **Gold:** ಲಂಚ ಕೊಟ್ಟು ಸುಖ ಅಥವಾ ಸ್ಥಾನ ಗಳಿಸುವ, ವಂಚನೆ ಮಾಡಿ ಉನ್ನತಿ ಪಡೆಯುವ ಜನರ ಬಗ್ಗೆ ವ್ಯಂಗ್ಯವಾಗಿ ಹೇಳುವ ಮಾತು.
  - *EN: A sarcastic saying about people who gain comfort or position by bribery and rise through cheating.*
- **mT0-large** ✗: ಲಂಚ ಕೊಟ್ಟು ಮಂಚ ಏರು ವಂಚನೆ ಮಾಡಿ ಕೈಲಾಸ ಏರು
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಲಂಚ ಕೊಟ್ಟು ಮಂಚ ಏರು ವಂಚನೆ ಮಾಡಿ ಕೈಲಾಸ ಏರು
- **Sarvam-1** ✓: This means that you can't get what you want by asking for it, but if you pay someone to give it to you then you will get it.

## 170. ಲಾಭವಿಲ್ಲದ ವ್ಯಾಪಾರ ಕತ್ತೆ ಮೈ ಪರಚಿದಂಗೆ  (figurative)
*EN: Business without profit is like a donkey scratching its body*

- **Gold:** ಲಾಭವೇ ಬರದ ವ್ಯಾಪಾರದಲ್ಲಿ ಎಷ್ಟು ದುಡಿದರೂ ಅದು ಕತ್ತೆಯ ಮೈ ಪರಚಿದಂತೆ, ಶ್ರಮ ಮಾತ್ರ ಉಳಿಯುತ್ತದೆ, ಫಲವಿಲ್ಲ.
  - *EN: In a business that brings no profit, however much one works, it is like a donkey scratching its body: only the effort remains, with no fruit.*
- **mT0-large** ✗: ಲಾಭವಿಲ್ಲದ ವ್ಯಾಪಾರ ಕತ್ತೆ ಮೈ ಪರಚಿದಂಗೆ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಲಾಭವಿಲ್ಲದ ವ್ಯಾಪಾರ ಕತ್ತೆ ಮೈ ಪರಚಿದಂಗೆ
- **Sarvam-1** ✓: This means that if you are not making any money from your business, then it is better to stop and find another job or start a new business.

## 171. ಸೊಪ್ಪಿನ ಸಾರಾದರೂ ಲೆಕ್ಕದ ಮುದ್ದೆ ಉಣಬೇಕು  (figurative)
*EN: Even if it's greens sambar, eat a counted ragi ball*

- **Gold:** ಊಟ ಸಾಮಾನ್ಯವಾದ ಸೊಪ್ಪಿನ ಸಾರು ಆದರೂ ಅಳತೆ ಮೀರದಂತೆ ಲೆಕ್ಕದ ಮುದ್ದೆ ಉಣ್ಣಬೇಕು; ಸಣ್ಣ ವಿಷಯದಲ್ಲೂ ಲೆಕ್ಕ ಮತ್ತು ಮಿತಿ ಇಟ್ಟುಕೊಳ್ಳಬೇಕು.
  - *EN: Even if the meal is a simple greens sambar, one should eat a counted ragi ball without exceeding the measure; keep account and limit even in small matters.*
- **mT0-large** ✓: ಲೆಕ್ಕದ ಮುದ್ದೆ ಉಣಬೇಕು
  - *EN: Should eat the ball (mudde) of accounts (nonsensical)*
- **Qwen3.5-2B** ✓: ಸೊಪ್ಪಿನ ಸಾರಾದರೂ ಲೆಕ್ಕದ ಮುದ್ದೆ ಉಣಬೇಕು
- **Sarvam-1** ✗: This means that you should not be too concerned about small details, but focus on the big picture.

## 172. ಲಿಂಗ ಹರಿದ ಮೇಲೆ ಜಂಗಮನ ಹಂಗೇನು  (figurative)
*EN: After the lingam is torn, what obligation is there to the Jangama?*

- **Gold:** ಒಮ್ಮೆ ಬಂಧ ಕಡಿದು ಹೋದ ಮೇಲೆ ಆ ಬಂಧಕ್ಕೆ ಸಂಬಂಧಿಸಿದ ಋಣ ಅಥವಾ ಕಟ್ಟುಪಾಡು ಇನ್ನು ಇರುವುದಿಲ್ಲ ಎಂಬ ಅರ್ಥ.
  - *EN: Once a bond is severed, the obligation or restriction tied to that bond no longer exists.*
- **mT0-large** ✓: ಲಿಂಗ ಹರಿದ ಮೇಲೆ ಜಂಗಮನ ಹಂಗೇ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಲಿಂಗ ಹರಿದ ಮೇಲೆ ಜಂಗಮನ ಹಂಗೇನು
- **Sarvam-1** ✓: This means that if you lose something important, it's not worth getting upset about. It's better to accept what happened and move on than to keep fighting over it.

## 173. ಮೂರ್ಖನಿಗೆ ದೊಣೆ ಪೆಟ್ಟು ಬುದ್ಧಿವಂತನಿಗೆ ಮಾತಿನ ಪೆಟ್ಟು  (figurative)
*EN: A club blow for the fool, a word blow for the wise*

- **Gold:** ತಿಳುವಳಿಕೆ ಇಲ್ಲದವನು ಹೊಡೆತ ತಿಂದ ಮೇಲೆ ಕಲಿಯುತ್ತಾನೆ, ಬುದ್ಧಿವಂತನಿಗೆ ಒಂದು ಮಾತೇ ಸಾಕು ಎಂಬ ಅರ್ಥ.
  - *EN: One without understanding learns after being beaten; one word is enough for the wise.*
- **mT0-large** ✓: ದೊಣೆ ಪೆಟ್ಟು, வாதம், வாதம்
  - *EN: [Kannada+Tamil mix] Stick blow, argument, argument*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that if you are stupid, then someone will take advantage of your weaknesses and hurt you. If you are smart, then people may try to trick or deceive you because they know how clever you are.

## 174. ಮನೆಗೆ ಮಾರಿ ಊರಿಗೆ ಉಪಕಾರಿ  (figurative)
*EN: A calamity (Mari) at home, a benefactor to the town*

- **Gold:** ಮನೆಯವರಿಗೆ ಕಿರುಕುಳ ಅಥವಾ ತೊಂದರೆಯಾಗಿದ್ದು, ಹೊರಗಿನ ಊರಿನವರಿಗೆ ಮಾತ್ರ ಒಳ್ಳೆಯವನಂತೆ ಕಾಣುವ ವ್ಯಕ್ತಿಯನ್ನು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb describes a person who troubles his family but appears good only to outsiders in town.*
- **mT0-large** ✓: ಊರಿಗೆ ಉಪಕಾರಿ
  - *EN: Benefactor to the village*
- **Qwen3.5-2B** ✓: ಮನೆಗೆ ಮಾರಿ ಊರಿಗೆ ಉಪಕಾರಿ means "A house is a good investment for a family, but a house is not a good investment for a friend."
- **Sarvam-1** ✓: This means that selling something to someone who lives far away is not a good idea because they will be unable to help you when you need them most.

## 175. ಮೇಲೆ ಬಿದ್ದು ಬಂದೋಳು ಮೂರು ಕಾಮಿಗೆ ಕಡೆ  (figurative)
*EN: The one who comes falling on you is last among the three 'kaami'*

- **Gold:** ಯಾರೂ ಕರೆಯದಿದ್ದರೂ ತಾನಾಗಿ ಮೈಮೇಲೆ ಬಿದ್ದು ಬರುವವರಿಗೆ ಬೆಲೆ ಕಡಿಮೆ ಎಂಬ ಅರ್ಥ ಇರಬಹುದು.
  - *EN: It may mean that those who impose themselves uninvited are valued less.*
- **mT0-large** ✗: ಬಿದ್ದುಕೊಂಡ ಜಾಗದಿಂದ ಮೂರು ಕಾಮಿಗಳು
  - *EN: Three lustful men from the place where (someone) lay (nonsensical)*
- **Qwen3.5-2B** ✓: ಮೇಲೆ ಬಿದ್ದು ಬಂದೋಳು ಮೂರು ಕಾಮಿಗೆ ಕಡೆ
- **Sarvam-1** ✓: This means that if you try to do too many things at once, you will fail. It is better to focus on a few important tasks and get them done well than to try to do everything at once. </s>

## 176. ಮೂರು ಬಿಟ್ಟೋಳು ಊರಿಗೆ ದೊಡ್ಡೋಳು  (figurative)
*EN: One who has given up the three is big in the town*

- **Gold:** ನಾಚಿಕೆ, ಮಾನ-ಅಪಮಾನದ ಚಿಂತೆಗಳನ್ನು ಬಿಟ್ಟವನು ಲೋಕದಲ್ಲಿ ಬೇಗ ಮುಂದೆ ಬರುತ್ತಾನೆ, ಎಲ್ಲರ ಮೇಲೆ ಪ್ರಭಾವ ಬೀರುತ್ತಾನೆ.
  - *EN: One who gives up concerns of shame, honor and dishonor gets ahead in the world quickly and influences everyone.*
- **mT0-large** ✗: ಊರಿಗೆ ದೊಡ್ಡ ಜಾಗ
  - *EN: Big place for the village*
- **Qwen3.5-2B** ✓: ಮೂರು ಬಿಟ್ಟೋಳು ಊರಿಗೆ ದೊಡ್ಡೋಳು
- **Sarvam-1** ✓: ಈ proverb ಅಂದ್ರೆ, ಒಂದು ಸಣ್ಣ ವಿಷಯದಿಂದ ದೊಡ್ಡ ಪರಿಣಾಮ ಆಗಬಹುದು ಅಂತ.

## 177. ಮಾಡೋದು ದುರಾಚಾರ, ಮನೆ ಮುಂದೆ ಬೃಂದಾವನ  (figurative)
*EN: Does wrong, but has a Brindavan in front of the house*

- **Gold:** ಒಳಗೆ ಕೆಟ್ಟ ನಡತೆ ಇಟ್ಟುಕೊಂಡು, ಹೊರಗೆ ಧರ್ಮಿಷ್ಠನಂತೆ ತೋರಿಸಿಕೊಳ್ಳುವ ಕಪಟಿಯನ್ನು ಈ ಗಾದೆ ಟೀಕಿಸುತ್ತದೆ.
  - *EN: This proverb criticizes a hypocrite who keeps bad conduct within but shows himself as pious outside.*
- **mT0-large** ✗: ದುರಾಚಾರ, ಮನೆ ಮುಂದೆ ಬೃಂದಾವನ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: The meaning of the proverb is:
- **Sarvam-1** ✓: This means that doing something wrong will lead to bad consequences.

## 178. ಮಾತು ಬಲ್ಲವನಿಗೆ ಜಗಳವಿಲ್ಲ, ಊಟ ಬಲ್ಲವನಿಗೆ ರೋಗವಿಲ್ಲ  (literal)
*EN: One who knows speech has no quarrel; one who knows eating has no disease*

- **Gold:** ಯಾವಾಗ ಹೇಗೆ ಮಾತನಾಡಬೇಕೆಂದು ತಿಳಿದವನಿಗೆ ಜಗಳ ಬರುವುದಿಲ್ಲ, ಏನನ್ನು ಎಷ್ಟು ತಿನ್ನಬೇಕೆಂದು ತಿಳಿದವನಿಗೆ ರೋಗ ಬರುವುದಿಲ್ಲ.
  - *EN: One who knows when and how to speak doesn't get into quarrels; one who knows what to eat and how much doesn't get disease.*
- **mT0-large** ✗: ಊಟ ಬಲ್ಲವನಿಗೆ ರೋಗವಿಲ್ಲ
  - *EN: No disease for one who knows (how to) eat*
- **Qwen3.5-2B** ✓: The proverb means that a person who knows how to speak wisely will not fight, and a person who knows how to cook well will not get sick.
- **Sarvam-1** ✓: This means that if you can communicate well with others and get along with them, then there is no need to fight or argue because everyone will be happy. However, if you cannot communicate effectively with others, it may lead to conflicts and arguments which could cause harm to yourself and those around you.

## 179. ಮಾತು ಮನೆ ಕೆಡಿಸಿತು, ತೂತು ಒಲೆ ಕೆಡಿಸಿತು  (figurative)
*EN: Speech ruined the house, the hole ruined the stove*

- **Gold:** ಯೋಚನೆಯಿಲ್ಲದೆ ಆಡಿದ ಮಾತು ಕುಟುಂಬವನ್ನೇ ಒಡೆಯುತ್ತದೆ, ತೂತು ಬಿದ್ದ ಒಲೆ ಅಡುಗೆಗೆ ಹೇಗೆ ಕೆಡುತ್ತದೋ ಹಾಗೆ ಸಣ್ಣ ದೋಷವೂ ದೊಡ್ಡ ಹಾನಿ ತರುತ್ತದೆ.
  - *EN: Thoughtless speech breaks the family itself; as a stove with a hole is ruined for cooking, even a small defect brings great harm.*
- **mT0-large** ✓: ತೂತು ಒಲೆ ಕೆಡಿಸಿತು
  - *EN: The hole spoiled the stove*
- **Qwen3.5-2B** ✓: The proverb means that a person who speaks without thinking or acts without planning will bring ruin to their own home.
- **Sarvam-1** ✓: This means that words can have a big impact on people and things around us. If we say something carelessly or without thinking about it, it could cause problems for ourselves and others. It's important to think carefully before speaking so that our words are helpful and not harmful.

## 180. ಮದುವೆ ಮಾಡಿ ನೋಡು ಮನೆ ಕಟ್ಟಿ ನೋಡು  (literal)
*EN: Perform a wedding and see, build a house and see*

- **Gold:** ಮದುವೆ ಮಾಡುವುದು ಮತ್ತು ಮನೆ ಕಟ್ಟುವುದು ಎರಡೂ ಎಷ್ಟು ಕಷ್ಟ ಎಂಬುದು ಅವನ್ನು ಸ್ವತಃ ಮಾಡಿದವರಿಗೆ ಮಾತ್ರ ಗೊತ್ತಾಗುತ್ತದೆ.
  - *EN: How hard conducting a wedding and building a house are is known only to those who have done them.*
- **mT0-large** ✗: marriage, house, build
- **Qwen3.5-2B** ✓: The proverb means that a marriage is a temporary arrangement, and one should not be too attached to it, as the house can be built later.
- **Sarvam-1** ✓: This means that you should try things out before making a decision, because it is better to make mistakes than not do something at all.

## 181. ಮದುವೆಯಾಗೋ ಗುಂಡ ಅಂದ್ರೆ ನೀನೇ ನನ್ನ ಹೆಂಡತಿ ಅಂದ  (figurative)
*EN: When told 'Gunda is getting married', he said 'you yourself are my wife'*

- **Gold:** ಹೇಳಿದ ವಿಷಯಕ್ಕೆ ಸಂಬಂಧವೇ ಇಲ್ಲದ ತಮಾಷೆಯ ಅಥವಾ ಅಸಂಗತ ಉತ್ತರ ಕೊಡುವವನನ್ನು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: It seems this proverb refers to one who gives a funny or irrelevant reply unrelated to what was said.*
- **mT0-large** ✗: 'ఆమె కూడా నా మేనేజరు'
  - *EN: [Telugu] 'She is also my manager'*
- **Qwen3.5-2B** ✓: ಮದುವೆಯಾಗೋ ಗುಂಡ ಅಂದ್ರೆ ನೀನೇ ನನ್ನ ಹೆಂಡತಿ ಅಂದ
- **Sarvam-1** ✗: ಈ proverb ನ ಅರ್ಥ "marriage is like a gun" ಅಂತ. ಇದು ಮದುವೆ ಅಂದ್ರೆ ಒಂದು ರೀತಿಯ commitment ಅಥವಾ responsibility ಅಂತ ಹೇಳುತ್ತೆ, ಅದು ನಿಮ್ಮ partner ಜೊತೆ ಇರೋ relationship ಮೇಲೆ effect ಮಾಡುತ್ತೆ.

## 182. ಮುಖ ನೋಡಿ ಮಾರು ಹೋದ, ಗುಣ ನೋಡಿ ದೂರ ಹೋದ  (figurative)
*EN: Smitten on seeing the face, moved away on seeing the character*

- **Gold:** ಹೊರಗಿನ ಸೌಂದರ್ಯಕ್ಕೆ ಮರುಳಾಗಿ ಹತ್ತಿರ ಹೋದವನು, ಒಳಗಿನ ಗುಣ ತಿಳಿದ ಮೇಲೆ ನಿರಾಶನಾಗಿ ದೂರವಾಗುತ್ತಾನೆ.
  - *EN: One who is charmed by outward beauty and goes near becomes disappointed after learning the inner qualities and drifts away.*
- **mT0-large** ✓: When he saw his face, he looked away.
- **Qwen3.5-2B** ✗: The proverb means that one should judge a person's character by their actions rather than by their appearance.
- **Sarvam-1** ✓: This means that you should not judge a person by their appearance or first impression. You need to get to know them better before making any judgments about them.

## 183. ಮನೆಗೆ ಬೆಂಕಿ ಬಿದ್ದಾಗ ಬಾವಿ ತೋಡಿದರಂತೆ  (figurative)
*EN: They dug a well when the house caught fire*

- **Gold:** ಅಪಾಯ ಬಂದ ಮೇಲೆ ಅದಕ್ಕೆ ತಯಾರಿ ಮಾಡಲು ಶುರು ಮಾಡುವುದು ತಡವಾದ ಮತ್ತು ವ್ಯರ್ಥ ಪ್ರಯತ್ನ.
  - *EN: Starting to prepare for a danger after it has come is a late and futile effort.*
- **mT0-large** ✗: ಮನೆಯ ಒಳಗಿನಿಂದ ಬೆಂಕಿ ಬಿದ್ದಾಗ ಬಾವಿ ತೋಡಿದಂತೆ
  - *EN: Like digging a well when fire fell from inside the house*
- **Qwen3.5-2B** ✗: ಮನೆಗೆ ಬೆಂಕಿ ಬಿದ್ದಾಗ ಬಾವಿ ತೋಡಿದರಂತೆ
- **Sarvam-1** ✓: When something bad happens, people try to fix it as quickly and thoroughly as possible. This is because they don't want things to get worse.

## 184. ಮುಳ್ಳಿನಿಂದ ಮುಳ್ಳು ತೆಗೆ, ಹಗೆಯಿಂದ ಹಗೆ ತೆಗೆ  (figurative)
*EN: Remove a thorn with a thorn, remove enmity with enmity*

- **Gold:** ಒಬ್ಬ ಶತ್ರು ಅಥವಾ ತೊಂದರೆಯನ್ನು ಇನ್ನೊಬ್ಬ ಶತ್ರು ಅಥವಾ ಅದೇ ರೀತಿಯ ಸಾಧನದಿಂದ ನಿವಾರಿಸಿಕೊಳ್ಳಬೇಕು.
  - *EN: One enemy or trouble should be removed by another enemy or a similar means.*
- **mT0-large** ✗: a sheep takes a sheep's sheep's sheep
- **Qwen3.5-2B** ✗: The proverb means that one should not try to remove a bad habit or vice by using the same method, as the solution is often worse than the problem.
- **Sarvam-1** ✓: This means that you should not try to get rid of something bad by getting rid of something else bad. It is better to deal with the problem directly and face it head on.

## 185. ಮುಲಾಜಿಗೆ ಬಸುರಾಗಿ ಹೆರೋಕೆ ತಾವಿಲ್ಲ  (figurative)
*EN: Pregnant out of deference, with no place to give birth*

- **Gold:** ಮುಲಾಜಿಗೆ ಸಿಲುಕಿ ಎಲ್ಲದಕ್ಕೂ ಒಪ್ಪಿಕೊಂಡರೆ ಕೊನೆಗೆ ಅದರಿಂದ ಹೊರಬರಲು ದಾರಿಯೇ ಇಲ್ಲದೆ ಸಿಲುಕಿಕೊಳ್ಳಬೇಕಾಗುತ್ತದೆ ಎಂದು ಅರ್ಥೈಸಬಹುದು.
  - *EN: It can be interpreted that if one agrees to everything out of deference, one is finally stuck with no way out.*
- **mT0-large** ✓: """ఇది కూడా చదవండి."""
  - *EN: [Telugu] "Also read this." (web boilerplate)*
- **Qwen3.5-2B** ✗: ಮುಲಾಜಿಗೆ ಬಸುರಾಗಿ ಹೆರೋಕೆ ತಾವಿಲ್ಲ
- **Sarvam-1** ✓: This means that if you are not careful, even a small mistake can lead to big problems.

## 186. ಮುತ್ತು ಒಡೆದರೆ ಹೋಯ್ತು, ಮಾತು ಆಡಿದರೆ ಹೋಯ್ತು  (figurative)
*EN: A pearl once broken is gone, a word once spoken is gone*

- **Gold:** ಒಡೆದ ಮುತ್ತನ್ನು ಮತ್ತೆ ಕೂಡಿಸಲಾಗುವುದಿಲ್ಲ, ಹಾಗೆಯೇ ಒಮ್ಮೆ ಆಡಿದ ಮಾತನ್ನು ಹಿಂದಕ್ಕೆ ಪಡೆಯಲಾಗುವುದಿಲ್ಲ.
  - *EN: A broken pearl cannot be joined again; likewise a word once spoken cannot be taken back.*
- **mT0-large** ✗: When you throw a sweater, you would throw a hat.
- **Qwen3.5-2B** ✓: ಮುತ್ತು ಒಡೆದರೆ ಹೋಯ್ತು, ಮಾತು ಆಡಿದರೆ ಹೋಯ್ತು ಎಂದರೆ, "ಮುತ್ತು ಒಡೆದರೆ ಹೋಯ್ತು" ಎಂದರೆ, "ಮುತ್ತು �
- **Sarvam-1** ✓: This means that once something is broken or lost, it cannot be recovered. It's gone forever.

## 187. ಮಂಗನ ಪಾರುಪತ್ಯ ಮರದ ಟೊಂಗೆ ಮೇಲೆ  (figurative)
*EN: The monkey's rule is on the tree branch*

- **Gold:** ಅಲ್ಪನ ಅಧಿಕಾರ ಅವನ ಸಣ್ಣ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಮಾತ್ರ ನಡೆಯುತ್ತದೆ, ಮರದ ತುದಿಯಲ್ಲಿರುವ ಮಂಗನ ದರ್ಬಾರಿನಂತೆ ಅದಕ್ಕೆ ಭದ್ರತೆಯೂ ಇರುವುದಿಲ್ಲ.
  - *EN: A petty person's authority works only within his small sphere, and like the monkey's court at the top of a tree, it has no security.*
- **mT0-large** ✓: ಟೊಂಗೆ ಮೇಲೆ ಬಿದ್ದ ಮಂಗನ ಪಾರುಪತ್ಯ
  - *EN: The monkey's authority that fell on the branch*
- **Qwen3.5-2B** ✗: ಮಂಗನ ಪಾರುಪತ್ಯ ಮರದ ಟೊಂಗೆ ಮೇಲೆ
- **Sarvam-1** ✗: This means that if you want to get something done, it is better to ask for help from someone who has more power or influence than yourself.

## 188. ಮಾತಿನ ಬೊಮ್ಮ ತೂತಾದ ಮಡಕೆಯ ಪರಿ  (figurative)
*EN: The talkative Brahma is like a pot with holes*

- **Gold:** ಬಹಳ ಮಾತನಾಡುವ ವ್ಯಕ್ತಿ ತೂತಾದ ಮಡಕೆಯಂತೆ ಏನನ್ನೂ, ಗುಟ್ಟನ್ನೂ ಹಿಡಿದಿಟ್ಟುಕೊಳ್ಳಲಾರ.
  - *EN: A very talkative person, like a pot with holes, cannot hold anything, not even a secret.*
- **mT0-large** ✗: ತೂತಾದ ಮಡಕೆ
  - *EN: A pot with a hole*
- **Qwen3.5-2B** ✓: Here is the meaning of the proverb in one short sentence:
- **Sarvam-1** ✓: This means that if you speak too much, your words will be like a heavy burden on others. It is better to keep quiet and not say anything than to make someone else feel bad by speaking out.

## 189. ನಮ್ಮ ಕಣ್ಣು ನಮಗೆ ಕೆಡಿಸಿತು  (figurative)
*EN: Our own eye ruined it for us*

- **Gold:** ನಮ್ಮದೇ ಆಯ್ಕೆ ಅಥವಾ ನಮ್ಮವರಿಂದಲೇ ನಮಗೆ ಹಾನಿ ಆಯಿತು ಎಂಬ ಅರ್ಥ ಇರಬಹುದು.
  - *EN: It may mean that harm came through our own choice or through our own people.*
- **mT0-large** ✗: Our eyes were broken.
- **Qwen3.5-2B** ✓: ನಮ್ಮ ಕಣ್ಣು ನಮಗೆ ಕೆಡಿಸಿತು
- **Sarvam-1** ✓: This means that we should not judge a person by what they look like, because people are more than their appearance.

## 190. ನುಡಿ ಪುರಾತನ ನಡೆ ಕಿರಾತನ  (figurative)
*EN: Speech ancient, conduct that of a Kirata*

- **Gold:** ಮಾತು ಪುರಾಣ ಹೇಳುವ ಸಜ್ಜನರಂತೆ ಇರುತ್ತದೆ, ಆದರೆ ನಡತೆ ಕಿರಾತರಂತೆ ಒರಟು ಮತ್ತು ಕೆಟ್ಟದು; ಹೇಳುವುದು ಒಂದು, ಮಾಡುವುದು ಇನ್ನೊಂದು.
  - *EN: Speech sounds like a virtuous person narrating the Puranas, but conduct is rough and bad like a Kirata (hunter-tribesman); saying one thing and doing another.*
- **mT0-large** ✗: ನುಡಿ ಪುರಾತನ ನಡೆ ಕಿರಾತನ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: ನುಡಿ ಪುರಾತನ ನಡೆ ಕಿರಾತನ means "Silence is the path of the old man, and the path of the new man."
- **Sarvam-1** ✓: This means that old habits die hard, and it is difficult to change them completely.

## 191. ನೀರಿಗೆ ಬಿದ್ದವನಿಗೆ, ಮಳೆ ಏನು? ಚಳಿ ಏನು?  (figurative)
*EN: What is rain, what is cold, to one who has fallen into the water?*

- **Gold:** ಈಗಾಗಲೇ ದೊಡ್ಡ ಕಷ್ಟದಲ್ಲಿ ಮುಳುಗಿರುವವನಿಗೆ ಅದರ ಜೊತೆ ಬರುವ ಸಣ್ಣಪುಟ್ಟ ತೊಂದರೆಗಳು ಹೆಚ್ಚು ಪರಿಣಾಮ ಬೀರುವುದಿಲ್ಲ.
  - *EN: To one already immersed in great trouble, the small troubles that come along with it don't matter much.*
- **mT0-large** ✗: ನೀರಿನಲ್ಲಿ ಬಿದ್ದವನಿಗೆ, ಮಳೆ ಏನು? ಚಳಿ ಏನು?
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ನೀರಿಗೆ ಬಿದ್ದವನಿಗೆ, ಮಳೆ ಏನು? ಚಳಿ ಏನು?
- **Sarvam-1** ✗: This is a common English saying that means "What doesn't kill you makes you stronger." It suggests that people can learn from their mistakes and become wiser because they have faced difficult situations before. The phrase uses two different weather conditions to illustrate this idea - cold weather represents hardship or advers

## 192. ಅಡಿಗೆ ಬಿದ್ದರೂ ಮೂಗು ಮೇಲೆ  (figurative)
*EN: Even fallen underneath, the nose is up*

- **Gold:** ಸೋತರೂ ಅಥವಾ ತಪ್ಪಿ ಬಿದ್ದರೂ ತನ್ನ ಸೋಲನ್ನು ಒಪ್ಪಿಕೊಳ್ಳದೆ ಜಂಭ ಮತ್ತು ಒರಟು ಹಠ ತೋರಿಸುವವನ ಬಗ್ಗೆ ಹೇಳುವ ಮಾತು ಇದು.
  - *EN: A saying about one who, even after losing or falling by mistake, doesn't admit defeat and shows arrogance and rough stubbornness.*
- **mT0-large** ✓: A duck is eating a duck.
- **Qwen3.5-2B** ✗: ಅಡಿಗೆ ಬಿದ್ದರೂ ಮೂಗು ಮೇಲೆ
- **Sarvam-1** ✗: This means that if you are trying to do something, and it is difficult or impossible for you to achieve what you want, then you should not give up but keep trying until you succeed.

## 193. ನಾಯಿ ಬಾಲ ಯಾವಾಲೂ ಡೊಂಕು  (figurative)
*EN: A dog's tail is always crooked*

- **Gold:** ಕೆಟ್ಟ ಸ್ವಭಾವದವನನ್ನು ಎಷ್ಟೇ ತಿದ್ದಲು ಪ್ರಯತ್ನಿಸಿದರೂ ಅವನ ಗುಣ ಬದಲಾಗುವುದಿಲ್ಲ ಎಂದು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: No matter how much one tries to correct a person of bad nature, his nature does not change.*
- **mT0-large** ✓: ಡೊಂಕು ಡೊಂಕು ಡೊಂಕು
  - *EN: Crooked crooked crooked*
- **Qwen3.5-2B** ✓: ನಾಯಿ ಬಾಲ ಯಾವಾಲೂ ಡೊಂಕು
- **Sarvam-1** ✓: This means that if you do something wrong, it will come back to haunt you. It is a warning against repeating mistakes and not learning from them.

## 194. ನಾಯಿ ಬೊಗಳಿದರೆ ದೇವಲೋಕ ಹಾಳೇನು?  (figurative)
*EN: If a dog barks, is heaven ruined?*

- **Gold:** ಕೀಳು ಮನಸ್ಸಿನವರು ಟೀಕಿಸಿದ ಮಾತ್ರಕ್ಕೆ ಶ್ರೇಷ್ಠರಿಗೆ ಅಥವಾ ಒಳ್ಳೆಯ ಕೆಲಸಕ್ಕೆ ಯಾವ ಹಾನಿಯೂ ಆಗುವುದಿಲ್ಲ.
  - *EN: No harm comes to the great, or to a good work, just because petty-minded people criticize.*
- **mT0-large** ✓: God is evil.
- **Qwen3.5-2B** ✗: ನಾಯಿ ಬೊಗಳಿದರೆ ದೇವಲೋಕ ಹಾಳೇನು?
- **Sarvam-1** ✗: This is a very old saying that means if you are angry or upset, it can cause problems for others and yourself. It's like when someone gets mad at another person, they might say something mean to them, which could make things worse between both people. So, this saying encourages

## 195. ನಡತೆ ಕಲಿಯೋದು ಏರುಬಂಡೆ ನಡತೆ ಕೆಡೋದು ಜಾರುಬಂಡೆ  (figurative)
*EN: Learning conduct is an uphill rock, losing conduct is a slide*

- **Gold:** ಒಳ್ಳೆಯ ನಡತೆಯನ್ನು ಕಲಿಯಲು ಬೆಟ್ಟ ಹತ್ತುವಷ್ಟು ಶ್ರಮ ಬೇಕು, ಆದರೆ ಕೆಟ್ಟ ನಡತೆ ಜಾರುಬಂಡೆಯಂತೆ ಬಹಳ ಸುಲಭವಾಗಿ ಬರುತ್ತದೆ.
  - *EN: Learning good conduct takes as much effort as climbing a hill, but bad conduct comes very easily, like a slide.*
- **mT0-large** ✓: ಜಾರುಬಂಡೆ, ಜಾರುಬಂಡೆ
  - *EN: Slide, slide (slippery rock)*
- **Qwen3.5-2B** ✓: ನಡತೆ ಕಲಿಯೋದು ಏರುಬಂಡೆ ನಡತೆ ಕೆಡೋದು ಜಾರುಬಂಡೆ
- **Sarvam-1** ✓: This means that you should learn how to walk on a rocky path, not try to climb it. It's easier and safer for you to start with something easy and then work your way up.

## 196. ನಾಯಿಗೆ ಕೆಲಸವಿಲ್ಲ, ನಿಲ್ಲೋಕೆ ಹೊತ್ತಿಲ್ಲ  (figurative)
*EN: The dog has no work, no time to stand*

- **Gold:** ನಿಜವಾದ ಕೆಲಸವಿಲ್ಲದಿದ್ದರೂ ಸದಾ ಬಿಡುವಿಲ್ಲದವರಂತೆ ಓಡಾಡುತ್ತಾ ಬ್ಯುಸಿಯಾಗಿರುವಂತೆ ತೋರಿಸಿಕೊಳ್ಳುವವರ ಬಗ್ಗೆ ಹೇಳುವ ಮಾತು.
  - *EN: A saying about those who, though they have no real work, run around always acting busy.*
- **mT0-large** ✗: nothing is going to happen to the elephant.
- **Qwen3.5-2B** ✓: ನಾಯಿಗೆ ಕೆಲಸವಿಲ್ಲ, ನಿಲ್ಲೋಕೆ ಹೊತ್ತಿಲ್ಲ ಎಂಬ ಪ್ರಭಾವಕ ಹೇಳಿಕೆಯು, ನಿಲ್ಲುವುದು ಅಥವಾ ಕೆಲಸ ಮಾಡುವುದು ಎಂಬುದು ನಾಯಿಗೆ ಸ
- **Sarvam-1** ✓: This means that if you don't do anything or work hard, then you will not get anywhere. It is a way to say that it is important to be active and take action. </s>

## 197. ನಯಶಾಲಿ ಆದವನು ಜಯಶಾಲಿ ಆದಾನು  (literal)
*EN: One who becomes courteous will become victorious*

- **Gold:** ವಿನಯ ಮತ್ತು ಸೌಜನ್ಯದಿಂದ ನಡೆದುಕೊಳ್ಳುವವನು ಜೀವನದಲ್ಲಿ ಗೆಲುವು ಸಾಧಿಸುತ್ತಾನೆ.
  - *EN: One who behaves with humility and courtesy achieves victory in life.*
- **mT0-large** ✓: ಜಯಶಾಲಿಗಳು ಜಯಶಾಲಿಗಳು
  - *EN: Winners winners*
- **Qwen3.5-2B** ✓: ನಯಶಾಲಿ ಆದವನು ಜಯಶಾಲಿ ಆದಾನು ಎಂದರೆ, "ನಯನು" (new) ಮತ್ತು "ಜಯಶಾಲಿ" (victorious) ಎಂಬ ಪದಗಳನ್ನು ಬಳಸಿ, "ನಯ
- **Sarvam-1** ✓: This means that if you are not smart enough to be a ninja, then you will never win against someone who is smarter than you.

## 198. ನೆಂಟರೆಲ್ಲ ಕರೆ, ಕಂಟಲೆ ಚೀಲಕ್ಕೆ ಕೈ ಹಾಕಬೇಡ  (figurative)
*EN: Invite all the relatives, but don't put your hand into the kantale bag*

- **Gold:** ನೆಂಟರನ್ನೆಲ್ಲ ಕರೆಯಬಹುದು, ಆದರೆ ಸಂಭ್ರಮದ ಹೆಸರಿನಲ್ಲಿ ಹಣದ ಚೀಲಕ್ಕೆ ಮಿತಿಮೀರಿ ಕೈ ಹಾಕಬಾರದು ಎಂಬ ಅರ್ಥದ ಗಾದೆ ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: It seems to be a proverb meaning that you may invite all the relatives, but shouldn't dip excessively into the money bag in the name of celebration.*
- **mT0-large** ✓: ನೆಂಟರೆಲ್ಲ ಕರೆ, ಕಂಟಲೆ ಚೀಲಕ್ಕೆ ಕೈ ಹಾಕಬೇಡಿ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that you should not take everything for granted and be careful about what you have because it might disappear or get lost.

## 199. ನಿಜ ಆಡಿದರೆ ನಿಷ್ಠೂರ  (literal)
*EN: Speaking the truth brings resentment*

- **Gold:** ಸತ್ಯವನ್ನು ನೇರವಾಗಿ ಹೇಳಿದರೆ ಕೇಳಿದವರಿಗೆ ಕೋಪ ಬಂದು ಸಂಬಂಧ ಹಾಳಾಗಬಹುದು.
  - *EN: If you state the truth directly, the listener gets angry and the relationship may be spoiled.*
- **mT0-large** ✗: When you say the truth, you are a fool.
- **Qwen3.5-2B** ✓: Here is the explanation:
- **Sarvam-1** ✓: This means that if you are honest, people will trust and respect you. If you cheat or lie, they won't like you very much.

## 200. ನಿಯತ್ತಿಲ್ಲದವರಿಗೆ ಬರಕತ್ತಿಲ್ಲ  (literal)
*EN: No prosperity for those without honesty*

- **Gold:** ಪ್ರಾಮಾಣಿಕತೆ ಇಲ್ಲದವರಿಗೆ ಅಭಿವೃದ್ಧಿ ಮತ್ತು ಲಾಭ ಸಿಗುವುದಿಲ್ಲ.
  - *EN: Those without honesty get no growth or profit.*
- **mT0-large** ✓: ನಿಯತ್ತಿನಿಲ್ಲದವರಿಗೆ ಬರಕತ್ತಿಲ್ಲ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: Here is the explanation:
- **Sarvam-1** ✓: This means that if you don't have a plan, then you won't be able to achieve anything.

## 201. ಊಟಕ್ಕೆ ಇಲ್ಲದ ಉಪ್ಪಿನಕಾಯಿ, ಮಣ್ಣಿಗೆ ಸಮಾನ  (figurative)
*EN: Pickle that isn't there at mealtime is equal to dirt*

- **Gold:** ಅಗತ್ಯವಿದ್ದ ಸಮಯದಲ್ಲಿ ಸಿಗದ ಸಹಾಯ ಅಥವಾ ವಸ್ತು ಆಮೇಲೆ ಸಿಕ್ಕರೂ ಅದಕ್ಕೆ ಯಾವ ಬೆಲೆಯೂ ಇಲ್ಲ.
  - *EN: Help or a thing not available at the time of need has no value even if it arrives later.*
- **mT0-large** ✗: ಊಟಕ್ಕೆ ಇಲ್ಲದ ಉಪ್ಪಿನಕಾಯಿ, ಮಣ್ಣಿಗೆ ಸಮಾನ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಊಟಕ್ಕೆ ಇಲ್ಲದ ಉಪ್ಪಿನಕಾಯಿ, ಮಣ್ಣಿಗೆ ಸಮಾನ
- **Sarvam-1** ✗: ಊಟಕ್ಕೆ ಇಲ್ಲದ ಉಪ್ಪಿನಕಾಯಿ, ಮಣ್ಣಿಗೆ ಸಮಾನ.

## 202. ಒಂದು ಕಣ್ಣಿಗೆ ಸುಣ್ಣ ಒಂದು ಕಣ್ಣಿಗೆ ಬೆಣ್ಣೆ  (figurative)
*EN: Lime for one eye, butter for the other eye*

- **Gold:** ಇಬ್ಬರಿಗೆ ಒಂದೇ ರೀತಿ ನೋಡದೆ, ಒಬ್ಬರಿಗೆ ಒಲವು ಇನ್ನೊಬ್ಬರಿಗೆ ಕಠಿಣತೆ ತೋರಿಸುವ ಪಕ್ಷಪಾತದ ನಡವಳಿಕೆಯನ್ನು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb describes partial behavior, treating two people differently: favor for one, harshness for the other.*
- **mT0-large** ✓: One eye is a toothbrush.
- **Qwen3.5-2B** ✓: ಒಂದು ಕಣ್ಣಿಗೆ ಸುಣ್ಣ ಒಂದು ಕಣ್ಣಿಗೆ ಬೆಣ್ಣೆ
- **Sarvam-1** ✗: ಈ proverb ನ ಅರ್ಥ ಏನಂದ್ರೆ, ಒಬ್ಬರಿಗೆ ತೊಂದರೆ ಕೊಡೋದು ಅಂದ್ರೆ ಬೇರೆಯವರಿಗೆ ತೊಂದರೆ ಕೊಡಬೇಕು ಅಂತ ಅಲ್ಲ.

## 203. ಒಂದು ಸಿಟ್ಟಿನಲ್ಲಿ ಬಾವಿಗೆ ಬಿದ್ದರೆ, ಏಳು ಸಿಟ್ಟಿನಲ್ಲೂ ಏಳಲಾಗದು.  (figurative)
*EN: If you fall into a well in one fit of anger, you can't get up even in seven fits of anger*

- **Gold:** ಸಿಟ್ಟಿನ ಭರದಲ್ಲಿ ಯೋಚಿಸದೆ ಮಾಡುವ ಕೆಲಸ ತನಗೇ ಹಾನಿ ತರುತ್ತದೆ ಎಂಬ ಅರ್ಥದ ಗಾದೆ ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: It seems to be a proverb meaning that an act done thoughtlessly in a burst of anger harms oneself.*
- **mT0-large** ✗: ಒಂದು ಸಿಟ್ಟಿನಲ್ಲಿ ಬಾವಿಗೆ ಬಿದ್ದರೆ, ಏಳು ಸಿಟ್ಟಿನಲ್ಲಿ ಏರಲಾಗುವುದಿಲ್ಲ.
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಒಂದು ಸಿಟ್ಟಿನಲ್ಲಿ ಬಾವಿಗೆ ಬಿದ್ದರೆ, ಏಳು ಸಿಟ್ಟಿನಲ್ಲೂ ಏಳಲಾಗದು.
- **Sarvam-1** ✓: ಈ proverb ಹೇಳೋದೇನೆಂದರೆ, ನೀವು ಕೋಪದಲ್ಲಿ ಇದ್ದರೆ, ನೀವು ಶಾಂತವಾಗಲು ಸಾಧ್ಯವಿಲ್ಲ. ನೀವು ಕೋಪವನ್ನು ನಿಯಂತ್ರಿಸಲು ಸಾಧ್ಯವಾಗದಿದ್ದರೆ, ಅದು ನಿಮ್ಮನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ ಮತ್ತು ನಿಮ್ಮ ಮೇಲೆ ಪರಿಣಾಮ ಬೀರುತ್ತದೆ.

## 204. ಒಣ ಮರವ ಬೆಂಕಿ ತಿಂತಂತೆ ಹಸಿ ಮರವ ಚಿಂತೆ ತಿಂತಂತೆ  (figurative)
*EN: Fire eats the dry tree, worry eats the green tree*

- **Gold:** ಒಣ ಮರವನ್ನು ಬೆಂಕಿ ತಿನ್ನುವಂತೆ, ಹಸಿರಾಗಿರುವ ಜೀವಂತ ವ್ಯಕ್ತಿಯನ್ನು ಚಿಂತೆ ಒಳಗಿನಿಂದ ಕರಗಿಸುತ್ತದೆ.
  - *EN: Just as fire eats a dry tree, worry melts a living, green person from within.*
- **mT0-large** ✓: ಬಿಸಿಯಾದ ಮರಳಿನ ಹೊಂಡದಲ್ಲಿ ತೇಲುತ್ತಿರುವ ಬೆಂಕಿ, ಹಸಿವಾದ ಮರಳಿನ ಹೊಂಡದಲ್ಲಿ ತೇಲುತ್ತಿರುವ ಕಾಯಿಲೆ, ಕಾಯಿಲೆ, ರೋಗ, ಕಾಯಿಲೆ, ರೋಗ, ಕಾಯಿಲೆ, ರೋಗ
  - *EN: Fire floating in a pit of hot sand, illness floating in a pit of hungry sand, illness, illness, disease, illness, disease... (repetitive, nonsensical)*
- **Qwen3.5-2B** ✓: ಒಣ ಮರವ ಬೆಂಕಿ ತಿಂತಂತೆ ಹಸಿ ಮರವ ಚಿಂತೆ ತಿಂತಂತೆ
- **Sarvam-1** ✓: This means that if you don't take care of something, it will eventually cause problems for you. It is like a dry tree - it can easily catch fire and burn down. Similarly, if you ignore your worries or problems, they may grow bigger and become harder to deal with. </

## 205. ಪಾಲಿಗೆ ಬಂದದ್ದು ಪಂಚಾಮೃತ  (figurative)
*EN: What comes to one's lot is panchamrita*

- **Gold:** ತನ್ನ ಪಾಲಿಗೆ ಏನು ಬಂದಿದೆಯೋ ಅದನ್ನೇ ಪಂಚಾಮೃತದಂತೆ ತೃಪ್ತಿಯಿಂದ ಸ್ವೀಕರಿಸಬೇಕು.
  - *EN: Whatever comes to one's share, one should accept contentedly, like panchamrita (a sweet sacred offering).*
- **mT0-large** ✓: a newspaper written by a man
- **Qwen3.5-2B** ✓: ಪಾಲಿಗೆ ಬಂದದ್ದು ಪಂಚಾಮೃತ
- **Sarvam-1** ✓: This means that if you get something good, it is better to share it with others than keep it for yourself.

## 206. ಪಾಲಿಗೆ ಇಲ್ಲದ್ದು ಏನಾದರೇನು?  (figurative)
*EN: What does it matter what happens to what isn't in one's share?*

- **Gold:** ತನ್ನ ಪಾಲಿಗೆ ಸೇರದ ವಿಷಯ ಏನಾದರೂ ಆಗಲಿ, ಅದರ ಬಗ್ಗೆ ತನಗೆ ಚಿಂತೆ ಇಲ್ಲ ಎಂಬ ಅರ್ಥದ ಗಾದೆ ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: It seems to be a proverb meaning: whatever happens to something that isn't part of my share, I have no worry about it.*
- **mT0-large** ✓: nothing
- **Qwen3.5-2B** ✓: ಪಾಲಿಗೆ ಇಲ್ಲದ್ದು ಏನಾದರೇನು?
- **Sarvam-1** ✓: The proverb means that if you have nothing, then what can you do about it? It is a way to say that there are no excuses for not doing something when you don't have anything to start with. The phrase comes from an old English saying which was used as early as

## 207. ಪಾಪ ಅಂದರೆ ಕರ್ಮ ಬರ್ತದೆ  (figurative)
*EN: Say 'poor thing' and karma comes*

- **Gold:** ಕನಿಕರದಿಂದ ಬೇರೆಯವರ ಕಷ್ಟಕ್ಕೆ ಕೈ ಹಾಕಿದರೆ ಅವರ ತೊಂದರೆ ನಮ್ಮ ಹೆಗಲಿಗೇ ಬೀಳುತ್ತದೆ ಎಂಬ ಅರ್ಥದ ಗಾದೆ ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: It seems to be a proverb meaning that if you step into others' trouble out of pity, their trouble falls on your own shoulders.*
- **mT0-large** ✗: ಪಾಪ అంటే ಕರ್ಮ
  - *EN: [Kannada+Telugu mix] Sin means karma*
- **Qwen3.5-2B** ✗: ಪಾಪ ಅಂದರೆ ಕರ್ಮ ಬರ್ತದೆ
- **Sarvam-1** ✗: This means that if you do something bad, then it will come back to haunt you later on.

## 208. ಪಾಪ ಬರಬಾರದೆಂದು ಶಾಪ ಕೊಂಡ  (figurative)
*EN: Bought a curse so that sin wouldn't come*

- **Gold:** ಪಾಪ ತಟ್ಟಬಾರದೆಂದು ಹೋಗಿ ತಾನೇ ಬೇರೊಂದು ತೊಂದರೆಯನ್ನು ಬೆಲೆ ಕೊಟ್ಟು ತಂದುಕೊಂಡ ಎಂಬ ಅರ್ಥ ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: It seems to mean that in trying to avoid sin, one paid a price and brought another trouble upon oneself.*
- **mT0-large** ✓: ಪಾಪ ಬರಬಾರದೇ ಎಂದು ತಾಯಿ ತಿಳಿಸಿದ್ದಾಳೆ.
  - *EN: Mother has informed: shouldn't sin come?*
- **Qwen3.5-2B** ✓: ಪಾಪ ಬರಬಾರದೆಂದು ಶಾಪ ಕೊಂಡ
- **Sarvam-1** ✓: This means that you should try to avoid doing something bad or wrong, because if you do it then there will be a consequence.

## 209. ಪರರ ಹಂಗಿಸಿ ಮಂಗ ಅನಿಸಿಕೊಂಡ  (figurative)
*EN: Mocked others and got called a monkey*

- **Gold:** ಬೇರೆಯವರನ್ನು ಗೇಲಿ ಮಾಡಿದವನೇ ಕೊನೆಗೆ ತಾನೇ ಅಪಹಾಸ್ಯಕ್ಕೆ ಗುರಿಯಾಗುತ್ತಾನೆ.
  - *EN: One who ridicules others finally becomes the target of ridicule himself.*
- **mT0-large** ✓: 'అతను 'మಂಗ' అయ్యింది.
  - *EN: [Telugu+Kannada mix] 'He became a 'monkey'.*
- **Qwen3.5-2B** ✓: ಪರರ ಹಂಗಿಸಿ ಮಂಗ ಅನಿಸಿಕೊಂಡ
- **Sarvam-1** ✓: This means that you should not put yourself down because someone else is better than you, or worse still, you are better than them. It's important to be proud of your own achievements and work hard for what you want. [/INST]

## 210. ಪ್ರಾಯ ಬರುವಾಗ ಆಯ ತಪ್ಪಿತು  (figurative)
*EN: When youth came, the measure was lost*

- **Gold:** ಯೌವನ ಬರುವ ಹೊತ್ತಿಗೆ ಹತೋಟಿ ಮತ್ತು ವಿವೇಕ ತಪ್ಪಿ ಹೋಗುತ್ತದೆ ಎಂಬುದನ್ನು ಈ ಗಾದೆ ಹೇಳುತ್ತದೆ.
  - *EN: This proverb says that by the time youth arrives, self-control and discretion are lost.*
- **mT0-large** ✗: The age of the bride was a mistake.
- **Qwen3.5-2B** ✗: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that when you are young and have a lot of time to do things, it is easy to make mistakes or bad choices. But as you get older, those mistakes become harder to fix. It's like trying to put out a fire with water - it doesn't work very well

## 211. ಪುಣ್ಯವಂತ ಮುಟ್ಟಿದ್ದೆಲ್ಲ ಚಿನ್ನ  (figurative)
*EN: Everything the virtuous one touches is gold*

- **Gold:** ಭಾಗ್ಯಶಾಲಿ ಏನು ಮಾಡಿದರೂ ಅದರಲ್ಲಿ ಯಶಸ್ಸು ಮತ್ತು ಲಾಭ ಸಿಗುತ್ತದೆ.
  - *EN: Whatever a fortunate person does brings success and profit.*
- **mT0-large** ✗: The wealthy man took all gold.
- **Qwen3.5-2B** ✓: ಪುಣ್ಯವಂತ ಮುಟ್ಟಿದ್ದೆಲ್ಲ ಚಿನ್ನ
- **Sarvam-1** ✓: This means that if you do something good, it will come back to you. It is a way of saying that people who are kind and helpful will be rewarded with happiness or success later on.

## 212. ಪುಟ್ಯಾನ ಜ್ವಾಳ ತೀರಿದರೂ ಹೊಟ್ಯಾನ ಹಾಡು ತೀರಲಿಲ್ಲ  (figurative)
*EN: Though Putya's sorghum is finished, Hotya's song isn't finished*

- **Gold:** ಸಂಪತ್ತು ಖಾಲಿಯಾದರೂ ಆಸೆ ಮತ್ತು ಬೇಡಿಕೆಗಳು ಮುಗಿಯುವುದಿಲ್ಲ ಎಂಬ ಅರ್ಥದ ಗಾದೆ ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: It seems to be a proverb meaning that even when wealth runs out, desires and demands don't end.*
- **mT0-large** ✗: ಗಾಯಕರು ಗಾಯಗೊಂಡ ಹೊಟನಾ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ ಗೀತೆ
  - *EN: Singers, the wounded belly(?) song song song song... (repetitive, nonsensical)*
- **Qwen3.5-2B** ✓: ಪುಟ್ಯಾನ ಜ್ವಾಳ ತೀರಿದರೂ ಹೊಟ್ಯಾನ ಹಾಡು ತೀರಲಿಲ್ಲ
- **Sarvam-1** ✓: This means that even if you have a lot of money, it won't make up for your mistakes or failures. It is like trying to put out a fire with water - it will only cool down the flames but not extinguish them completely.

## 213. ಪುಕ್ಸಟ್ಟೆ ಗಂಡ ಹೊಟ್ಟೆ ತುಂಬ ಉಂಡಾ, ಮನೆ ಗಂಡ ಗಿಣಿಕೊಂಡು ಬಿದ್ದ  (figurative)
*EN: The free husband ate to his belly's fill, the house husband fell down groaning*

- **Gold:** ಹೊರಗಿನವನಿಗೆ ಉಚಿತವಾಗಿ ಭರ್ಜರಿ ಸತ್ಕಾರ ಸಿಕ್ಕರೆ ಮನೆಯವನು ಕಡೆಗಣಿಸಲ್ಪಡುತ್ತಾನೆ ಎಂಬ ಅರ್ಥ ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: It seems to mean that when an outsider gets a lavish free treat, the member of the house is neglected.*
- **mT0-large** ✗: தாய்కు தாய் తల్లిదండ్రులు తమ తల్లిదండ్రుల కోసం గూడు కట్టుకొని ಬಿದ್ದார்கள்.
  - *EN: [Tamil+Telugu+Kannada mix] Mother to mother, parents built a nest for their parents and fell. (nonsensical)*
- **Qwen3.5-2B** ✗: ಪುಕ್ಸಟ್ಟೆ ಗಂಡ ಹೊಟ್ಟೆ ತುಂಬ ಉಂಡಾ, ಮನೆ ಗಂಡ ಗಿಣಿಕೊಂಡು ಬಿದ್ದ
- **Sarvam-1** ✓: This means that if you are not satisfied with your life and have a lot to be grateful for, then it is better to stay happy than try to change something about yourself or others.

## 214. ಪುನಗನ ಬೆಕ್ಕು ತನ್ನ ವಾಸನೆ ಅರಿಯದೆ ಕಾಡೆಲ್ಲ ತಿರುಗಿ ತಿರುಗಿ ಸಾಯ್ತಂತೆ  (figurative)
*EN: The civet cat, not knowing its own scent, is said to wander the whole forest and die*

- **Gold:** ತನ್ನೊಳಗೇ ಇರುವ ಗುಣ ಅಥವಾ ಸಾಮರ್ಥ್ಯವನ್ನು ಅರಿಯದೆ ಹೊರಗೆ ಅದನ್ನು ಹುಡುಕುತ್ತಾ ಅಲೆದಾಡುವವರ ಬಗ್ಗೆ ಈ ಗಾದೆ.
  - *EN: This proverb is about those who, not knowing the quality or ability within themselves, wander outside looking for it.*
- **mT0-large** ✓: ಪುನಗನ ಬೆಕ್ಕು ತನ್ನ ವಾಸನೆ ಅರಿಯದೆ ಕಾಡೆಲ್ಲ ತಿರುಗಿ ತಿರುಗಿ ಸಾಯುತ್ತಾ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಪುನಗನ ಬೆಕ್ಕು ತನ್ನ ವಾಸನೆ ಅರಿಯದೆ ಕಾಡೆಲ್ಲ ತಿರುಗಿ ತಿರುಗಿ ಸಾಯ್ತಂತೆ
- **Sarvam-1** ✗: This means that if you don't pay attention to something, it can cause serious problems for you.

## 215. ಪುರಾಣ ಹೇಳಿದರೆ ಪುಷ್ಪ ಬಿದ್ದಾವೇ?  (figurative)
*EN: If you tell a Purana, will flowers fall?*

- **Gold:** ಬರೀ ಮಾತು, ಉಪದೇಶ ಅಥವಾ ಭಾಷಣದಿಂದ ಯಾವ ಫಲವೂ ಸಿಗುವುದಿಲ್ಲ, ಕೃತಿ ಬೇಕು.
  - *EN: No fruit comes from mere talk, preaching or speeches; action is needed.*
- **mT0-large** ✗: ಪುರಾಣ చెప్పడం వల్ల పుష్పాలు ಬಿದ್ದಾವೇ?
  - *EN: [Kannada+Telugu mix] Have flowers fallen because of telling the Purana?*
- **Qwen3.5-2B** ✗: ಪುರಾಣ ಹೇಳಿದರೆ ಪುಷ್ಪ ಬಿದ್ದಾವೇ? (If the ancient history tells you, will the flowers fall?)
- **Sarvam-1** ✓: This means that if you tell a lie, it will come back to haunt you.

## 216. ಪುಸ್ತಕದಲ್ಲಿರೋ ಬದನೆಕಾಯಿ ಸಾರಿಗೆ ಬಂದಾತೆ?  (figurative)
*EN: Will the brinjal in the book come to the curry?*

- **Gold:** ಪುಸ್ತಕದಲ್ಲಿ ಓದಿದ ಜ್ಞಾನ ಕೈಯಾರೆ ಮಾಡಿ ಅನುಭವ ಪಡೆಯದೆ ನಿಜ ಜೀವನದಲ್ಲಿ ಉಪಯೋಗಕ್ಕೆ ಬರುವುದಿಲ್ಲ.
  - *EN: Knowledge read in a book is not useful in real life without hands-on experience.*
- **mT0-large** ✗: புத்தகத்தில்ರೋ ಬದನೆಕಾಯಿ ಸಾರಿಗೆ ಬಂದారా?
  - *EN: [Tamil+Kannada+Telugu mix] In the book, did the brinjal come for the curry?*
- **Qwen3.5-2B** ✓: ಪುಸ್ತಕದಲ್ಲಿರೋ ಬದನೆಕಾಯಿ ಸಾರಿಗೆ ಬಂದಾತೆ?
- **Sarvam-1** ✓: The proverb means that if you are not careful, something will go wrong even when everything seems to be going well. [/INST]

## 217. ರೀತಿ ತಿಳಿಯದಿದ್ದರೂ ಮಾತು ಬಲ್ಲ  (figurative)
*EN: Though he doesn't know the manner, he knows the talk*

- **Gold:** ನಡವಳಿಕೆಯ ಸರಿಯಾದ ರೀತಿ ತಿಳಿಯದಿದ್ದರೂ ಬೇರೆಯವರಿಗೆ ಬುದ್ಧಿವಾದ ಹೇಳುವುದರಲ್ಲಿ ಮುಂದಿರುವವನ ಬಗ್ಗೆ ಎಂದು ತೋರುತ್ತದೆ.
  - *EN: It seems to be about one who, though not knowing the right way of conduct, is ahead in giving advice to others.*
- **mT0-large** ✓: ರೀತಿಯ ಅರಿವಿಲ್ಲದಿದ್ದರೂ, ಭಾಷೆಯನ್ನು ಬಲ್ಲ
  - *EN: Even without knowing the manner, knows the language*
- **Qwen3.5-2B** ✓: Here is the explanation:
- **Sarvam-1** ✓: This means that even if you don't know what something is, you can still understand it by listening to how people talk about it.

## 218. ರೀತಿಯಲ್ಲದ ಮಾತು ತಲೆ ಬೇನೆ  (figurative)
*EN: Talk without propriety is a headache*

- **Gold:** ಸಂದರ್ಭ ಅಥವಾ ಸಭ್ಯತೆ ಇಲ್ಲದ ಮಾತು ಕೇಳುವವರಿಗೆ ತಲೆನೋವಿನಂತೆ ಕಿರಿಕಿರಿ ಉಂಟುಮಾಡುತ್ತದೆ.
  - *EN: Speech without context or courtesy irritates the listener like a headache.*
- **mT0-large** ✓: ರೀತಿಯ ಮಾತು ತಲೆ ಬೇನೆ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that if you say something without thinking, it can cause problems for yourself or others. It's like saying something that might hurt someone else's feelings or make them upset. So, it's better to think before we speak and choose our words carefully. </s>

## 219. ರೋಗಕ್ಕೆ ಮದ್ದುಂಟು ಶೀಲಕ್ಕೆ ಮದ್ದಿಲ್ಲ  (literal)
*EN: There is medicine for disease, there is no medicine for character*

- **Gold:** ರೋಗಕ್ಕೆ ಔಷಧ ಇದೆ, ಆದರೆ ಕೆಟ್ಟ ನಡತೆ ಅಥವಾ ಶೀಲದ ದೋಷಕ್ಕೆ ಔಷಧವಿಲ್ಲ.
  - *EN: There is medicine for illness, but no medicine for a flaw of bad conduct or character.*
- **mT0-large** ✗: ರೋಗಕ್ಕೆ ಮದ್ದಿಲ್ಲ
  - *EN: No medicine for the disease*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that you can't cure a disease with medicine if your body is not strong enough to fight it off.

## 220. ರೂಪಕ್ಕೆ ಮನಸೋತವರಿಗೆ ಪಾಪಕ್ಕೆ ಭಯವಿಲ್ಲ  (literal)
*EN: Those smitten by beauty have no fear of sin*

- **Gold:** ಸೌಂದರ್ಯಕ್ಕೆ ಮರುಳಾದವರು ತಪ್ಪು ಮಾಡಲು ಹೆದರುವುದಿಲ್ಲ.
  - *EN: Those infatuated by beauty are not afraid of doing wrong.*
- **mT0-large** ✗: ರೂಪಕ್ಕೆ ಮನಸೋತವರಿಗೆ ಪಾಪಪಡುವುದರಲ್ಲಿ ಯಾವುದೇ ಅರ್ಥವಿಲ್ಲ.
  - *EN: For those enamoured by looks, there is no meaning in repenting.*
- **Qwen3.5-2B** ✓: The meaning of the proverb is that people who are focused on their appearance are not afraid of sin.
- **Sarvam-1** ✓: This means that people who are attracted to someone's appearance will not be afraid of their bad characteristics.

## 221. ರಾಜ ಠೀವಿ ತಿರುಬೋಕಿ ಲಕ್ಷಣ  (figurative)
*EN: Royal pomp is the mark of a pauper*

- **Gold:** ಹೊರಗೆ ರಾಜನಂತೆ ದೊಡ್ಡಸ್ತಿಕೆ ತೋರಿಸಿದರೂ ಒಳಗೆ ಭಿಕ್ಷುಕನಂತಹ ಬಡತನ ಇರುವವನ ಬಗ್ಗೆ ಹೇಳುವ ಮಾತು.
  - *EN: A saying about one who shows grandeur like a king outside but has beggar-like poverty within.*
- **mT0-large** ✗: The importance of a king's throne.
- **Qwen3.5-2B** ✓: The proverb "Raja Thievi Tirubokiki Lakshan" (The King's Thievery of the Monkey's Tail) is a metaphor for the **extreme difficulty and futility of trying to control or fix a situation that is already deeply entrenched and beyond one's power to
- **Sarvam-1** ✓: The king is not a man who can be fooled by small tricks, but he will see through them and punish those who try to deceive him.

## 222. ರಾಜ ಇರೋತನಕ ರಾಣಿ ಭೋಗ  (literal)
*EN: As long as the king lives, the queen enjoys*

- **Gold:** ಗಂಡ ಬದುಕಿದ್ದು ದುಡಿದು ಸಲಹುವವರೆಗೆ ಮಾತ್ರ ಹೆಂಡತಿಗೆ ಸುಖ ಸೌಕರ್ಯ ಸಿಗುತ್ತದೆ.
  - *EN: The wife gets comforts and luxuries only as long as the husband lives and earns to support her.*
- **mT0-large** ✓: రాజు ಇರೋತನಕ రాణి ಭೋಗ
  - *EN: [Telugu+Kannada mix] As long as the king is there, the queen enjoys*
- **Qwen3.5-2B** ✓: Here is the explanation:
- **Sarvam-1** ✗: This means that a king's power and authority is greater than any other person or thing, including his wife. The phrase comes from an old English saying which was used to describe how powerful kings were compared to their wives. It also implies that even though a queen may be married to a

## 223. ರತ್ನ ಒಳ್ಳೆದಾದ್ರೆ ಇದ್ದ ಠಾವಿನಲ್ಲೇ ಬೆಳೆಯುತ್ತದೆ  (figurative)
*EN: If the gem is good, it grows in the very place it is*

- **Gold:** ನಿಜವಾದ ಪ್ರತಿಭೆ ಅಥವಾ ಯೋಗ್ಯತೆ ಇರುವವರು ಯಾವ ಸ್ಥಳದಲ್ಲಿದ್ದರೂ ಬೆಳಗುತ್ತಾರೆ.
  - *EN: Those who have real talent or worth shine wherever they are.*
- **mT0-large** ✗: ರತ್ನ ಒಳ್ಳೆಯದಾದ್ರೆ ಇದ್ದ ಠಾವಿನಲ್ಲೇ ಬೆಳೆಯುತ್ತದೆ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: The meaning of the proverb is:
- **Sarvam-1** ✓: This means that if you have something good, it will grow and flourish over time.

## 224. ರತ್ನ ತಿನ್ನೋ ಪಕ್ಷಿ ಕಾಗೆ ಸವಾಸಕ್ಕೆ ಬಿದ್ದು ಎಂಜಲೆಲೆಗೆ ಸೊಬತಿ ಆಗಿತ್ತಂತೆ  (figurative)
*EN: The bird that eats gems fell in with the crow and became a guest at the leftover leaf*

- **Gold:** ಒಳ್ಳೆಯ ಗುಣದವರೂ ಕೆಟ್ಟ ಸಹವಾಸಕ್ಕೆ ಬಿದ್ದರೆ ತಮ್ಮ ಮೌಲ್ಯ ಮತ್ತು ಗೌರವ ಕಳೆದುಕೊಳ್ಳುತ್ತಾರೆ.
  - *EN: Even those of good qualities, if they fall in bad company, lose their value and respect.*
- **mT0-large** ✗: ರತ್ನ ತಿನ್ನೋ ಪಕ್ಷಿ ಕಾಗೆ ಸವಾಸಕ್ಕೆ ಬಿದ್ದು ಎಂಜಲೆಲೆಗೆ ಸೊಬತು అయినప్పుడు
  - *EN: [Kannada+Telugu mix] When the jewel-eating bird falls into the crow's company and becomes friendly(?) with leftover leaf-plates*
- **Qwen3.5-2B** ✓: The meaning of the proverb is:
- **Sarvam-1** ✓: This means that if you try to get something without working for it, then you will end up with nothing.

## 225. ಗೆದ್ದೊನು ಸೋತ, ಸೋತೊನು ಸತ್ತ  (figurative)
*EN: The winner lost, the loser died*

- **Gold:** ಜಗಳ ಅಥವಾ ಮೊಕದ್ದಮೆಯಲ್ಲಿ ಗೆದ್ದವನೂ ಬಹಳ ನಷ್ಟ ಅನುಭವಿಸಿ ಸೋತಂತೆಯೇ ಆಗುತ್ತಾನೆ, ಸೋತವನು ಇನ್ನೂ ಹಾಳಾಗುತ್ತಾನೆ.
  - *EN: Even the one who wins a quarrel or lawsuit suffers great loss and is as good as defeated; the loser is ruined even more.*
- **mT0-large** ✓: ಗೆದ್ದೊನು ಗೆದ್ದ, ಸೋತೊನು ಸತ್ತ
  - *EN: The one who won won, the one who lost died*
- **Qwen3.5-2B** ✓: The proverb means that a person who has already suffered defeat or loss is more likely to be killed or destroyed than one who has not yet faced any adversity.
- **Sarvam-1** ✓: This means that if you win something but lose your temper or get angry at someone for losing it to you, then you will be worse off than before. You have lost what was important to you and gained nothing in return. It is better to accept defeat gracefully and move on without letting anger

## 226. ಶುಭ ನುಡಿಯೋ ಸೋಮ ಅಂದ್ರೆ ಗೂಬೆ ಕಾಣಿಸ್ತಲ್ಲೊ ಮಾವ ಅಂದ  (figurative)
*EN: When told 'say something auspicious, Soma', he said 'an owl is visible, uncle'*

- **Gold:** ಒಳ್ಳೆಯದನ್ನು ಹೇಳು ಎಂದರೂ ಕೆಟ್ಟ ಸೂಚನೆಯ ಮಾತನ್ನೇ ಆಡುವ ಅಪಶಕುನದ ಸ್ವಭಾವದವನ ಬಗ್ಗೆ ಈ ಗಾದೆ.
  - *EN: This proverb is about an ill-omened person who speaks words of bad portent even when asked to say something good.*
- **mT0-large** ✓: 'ಸೋಮ' అంటే 'ಗೋಬೆ ಕಾಣిಸ್ತಲ್ಲ'
  - *EN: [Kannada+Telugu mix] 'Soma' means 'the doll is visible'(?) (broken)*
- **Qwen3.5-2B** ✓: The meaning of the proverb is:
- **Sarvam-1** ✗: This means that if you see a bird with an evil look, then it is likely to be a wolf or other dangerous animal.

## 227. ಸನ್ಯಾಸಿ ಹೆಂಡತಿ ಮುಂಡೇನೂ ಅಲ್ಲ ಮುತ್ತೈದೆನೂ ಅಲ್ಲ  (figurative)
*EN: The ascetic's wife is neither a widow nor a married woman*

- **Gold:** ಸನ್ಯಾಸಿಯ ಹೆಂಡತಿ ವಿಧವೆಯೂ ಅಲ್ಲ, ಸುಮಂಗಲಿಯೂ ಅಲ್ಲ; ಎರಡೂ ಅಲ್ಲದ ಅತಂತ್ರ ಸ್ಥಿತಿಯನ್ನು ಇದು ಸೂಚಿಸುತ್ತದೆ.
  - *EN: The ascetic's wife is neither widow nor a woman whose husband lives; it points to a limbo state of being neither.*
- **mT0-large** ✗: ಸನ್ಯಾಸಿ ಹೆಂಡತಿಗೆ ಮುಂಡೇನೂ ಅಲ್ಲ, ಮುತ್ತೈದೇನೂ ಅಲ್ಲ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಸನ್ಯಾಸಿ ಹೆಂಡತಿ ಮುಂಡೇನೂ ಅಲ್ಲ ಮುತ್ತೈದೆನೂ ಅಲ್ಲ
- **Sarvam-1** ✓: This means that a woman who is not married can still be considered as a good wife and mother, just like a man who is not married can also be considered as a good husband.

## 228. ಸಂಸಾರ ಅನ್ನೋದು ಸಾಗರದ ಹೊಳೆ ಈಜ ಬಲ್ಲವನಿಗೆ ಎದೆದುದ್ದು  (literal)
*EN: Worldly life is a river of the ocean; to one who can swim, it's chest-deep*

- **Gold:** ಸಂಸಾರವೆಂಬ ಸಾಗರವೂ ಈಜು ತಿಳಿದವನಿಗೆ ಎದೆಮಟ್ಟದ ನೀರಷ್ಟೇ; ಜಾಣ್ಮೆ ಇರುವವನಿಗೆ ಸಂಸಾರದ ಕಷ್ಟಗಳು ಸುಲಭ ಎಂದರ್ಥ.
  - *EN: Even the ocean of worldly life is only chest-deep water to one who knows swimming; to the skillful, family troubles are easy.*
- **mT0-large** ✗: జీవితం என்பது சவாலுக்காக எந்தவொரு மனிதரிடமும் எந்த வித உண்மையான జీవితத்தை அனுபவிக்க முடியும்.
  - *EN: [Telugu+Tamil mix] Life is - for a challenge, from any human, one can experience any kind of true life. (broken)*
- **Qwen3.5-2B** ✓: ಸಂಸಾರ ಅನ್ನೋದು ಸಾಗರದ ಹೊಳೆ ಈಜ ಬಲ್ಲವನಿಗೆ ಎದೆದುದ್ದು
- **Sarvam-1** ✓: This means that life is like a river, and you have to swim through it. You can't avoid its currents or waves, but if you know how to swim, you will be able to enjoy your journey.

## 229. ಸಂಸಾರ ಗುಟ್ಟು ವ್ಯಾಧಿ ರಟ್ಟು  (literal)
*EN: Keep family matters secret, disease matters out*

- **Gold:** ಮನೆಯ ಒಳಗಿನ ವಿಷಯಗಳನ್ನು ಗುಟ್ಟಾಗಿಡಬೇಕು, ಆದರೆ ಕಾಯಿಲೆಯನ್ನು ಮುಚ್ಚಿಡದೆ ಬಹಿರಂಗಪಡಿಸಿ ಚಿಕಿತ್ಸೆ ಪಡೆಯಬೇಕು ಎಂದರ್ಥ.
  - *EN: Internal household matters should be kept secret, but illness should not be hidden; it must be disclosed and treated.*
- **mT0-large** ✓: ಸಂಸಾರ గుట్టు ವ್ಯಾಧಿ
  - *EN: [Kannada+Telugu mix] Family secret is a disease*
- **Qwen3.5-2B** ✗: ಸಂಸಾರ ಗುಟ್ಟು ವ್ಯಾಧಿ ರಟ್ಟು
- **Sarvam-1** ✗: This means that there are many things we don't know about life and it is difficult to find out what they are, so we should not worry too much about them.

## 230. ಸಂಸಾರ ಸಾಗರ, ಈಸಬೇಕು ಇದ್ದು ಜೈಸಬೇಕು  (figurative)
*EN: Worldly life is an ocean; one must swim, stay, and win*

- **Gold:** ಸಂಸಾರ ಒಂದು ಸಾಗರ; ಅದರಲ್ಲಿ ಈಜಿ, ಅಲ್ಲೇ ನೆಲೆಸಿ ಕಷ್ಟಗಳನ್ನು ಎದುರಿಸಿ ಗೆಲ್ಲಬೇಕು ಎಂದರ್ಥ.
  - *EN: Worldly life is an ocean; one must swim in it, stay there, face the troubles and win.*
- **mT0-large** ✓: ವಾಸ್ತವವಾಗಿ, ಸಂಸಾರ ಸಾಗರ, ಈಸಬೇಕು ಇದ್ದು ಜೈಸಬೇಕು
  - *EN: Actually, family life is an ocean, one must swim and win in it*
- **Qwen3.5-2B** ✓: ಸಂಸಾರ ಸಾಗರ, ಈಸಬೇಕು ಇದ್ದು ಜೈಸಬೇಕು
- **Sarvam-1** ✓: This means that life is a big ocean and we have to swim through it with all our might. We can't just sit back and relax because there are so many things that need our attention. We must keep moving forward no matter what obstacles come our way.

## 231. ಸಂಸಾರಿ ಸಾವಾಸ ಮಾಡಿ ಸನ್ಯಾಸಿ ಕೆಟ್ಟ  (figurative)
*EN: Associating with a householder spoiled the ascetic*

- **Gold:** ಲೌಕಿಕ ಜನರ ಸಹವಾಸ ಮಾಡಿ ಸಂಯಮದಿಂದಿದ್ದವನೂ ದಾರಿ ತಪ್ಪುತ್ತಾನೆ ಎಂಬುದು ಇದರ ಅರ್ಥ.
  - *EN: By associating with worldly people, even one who was self-controlled goes astray.*
- **mT0-large** ✗: திருமண விழாவில் ಸನ್ಯಾಸಿ கெட்ட
  - *EN: [Tamil+Kannada mix] At the wedding ceremony, the ascetic (sanyasi) spoiled*
- **Qwen3.5-2B** ✗: ಸಂಸಾರಿ ಸಾವಾಸ ಮಾಡಿ ಸನ್ಯಾಸಿ ಕೆಟ್ಟ
- **Sarvam-1** ✓: This means that if you are a person who is not happy with your life, then it's better to be a bad person than to try and change things for yourself.

## 232. ಸನ್ಯಾಸಿಗೆ ಯಾತರ ಕಳವಳ ಅಂದ್ರೆ ಅನ್ನದೊಂದೇ ಕಳವಳ  (figurative)
*EN: Asked what worries an ascetic: the only worry is food*

- **Gold:** ಎಷ್ಟೇ ನಿರ್ಲಿಪ್ತನಾಗಿದ್ದರೂ ಅನ್ನದ ಚಿಂತೆ ಎಲ್ಲರಿಗೂ ಇರುತ್ತದೆ ಎಂದು ಈ ಮಾತು ಹೇಳುತ್ತದೆ.
  - *EN: This saying says that however detached one is, everyone has the worry of food.*
- **mT0-large** ✗: ಸನ್ಯಾಸಿರಿಗೆ ಯಾತರ ಕಳವಳ ಅಂದ್ರೆ ಏನು?
  - *EN: What does 'what worry does an ascetic have' mean?*
- **Qwen3.5-2B** ✓: ಸನ್ಯಾಸಿಗೆ ಯಾತರ ಕಳವಳ ಅಂದ್ರೆ ಅನ್ನದೊಂದೇ ಕಳವಳ
- **Sarvam-1** ✗: This means that a monk is not worried about anything except his food and drink, which shows how little he cares for other things.

## 233. ಸಿರಿ ಸೋಂಕಿದವರ ಪರಿ ಬೇರೆ  (figurative)
*EN: The ways of those touched by wealth are different*

- **Gold:** ಸಂಪತ್ತು ಬಂದವರ ನಡವಳಿಕೆ ಮತ್ತು ವರ್ತನೆ ಬದಲಾಗುತ್ತದೆ, ಅವರು ಮೊದಲಿನಂತೆ ಇರುವುದಿಲ್ಲ ಎಂದರ್ಥ.
  - *EN: The behavior and attitude of those who have come into wealth change; they are not as before.*
- **mT0-large** ✗: ಸಿರಿ ಸೋಂಕಿತರಿಗೆ ರೋಗಿಗಳು ಬೇರೆ
  - *EN: For those infected by wealth, the patients are different (nonsensical)*
- **Qwen3.5-2B** ✗: ಸಿರಿ ಸೋಂಕಿದವರ ಪರಿ ಬೇರೆ
- **Sarvam-1** ✗: This means that people who are sick will not be able to help others, and those who are healthy can do more good for society.

## 234. ಸೊಸೆಗೆ ಮನೆವಾಸ, ಅತ್ತೆಗೆ ಪರವಾಸ  (figurative)
*EN: Home stay for the daughter-in-law, exile for the mother-in-law*

- **Gold:** ಮನೆಯ ಅಧಿಕಾರ ಸೊಸೆಯ ಕೈಗೆ ಹೋಗಿ ಮನೆಯೊಡತಿಯಾಗಿದ್ದ ಅತ್ತೆ ಸ್ವಂತ ಮನೆಯಲ್ಲೇ ಪರಕೀಯಳಂತಾಗುತ್ತಾಳೆ ಎಂದರ್ಥ.
  - *EN: Household authority passes to the daughter-in-law and the mother-in-law, once mistress of the house, becomes like a stranger in her own home.*
- **mT0-large** ✓: Their mother lives in the house, her husband lives in the woods.
- **Qwen3.5-2B** ✗: ಸೊಸೆಗೆ ಮನೆವಾಸ, ಅತ್ತೆಗೆ ಪರವಾಸ
- **Sarvam-1** ✓: This means that a son should be loyal to his mother and respectful towards her. A daughter is expected to do the same for her father. The phrase comes from an old English saying which was used as a warning against disrespecting parents. It has been adapted into modern times to mean that

## 235. ಸ್ವತಂತ್ರ ಹೋಗಿ ಅಸ್ವತಂತ್ರ ಆಯಿತು  (literal)
*EN: Independence went, dependence came*

- **Gold:** ಸ್ವಾತಂತ್ರ್ಯ ಕಳೆದುಕೊಂಡು ಬೇರೊಬ್ಬರ ಹತೋಟಿಗೆ ಒಳಗಾಗಬೇಕಾದ ಸ್ಥಿತಿಯನ್ನು ಇದು ಸೂಚಿಸುತ್ತದೆ.
  - *EN: This indicates a state of losing freedom and coming under another's control.*
- **mT0-large** ✓: freedom is a freedom
- **Qwen3.5-2B** ✓: ಸ್ವತಂತ್ರ ಹೋಗಿ ಅಸ್ವತಂತ್ರ ಆಯಿತು
- **Sarvam-1** ✓: If you try to do something without help, it will not work out well.

## 236. ಸ್ತ್ರೀ ರೂಪವೇ ರೂಪ ಶೃಂಗಾರವೇ ರಸ  (figurative)
*EN: A woman's form is the form, adornment is the rasa*

- **Gold:** ಹೆಣ್ಣಿನ ಸೌಂದರ್ಯವೇ ಶ್ರೇಷ್ಠ ಸೌಂದರ್ಯ, ಅಲಂಕಾರವೇ ಅದರ ರಸ ಎಂದು ಮೆಚ್ಚಿ ಹೇಳುವ ಮಾತು.
  - *EN: A saying admiringly claiming that a woman's beauty is the finest beauty and adornment is its essence (rasa).*
- **mT0-large** ✓: ಸ್ತ್ರೀ ರೂಪವೇ రూప శృಂಗಾರವೇ రస
  - *EN: [Kannada+Telugu mix] Woman's form itself is beauty, adornment itself is flavour (rasa)*
- **Qwen3.5-2B** ✗: ಸ್ತ್ರೀ ರೂಪವೇ ರೂಪ ಶೃಂಗಾರವೇ ರಸ
- **Sarvam-1** ✓: The proverb means that women are beautiful and attractive because they have a feminine form, which is their beauty. It emphasizes the importance of physical appearance in attracting people. </s>

## 237. ಸುಖದ ಮೇಲೆ ದುಃಖ, ದುಃಖದ ಮೇಲೆ ಸುಖ  (literal)
*EN: Sorrow after joy, joy after sorrow*

- **Gold:** ಜೀವನದಲ್ಲಿ ಸುಖದ ನಂತರ ದುಃಖ, ದುಃಖದ ನಂತರ ಸುಖ ಬರುತ್ತಲೇ ಇರುತ್ತದೆ.
  - *EN: In life, sorrow follows joy and joy follows sorrow, again and again.*
- **mT0-large** ✗: ದುಃಖದ ಮೇಲೆ ಸುಖ, ದುಃಖದ ಮೇಲೆ ಸುಖ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that when you are happy, it is easy to forget about your problems and difficulties. But if you have a problem or difficulty, then happiness will not last long because you will be thinking about how bad things are.

## 238. ಸುಳ್ಳು ಹೇಳಿದ್ರು ನಿಜದ ನೆತ್ತಿ ಮೇಲೆ ಹೊಡೆದಂಗೆ ಹೇಳಬೇಕು  (figurative)
*EN: Even if you lie, say it as if hitting the crown of the truth*

- **Gold:** ಸುಳ್ಳು ಹೇಳುವುದಾದರೂ ಎಲ್ಲರೂ ನಂಬುವಂತೆ, ನಿಜವನ್ನೇ ಮೀರಿಸುವಷ್ಟು ಖಚಿತವಾಗಿ ಹೇಳಬೇಕು ಎಂದರ್ಥ.
  - *EN: Even if one must lie, it should be said so firmly, outdoing the truth itself, that everyone believes it.*
- **mT0-large** ✗: 'ಸಣ್ಣ ಧ್ವಜದ ಮೇಲೆ ಹೊಡೆದಂಗೆ ಹೇಳಬೇಕು'
  - *EN: 'Should say it like hitting on a small flag'*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: ಈ proverb ನ ಅರ್ಥ ಏನಂದ್ರೆ, ನೀವು ಸುಳ್ಳು ಹೇಳಿದಾಗ, ಅದು ನಿಮ್ಮನ್ನ ಮಾತ್ರವಲ್ಲ, ಬೇರೆಯವರನ್ನೂ ಕೂಡ ನೋಯಿಸುತ್ತೆ ಅಂತ.

## 239. ಸುಳ್ಳು ದೇವರಿಗೆ ಕಳ್ಳ ಪೂಜಾರಿ  (figurative)
*EN: A false god, a thieving priest*

- **Gold:** ಮೋಸದ ಸಂಸ್ಥೆಗೆ ತಕ್ಕಂತೆ ಮೋಸಗಾರನೇ ಮುಖ್ಯಸ್ಥನಾಗಿರುತ್ತಾನೆ; ಎರಡೂ ನಕಲಿ ಎಂದರ್ಥ.
  - *EN: A fraudulent institution fittingly has a fraudster as its head; both are fake.*
- **mT0-large** ✗: 'దేవుడికి ಸುಳ್ಳು ಹೇಳುವ'
  - *EN: [Telugu+Kannada mix] 'Telling lies to God'*
- **Qwen3.5-2B** ✓: ಸುಳ್ಳು ದೇವರಿಗೆ ಕಳ್ಳ ಪೂಜಾರಿ
- **Sarvam-1** ✗: A priest who worships a false god is like a thief, because he steals from his own people by pretending to be something he's not.

## 240. ಸುಸಾರಕ್ಕೆ (=ಅಪರೂಪಕ್ಕೆ) ಬಸುರಾಗಿವ್ನಿ ಮಿಸುಕಬೇಡ ಗಂಡಯ್ಯ  (figurative)
*EN: I've become pregnant, once in a blue moon; don't move, husband*

- **Gold:** ಅಪರೂಪಕ್ಕೆ ಸಿಕ್ಕ ಅವಕಾಶವನ್ನೇ ನೆಪ ಮಾಡಿಕೊಂಡು ಎಲ್ಲರೂ ತನ್ನನ್ನು ಮುದ್ದಿಸಬೇಕು, ಏನೂ ಕೆಲಸ ಹೇಳಬಾರದು ಎಂದು ನಿರೀಕ್ಷಿಸುವುದು.
  - *EN: Using a rare opportunity as an excuse to expect everyone to pamper one and assign no work.*
- **mT0-large** ✗: 'సుಸಾರಕ್ಕೆ (=ಅಪರೂಪಕ್ಕೆ) ಬಸುರಾಗಿವ್ನಿ ಮಿಸುರಿ ಬೇಡ ಗಂಡಯ್ಯ
  - *EN: [Kannada, starts in Telugu script] 'I am pregnant after a long while (=rarely), don't move (fuss), husband'*
- **Qwen3.5-2B** ✓: ಸುಸಾರಕ್ಕೆ ಬಸುರಾಗಿವ್ನಿ ಮಿಸುಕಬೇಡ ಗಂಡಯ್ಯ
- **Sarvam-1** ✗: This means that you should not be too hard on your husband, because he is human and will make mistakes.

## 241. ಸ್ವಧರ್ಮ ತಪ್ಪದ್ರೂ ಅಧರ್ಮ ಮಾಡಬಾರದು  (literal)
*EN: Even if you miss your own dharma, don't commit adharma*

- **Gold:** ತನ್ನ ಕರ್ತವ್ಯವನ್ನು ಪೂರ್ತಿಯಾಗಿ ಪಾಲಿಸಲು ಆಗದಿದ್ದರೂ ತಪ್ಪು ಅಥವಾ ಅನೀತಿಯ ಕೆಲಸ ಮಾಡಬಾರದು.
  - *EN: Even if one cannot fully follow one's duty, one should not do a wrong or unethical act.*
- **mT0-large** ✓: 'ಸ್ವಧರ್ಮ ತಪ್ಪಿದ್ದರೆ, ಸ್ವಧರ್ಮ ಮಾಡಬಾರದು'
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that you should do what is right even if it's not popular or easy to do, because doing wrong things can have bad consequences.

## 242. ಸ್ವರ್ಗವೂ ತಪ್ಪಿತು ದುರ್ಗವೂ ತಪ್ಪಿತು  (figurative)
*EN: Both heaven and fort were lost*

- **Gold:** ಎರಡೂ ಅವಕಾಶಗಳನ್ನು ಕಳೆದುಕೊಂಡು ಯಾವ ಕಡೆಯೂ ಆಸರೆ ಇಲ್ಲದಂತಾದ ಸ್ಥಿತಿಯನ್ನು ಇದು ಹೇಳುತ್ತದೆ.
  - *EN: It describes a state of having lost both options, with no support on either side.*
- **mT0-large** ✓: The devil is a devil.
- **Qwen3.5-2B** ✓: The proverb means that neither heaven nor earth can be trusted, implying that one should not rely on any authority or source of power.
- **Sarvam-1** ✓: This means that if you do something wrong, even if it is a big mistake or an important thing, there will be consequences. It's like saying "even heaven and hell are not exempt from punishment". [/INST]

## 243. ತಲೆ ತಲೆಗು ಪಟ್ಟ ಹೊಟ್ಟೆಗೆ ಇಲ್ಲದೆ ಕೆಟ್ಟ  (figurative)
*EN: A title for every head, but ruined with nothing for the belly*

- **Gold:** ಎಲ್ಲರಿಗೂ ಬಿರುದು, ಹುದ್ದೆ ಇದ್ದರೂ ನಿಜವಾಗಿ ತಿನ್ನಲು ಅನ್ನವಿಲ್ಲದ ಹೊಳಪು ಮಾತ್ರದ ಸ್ಥಿತಿ ಎಂದರ್ಥ.
  - *EN: A state of mere show: everyone has titles and posts, but there's no food actually to eat.*
- **mT0-large** ✓: """ఇది కూడా చదవండి."""
  - *EN: [Telugu] "Also read this." (web boilerplate)*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that you can't have everything, and if you try to get too much at once, it will not work out well for you.

## 244. ತಬ್ಬಲಿ ತಲೆ ಬೋಲಿಸಿಕೊಂಡರೆ ಆನೆಕಲ್ಲು ಮಳೆ ಬಂತು  (figurative)
*EN: When the orphan shaved his head, hailstones rained*

- **Gold:** ಈಗಾಗಲೇ ಕಷ್ಟದಲ್ಲಿರುವ ದಿಕ್ಕಿಲ್ಲದವನ ಮೇಲೆ ಮತ್ತೊಂದು ಕಷ್ಟ ಬಂದೆರಗುವ ದುರದೃಷ್ಟವನ್ನು ಇದು ಹೇಳುತ್ತದೆ.
  - *EN: It describes the misfortune of another trouble striking one who is already in distress and helpless.*
- **mT0-large** ✗: ಬೋಲಲಿ ತಲೆ ಬೋಲಿಸಿಕೊಂಡರೆ ಆನೆಕಲ್ಲು ಮಳೆಯಾಗಿತ್ತು
  - *EN: If one shaves the head when bald(?), it rained hailstones*
- **Qwen3.5-2B** ✓: The proverb means that if one is arrogant and haughty, bad luck will inevitably strike them.
- **Sarvam-1** ✓: This means that if you are not careful, things can get out of hand quickly and become much worse than they were originally. It is a warning to be cautious when making decisions or taking action. </s>

## 245. ತನ್ನೂರಿನಲ್ಲಿ ಬಾಳಲಾರದವ ಪರೂರಿನಲ್ಲಿ ಬಾಳಾನೇ?  (figurative)
*EN: He who cannot live in his own town, will he live in another's town?*

- **Gold:** ಸ್ವಂತ ಊರಲ್ಲೇ ಯಶಸ್ವಿಯಾಗದವನು ಬೇರೆ ಊರಿಗೆ ಹೋದ ಮಾತ್ರಕ್ಕೆ ಗೆಲ್ಲಲಾರ ಎಂಬುದು ಇದರ ಭಾವ.
  - *EN: The sense: one who hasn't succeeded in his own town won't succeed merely by going to another.*
- **mT0-large** ✗: ತನ್ನೂರಿನಲ್ಲಿ ಬಾಳಲಾರದವ ಪರೂರಿನಲ್ಲಿ ಬಾಳಾನೇ?
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: The proverb asks whether one can grow up in a place where they are not allowed to grow up, implying that one cannot truly grow up in a place where they are not allowed to grow up.
- **Sarvam-1** ✓: This means that you can't keep a good reputation if you don't have it where you live. If you are not respected or liked by people, then they will be less likely to respect and like you when you move away. [/INST]

## 246. ತನ್ನ ಊರಿಗೆ ರಂಗ ಪರ ಊರಿಗೆ ಮಂಗ  (figurative)
*EN: A Ranga in his own town, a monkey in another's town*

- **Gold:** ಸ್ವಂತ ಊರಿನಲ್ಲಿ ದೊಡ್ಡ ಹೀರೋ ಆಗಿರುವವನು ಹೊರಗೆ ಬಂದರೆ ಯಾರೂ ಗುರುತಿಸದ ಸಾಮಾನ್ಯನಾಗುತ್ತಾನೆ ಎಂದರ್ಥ.
  - *EN: One who is a big hero in his own town becomes an unnoticed ordinary person outside.*
- **mT0-large** ✗: ತನ್ನ ಊರಿಗೆ ರಂಗ ಪರ ಊರಿಗೆ ಮಂಗ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: The proverb means that a person should not fight or engage in conflict with their own village or community, as it is better to maintain harmony and peace within one's own group.
- **Sarvam-1** ✓: This means that people are more likely to do something if they have a reason or motivation for doing it, rather than just because they want to do it.

## 247. ಉಪಕಾರಕ್ಕೋಗಿ ಉಪದ್ರ ಬಂತು  (figurative)
*EN: Went to do a favor, trouble came*

- **Gold:** ಸಹಾಯ ಮಾಡಲು ಹೋಗಿ ತಾನೇ ತೊಂದರೆಗೆ ಸಿಲುಕುವ ಪರಿಸ್ಥಿತಿಯನ್ನು ಇದು ಸೂಚಿಸುತ್ತದೆ.
  - *EN: It indicates the situation of getting into trouble oneself while trying to help.*
- **mT0-large** ✓: ಉಪಕಾರಕ್ಕೋಗಿ ಉಪದ್ರ ಬಂತು
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✗: ಉಪಕಾರಕ್ಕೋಗಿ ಉಪದ್ರ ಬಂತು
- **Sarvam-1** ✓: This means that if you do something good for someone, they might get upset with you later on.

## 248. ಉಪವಾಸ ಇರಬಹುದು ಉಪದ್ರ ತಳಲಾಗದು  (literal)
*EN: One can fast, but cannot bear harassment*

- **Gold:** ಹಸಿವಿನ ಕಷ್ಟವನ್ನು ಸಹಿಸಬಹುದು, ಆದರೆ ಇತರರ ಕಿರುಕುಳ ಮತ್ತು ಕಾಟವನ್ನು ಸಹಿಸಲು ಸಾಧ್ಯವಿಲ್ಲ ಎಂದರ್ಥ.
  - *EN: One can bear the hardship of hunger, but cannot bear others' harassment and nuisance.*
- **mT0-large** ✓: hunger is a waste of time
- **Qwen3.5-2B** ✗: ಉಪವಾಸ ಇರಬಹುದು ಉಪದ್ರ ತಳಲಾಗದು
- **Sarvam-1** ✗: This means that you can't always control what happens to you, but you can choose how you react to it.

## 249. ಉರಿದ ಹೊಟ್ಟೆಗೆ ಉಪ್ಪು ತುಂಬಿಸಿದಂಗೆ  (figurative)
*EN: Like filling salt into a burning belly*

- **Gold:** ಈಗಾಗಲೇ ನೊಂದಿರುವವನಿಗೆ ಇನ್ನಷ್ಟು ನೋವು ಕೊಡುವ ಕೆಲಸವನ್ನು ಇದು ಸೂಚಿಸುತ್ತದೆ.
  - *EN: It indicates an act that gives yet more pain to one who is already hurting.*
- **mT0-large** ✗: """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
- **Qwen3.5-2B** ✗: ಉರಿದ ಹೊಟ್ಟೆಗೆ ಉಪ್ಪು ತುಂಬಿಸಿದಂಗೆ
- **Sarvam-1** ✓: This means that if you are angry or upset, it is better to deal with your problems rather than letting them build up inside you and make things worse.

## 250. ವ್ಯವಹಾರಕ್ಕೆ ಯಾವ ವಾರ ಆದ್ರೇನು? ವ್ಯಾಪಾರಕ್ಕೆ ಯಾವ ಪಾರ ಆದ್ರೇನು?  (literal)
*EN: What does the day of the week matter for dealing? What does the time matter for trade?*

- **Gold:** ವ್ಯಾಪಾರ ಆರಂಭಿಸಲು ಶುಭ ದಿನಕ್ಕಾಗಿ ಕಾಯುವ ಅಗತ್ಯವಿಲ್ಲ, ಯಾವ ದಿನವಾದರೂ ಸರಿ ಎಂದರ್ಥ.
  - *EN: There is no need to wait for an auspicious day to start a business; any day will do.*
- **mT0-large** ✗: ಯಾವ ವಾರ ವಾಸ್ತವವಾಗಿ ವಾಸ್ತವವಾಗಿ ವಾಸ್ತವವಾಗಿ ವಾಸ್ತವವಾಗಿ ವಾಸ್ತವವಾಗಿ ವಾಸ್ತವವಾಗಿ ವಾಸ್ತವವಾಗಿ ವಾಸ್ತವವಾಗಿ ವಾಸ್ತವವಾಗಿ ವಾಸ್ತವವಾಗಿ ವಾಸ್ತವವಾಗಿ ವಾಸ್ತವವಾಗಿ ವಾಸ್ತವವಾಗಿ ವಾಸ್ತವವಾಗಿ
  - *EN: Which day actually actually actually actually... (repetitive)*
- **Qwen3.5-2B** ✓: ವ್ಯವಹಾರಕ್ಕೆ ಯಾವ ವಾರ ಆದ್ರೇನು? ವ್ಯಾಪಾರಕ್ಕೆ ಯಾವ ಪಾರ ಆದ್ರೇನು?
- **Sarvam-1** ✓: The proverb is a play on words, as "business" can also mean "work". It's saying that you should always be prepared for anything when it comes to business or work. </s>

## 251. ವಾಲಾಡು ಗೊಂಬೆ ವಲಾಡು ನೀರಿಗೆ ಬಿದ್ದಾಗ ತೇಲಾಡು  (figurative)
*EN: Swaying doll, float when you fall into water*

- **Gold:** ಗೊಂಬೆಯಂತೆ ಹೊಂದಿಕೊಂಡು ಕಷ್ಟಕ್ಕೆ ಬಿದ್ದರೂ ಮುಳುಗದೆ ತೇಲಿ ಮೇಲೆ ಬರುವ ಸ್ವಭಾವವನ್ನು ಇದು ಸೂಚಿಸಬಹುದು.
  - *EN: It may indicate a nature that adapts like a doll and, even when falling into trouble, doesn't sink but floats back up.*
- **mT0-large** ✓: ಗೊಂಬೆ ತೇಲುತ್ತಾ నదికి ಬಿದ್ದప్పుడు ತೇಲುತ್ತಾ
  - *EN: [Kannada+Telugu mix] The doll, floating, when it fell into the river, floating*
- **Qwen3.5-2B** ✓: ವಾಲಾಡು ಗೊಂಬೆ ವಲಾಡು ನೀರಿಗೆ ಬಿದ್ದಾಗ ತೇಲಾಡು
- **Sarvam-1** ✓: This means that when you are trying to do something, if it doesn't work out, don't give up and keep trying. If you quit too soon, you will never succeed.

## 252. ವಲ್ಲದ ಹಸ ಉಣ್ಣದ ಕರ  (figurative)
*EN: A cow that won't, a calf that won't eat*

- **Gold:** ಹಾಲು ಕೊಡಲು ಒಪ್ಪದ ಹಸು ಮತ್ತು ಹಾಲು ಕುಡಿಯಲು ಒಪ್ಪದ ಕರು; ಎರಡೂ ಕಡೆಯವರು ಒಪ್ಪದೆ ಕೆಲಸ ಮುಂದೆ ಹೋಗದ ಸ್ಥಿತಿ.
  - *EN: A cow that won't give milk and a calf that won't drink it; a state where both sides refuse and the matter doesn't move.*
- **mT0-large** ✓: ವಲ್ಲದ ಹಸ ಉಣ್ಣದ ಕರ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ವಲ್ಲದ ಹಸ ಉಣ್ಣದ ಕರ
- **Sarvam-1** ✓: This means that you can't get something without giving up something else. It is a saying about how people often have to give up things they want or need in order to achieve other goals. For example, if someone wants to buy a new car but doesn't have enough money, they might

## 253. ವನ ಹಣ್ಣಾಯ್ತು ಗಿಣಿಯ ಬಾಯಿ ಹುಣ್ಣಾಯ್ತು  (figurative)
*EN: The forest became fruit, the parrot's mouth got ulcers*

- **Gold:** ಹೇರಳವಾಗಿ ಸಿಕ್ಕಿದ್ದನ್ನು ಅತಿಯಾಗಿ ಬಳಸಿ ತಾನೇ ತೊಂದರೆ ತಂದುಕೊಳ್ಳುವುದನ್ನು ಇದು ಸೂಚಿಸಬಹುದು.
  - *EN: It may indicate bringing trouble on oneself by overusing what was found in abundance.*
- **mT0-large** ✓: గిన్నిలు కాయగూరలు
  - *EN: [Telugu] Bowls(?) vegetables*
- **Qwen3.5-2B** ✓: The proverb means that a person who is foolish or foolishly confident will eventually face the consequences of their own actions.
- **Sarvam-1** ✓: This means that if you try to do something difficult, it will be very hard for you and your efforts may not pay off.

## 254. ಯಾರ ಮಾತು ಕೇಳಿ ಯಾಕೆ ಕೆಟ್ಟೀಯಾ? ನನ್ನ ಮಾತು ಕೇಳಿ ಬದುಕು  (literal)
*EN: Why do you get ruined listening to whose words? Listen to me and live*

- **Gold:** ಬೇರೆಯವರ ಮಾತು ಕೇಳಿ ಹಾಳಾಗಬೇಡ, ನನ್ನ ಸಲಹೆ ಕೇಳಿ ಒಳ್ಳೆಯದಾಗಿ ಬದುಕು ಎಂದು ಹಿರಿಯರು ಹೇಳುವ ನೇರ ಸಲಹೆ.
  - *EN: A direct piece of advice from an elder: don't be ruined by listening to others; hear my advice and live well.*
- **mT0-large** ✓: ಯಾರ ಮಾತು ಕೇಳಿ ಬದುಕು
  - *EN: Live by listening to whose words*
- **Qwen3.5-2B** ✗: Here is the explanation:
- **Sarvam-1** ✓: This means that if you listen to someone's advice, it is better for your life than listening to their criticism.

## 255. ಯಾವ ಹುತ್ತದಲ್ಲಿ ಯಾವ ಹಾವಿದೆಯೋ  (figurative)
*EN: Who knows which snake is in which anthill*

- **Gold:** ಹೊರಗೆ ಕಾಣದ ಅಪಾಯ ಎಲ್ಲಿ ಅಡಗಿದೆ ಎಂದು ತಿಳಿಯುವುದಿಲ್ಲ, ಆದ್ದರಿಂದ ಎಚ್ಚರದಿಂದಿರಬೇಕು ಎಂದರ್ಥ.
  - *EN: One cannot know where an unseen danger lies hidden, so one must be careful.*
- **mT0-large** ✓: ಯಾವ ಹುತ್ತದಲ್ಲಿ ಯಾವ ಹಾವಿದೆ?
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: The proverb means that a person's character or nature is determined by their actions and choices, rather than being fixed or predetermined.
- **Sarvam-1** ✓: This means that if you are not careful, someone else will take advantage of your good intentions or kindness. [/INST]

## 256. ಯಾವ ಕಾಲ ತಪ್ಪಿದರೂ ಸಾವು ಕಾಲ ತಪ್ಪುವುದಿಲ್ಲ  (literal)
*EN: Whatever season fails, the season of death never fails*

- **Gold:** ಬೇರೆ ಎಲ್ಲ ಕಾಲಗಳು ತಪ್ಪಿಹೋದರೂ ಸಾವಿನ ಕಾಲ ತಪ್ಪುವುದಿಲ್ಲ, ಸಾವು ಖಂಡಿತ ಬರುತ್ತದೆ.
  - *EN: Even if all other seasons fail, the season of death does not fail; death will surely come.*
- **mT0-large** ✓: Whenever you forget the time, death will not happen.
- **Qwen3.5-2B** ✓: Here is the explanation:
- **Sarvam-1** ✓: This means that no matter how much time passes, death is inevitable and cannot be avoided.

## 257. ಯುದ್ಧಕಾಲದಲ್ಲಿ ಕತ್ತಿ ವರುಸೆ ಕಲ್ತಂತೆ  (figurative)
*EN: Like learning sword-play in the time of war*

- **Gold:** ಅವಶ್ಯಕತೆ ಬಂದಾಗ ಕಲಿಯಲು ಹೋದರೆ ತಡವಾಗುತ್ತದೆ; ಮೊದಲೇ ತಯಾರಿ ಮಾಡಿಕೊಳ್ಳಬೇಕು ಎಂದರ್ಥ.
  - *EN: Trying to learn when the need arises is too late; one must prepare beforehand.*
- **mT0-large** ✗: ಯುದ್ಧಕಾಲದಲ್ಲಿ ಕತ್ತಿ ವರುಸೆ ಕಲ್ತಂತೆ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: The meaning of the proverb is:
- **Sarvam-1** ✗: This means that when you are trying to do something difficult, it is better to try and fail than not to try at all. If you don't try, then you will never know if you could have succeeded or not.

## 258. ಯುಕ್ತಿಯ ಮಾತು ಮಕ್ಕಳಿಂದಾದರೂ ತಿಳುಕೋ  (literal)
*EN: Learn a wise word even from children*

- **Gold:** ಬುದ್ಧಿವಂತಿಕೆಯ ಮಾತು ಯಾರೇ ಹೇಳಿದರೂ, ಮಕ್ಕಳೇ ಹೇಳಿದರೂ, ಕೇಳಿ ತಿಳಿದುಕೊಳ್ಳಬೇಕು.
  - *EN: Wise words should be heard and understood no matter who says them, even children.*
- **mT0-large** ✓: ಮಕ್ಕಳು ನಿಮ್ಮ ಮಗುವಿನ ಹಿತಾಸಕ್ತಿಯ ಮಾತುಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಬಹುದು.
  - *EN: Children can understand the words in your child's interest.*
- **Qwen3.5-2B** ✗: The proverb means that a person's words should be truthful and honest, even if they are spoken by children.
- **Sarvam-1** ✓: This means that children can be very clever and sometimes they will come up with a solution to a problem even if it is not the best way, but this is still better than doing nothing at all.

## 259. ಯೋಗ ಇದ್ದಷ್ಟೇ ಭೋಗ  (literal)
*EN: Enjoyment only as much as destiny allows*

- **Gold:** ಅದೃಷ್ಟದಲ್ಲಿ ಎಷ್ಟು ಬರೆದಿದೆಯೋ ಅಷ್ಟೇ ಸುಖ ಅನುಭವಿಸಲು ಸಿಗುತ್ತದೆ.
  - *EN: One gets to enjoy only as much happiness as is written in one's fortune.*
- **mT0-large** ✓: ಯೋಗ ಯೋಗ ಯೋಗ
  - *EN: Yoga yoga yoga*
- **Qwen3.5-2B** ✓: Here is the meaning of the proverb in one short sentence:
- **Sarvam-1** ✓: This means that if you have a good relationship with your body, then you will be able to enjoy life more fully and easily. If you are unhappy or sick, it is hard to find happiness. [/INST]

## 260. ಯೋಗಿ ತಂದದ್ದು ಯೋಗಿಗೆ, ಭೋಗಿ ತಂದದ್ದು ಭೋಗಿಗೆ  (figurative)
*EN: What the ascetic brought is for the ascetic, what the pleasure-seeker brought is for the pleasure-seeker*

- **Gold:** ಸಂಪಾದಿಸಿದ ಸಂಪತ್ತು ಯಾರ ಕೈಗೆ ಹೋಗುತ್ತದೋ ಅವರ ಸ್ವಭಾವಕ್ಕೆ ತಕ್ಕಂತೆ ವಿನಿಯೋಗವಾಗುತ್ತದೆ ಎಂಬ ಅರ್ಥ.
  - *EN: Earned wealth gets spent according to the nature of whoever's hands it falls into.*
- **mT0-large** ✗: ಯೋಗಿಗೆ ಯೋಗ, ಭೋಗಿಗೆ ಭೋಗಿ
  - *EN: Yoga for the yogi, indulgent one (bhogi) for the indulgent*
- **Qwen3.5-2B** ✓: The proverb means that a person who practices yoga gains the benefits of yoga, while a person who indulges in pleasure gains the benefits of pleasure.
- **Sarvam-1** ✓: This means that what you put into something is what you get out of it. If you work hard and study to become a doctor, then you will be a doctor. If you spend your time watching TV instead of studying, you won't become a doctor.

## 261. ಯೋಗ್ಯತೆ ಅರಿಯದ ದೊರೆ ರೋಗ ಅರಿಯದ ವೈದ್ಯ ಒಂದೇ  (figurative)
*EN: A ruler who doesn't know worth and a doctor who doesn't know disease are the same*

- **Gold:** ಜನರ ಸಾಮರ್ಥ್ಯ ಗುರುತಿಸಲಾಗದ ಆಳುವವನು, ರೋಗ ಗುರುತಿಸಲಾಗದ ವೈದ್ಯನಂತೆ ತನ್ನ ಕೆಲಸದಲ್ಲಿ ವಿಫಲನಾಗುತ್ತಾನೆ.
  - *EN: A ruler who cannot identify people's abilities fails in his work, like a doctor who cannot identify disease.*
- **mT0-large** ✗: ಯೋಗ್ಯತೆಯ ಅರಿಯದ రాజు ರೋಗ ಅರಿಯದ ವೈದ್ಯ
  - *EN: [Kannada+Telugu mix] A king who doesn't know merit, a doctor who doesn't know the disease*
- **Qwen3.5-2B** ✓: The meaning of the proverb is:
- **Sarvam-1** ✓: This means that a person who is not aware of his own weaknesses cannot be expected to help others with their problems.

## 262. ಯಾರೂ ಇಲ್ಲದ ಊರಿಗೆ ಹೋಗಿ ನೀರು ಮಜ್ಜಿಗೆ ಬಯಸಿದಂಗೆ  (figurative)
*EN: Like going to a town where nobody is and wanting water and buttermilk*

- **Gold:** ಯಾರೂ ಇಲ್ಲದ ಕಡೆ ಸಹಾಯ, ಆತಿಥ್ಯ ಸಿಗುತ್ತದೆಂದು ನಿರೀಕ್ಷಿಸುವುದು ವ್ಯರ್ಥ.
  - *EN: It is futile to expect help or hospitality where there is nobody.*
- **mT0-large** ✓: ನೀರು, ಮಜ್ಜಿಗೆ, ಊಟ
  - *EN: Water, buttermilk, meal*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: ಈ proverb ಅಂದ್ರೆ, ನೀವು ಒಂದು ಜಾಗಕ್ಕೆ ಹೋದಾಗ, ಅಲ್ಲಿ ಇರೋ ಜನಗಳ ಜೊತೆ interact ಮಾಡೋಕೆ try ಮಾಡಿ.

## 263. ಯಾರೂ ಇಲ್ಲದ ಮನೆಗೆ ನಾನು ಜೋಗಪ್ಪ ಅಂದ  (figurative)
*EN: To a house where no one is, he said 'I am Jogappa'*

- **Gold:** ತನ್ನನ್ನು ಪ್ರಶ್ನಿಸುವವರು ಇಲ್ಲದ ಕಡೆ ತಾನೇ ದೊಡ್ಡವನಂತೆ ಮೆರೆಯುವುದು.
  - *EN: Strutting about as a big man where there is no one to question him.*
- **mT0-large** ✓: I'm a jerk in a house without anyone.
- **Qwen3.5-2B** ✗: Here is the meaning of the proverb in one short sentence:
- **Sarvam-1** ✓: This means that if you are not doing anything, then nobody will notice or care about what you do.

## 264. ಯಥಾ ರಾಜ ತಥಾ ಪ್ರಜಾ  (literal)
*EN: As the king, so the subjects*

- **Gold:** ರಾಜನು ಹೇಗಿರುತ್ತಾನೋ ಪ್ರಜೆಗಳೂ ಹಾಗೆಯೇ ಇರುತ್ತಾರೆ; ನಾಯಕನ ನಡತೆಯನ್ನು ಜನರು ಅನುಸರಿಸುತ್ತಾರೆ.
  - *EN: As the king is, so are the subjects; people follow the leader's conduct.*
- **mT0-large** ✗: The king is the king.
- **Qwen3.5-2B** ✓: The proverb means that the king and the people are bound by the same laws and rules.
- **Sarvam-1** ✓: This means that a king's actions reflect on his people, and vice versa. It is often used to describe how leaders should behave towards their citizens. [/INST]

## 265. ಅಕ್ಕನ್ ಗಂಡನ ಕೂಡೆ ದುಃಖ ಹೇಳಿದ್ರೆ, ಮಕ್ಕಳು ಮರಿಯ ಬುಟ್ಟು ಬಾ ಅಂದ  (figurative)
*EN: When he told his sorrow to his sister's husband, he said 'leave your children and come'*

- **Gold:** ತನ್ನ ದುಃಖವನ್ನು ತಪ್ಪಾದ ವ್ಯಕ್ತಿಯ ಬಳಿ ಹೇಳಿಕೊಂಡರೆ ಅವನು ತನ್ನ ಸ್ವಾರ್ಥಕ್ಕೆ ತಕ್ಕ ಅನುಚಿತ ಸಲಹೆ ಕೊಡುತ್ತಾನೆ.
  - *EN: If you tell your sorrow to the wrong person, he gives improper advice suited to his own selfishness.*
- **mT0-large** ✗: ಮಕ್ಕಳು ಮರಿಯ ಬುಟ್ಟು ಬಾ
  - *EN: Children, leave the young ones and come*
- **Qwen3.5-2B** ✗: ಅಕ್ಕನ್ ಗಂಡನ ಕೂಡೆ ದುಃಖ ಹೇಳಿದ್ರೆ, ಮಕ್ಕಳು ಮರಿಯ ಬುಟ್ಟು ಬಾ ಅಂದ
- **Sarvam-1** ✓: This means that if you tell your husband about something bad happening to you, he will feel sad and may not be able to help you as much as he would otherwise.

## 266. ಕುಂಬಳ ಕಾಯ ಸಾಕಿ ಹಂಡಿಗೆ ಕೊಟ್ಟಂಗೆ  (figurative)
*EN: Like raising a pumpkin and giving it to the pot-maker*

- **Gold:** ಶ್ರಮಪಟ್ಟು ಬೆಳೆಸಿದ್ದರ ಫಲ ಅದಕ್ಕೆ ಅರ್ಹರಲ್ಲದವರ ಪಾಲಾಗುವುದು.
  - *EN: The fruit of what one raised with effort goes to those who don't deserve it.*
- **mT0-large** ✓: తమ పాదాలకు కూడా పాదాలు పెడతారు.
  - *EN: [Telugu] They place feet even on their own feet. (nonsensical)*
- **Qwen3.5-2B** ✓: ಕುಂಬಳ ಕಾಯ ಸಾಕಿ ಹಂಡಿಗೆ ಕೊಟ್ಟಂಗೆ
- **Sarvam-1** ✓: This means that if you give a little to someone, they will be more likely to give you something back.

## 267. ಸತ್ತ ಮೇಲೆ ಎತ್ತ ಹೋದ್ರೇನ ?  (figurative)
*EN: After death, what if he went anywhere?*

- **Gold:** ಎಲ್ಲವೂ ಕೈಮೀರಿ ಹೋದ ಮೇಲೆ ಪಶ್ಚಾತ್ತಾಪ ಪಟ್ಟು ಅಥವಾ ಎಲ್ಲಿ ಹೋದರೂ ಪ್ರಯೋಜನವಿಲ್ಲ ಎಂಬ ಅರ್ಥ.
  - *EN: The sense: after everything has gone beyond reach, regret, or going anywhere, is of no use.*
- **mT0-large** ✓: They went to the hospital .
- **Qwen3.5-2B** ✓: ಸತ್ತ ಮೇಲೆ ಎತ್ತ ಹೋದ್ರೇನ ?
- **Sarvam-1** ✓: This means that you can't take your problems with you when you die, and they will follow you wherever you go. [/INST]

## 268. ಸತ್ತ ಕೋಳಿ ಬತ್ತ ಮುಕ್ಕುತದೆ?  (figurative)
*EN: Will a dead hen peck at paddy?*

- **Gold:** ಈಗಾಗಲೇ ನಿಶ್ಶಕ್ತನಾದವನು ಅಥವಾ ಮುಳುಗಿದವನು ಯಾರಿಗೂ ಹಾನಿ ಮಾಡಲಾರ.
  - *EN: One who is already powerless or sunk cannot harm anyone.*
- **mT0-large** ✗: The dead rabbit is a lion.
- **Qwen3.5-2B** ✓: ಸತ್ತ ಕೋಳಿ ಬತ್ತ ಮುಕ್ಕುತದೆ?
- **Sarvam-1** ✓: This is a common English saying that means "Don't waste your time on things you can't change." It comes from an old story about a chicken who was killed and then cooked, only to find out it had been dead for quite some time. The chicken didn't realize its mistake

## 269. ಗೊಲ್ಲರು ಮಠ ಕಟ್ಟಿದಂಗೆ  (figurative)
*EN: Like the herdsmen building a monastery*

- **Gold:** ತನ್ನ ಹಿನ್ನೆಲೆ ಮತ್ತು ಅರ್ಹತೆಗೆ ಹೊಂದದ ದೊಡ್ಡ ಕೆಲಸಕ್ಕೆ ಕೈ ಹಾಕಿ ಹಾಸ್ಯಾಸ್ಪದವಾಗುವುದು.
  - *EN: Taking on a big undertaking that doesn't suit one's background and qualifications and becoming a laughing stock.*
- **mT0-large** ✗: ಗೊಲ್ಲರು మಠ కట్టిన
  - *EN: [Kannada+Telugu mix] The cowherds (Gollas) who built a monastery (matha)*
- **Qwen3.5-2B** ✓: The proverb "ಗೊಲ್ಲರು ಮಠ ಕಟ್ಟಿದಂಗೆ" (Gollaru Matha kattidanga) means that the people who built the temple were not the ones who were killed, but rather the people who were killed were the ones who built the temple.
- **Sarvam-1** ✓: This means that if you try to do something without any preparation or planning, it will probably not work out well. It's like trying to build a house with no foundation - it won't stand up for long!

## 270. ಗಂಡು ಗುಂಡು, ಹೆಣ್ಣು ಹೆಳವು  (figurative)
*EN: The male is a boulder, the female is lame*

- **Gold:** ಒಬ್ಬರು ತಮ್ಮ ನಿಲುವಿನಲ್ಲಿ ಕಲ್ಲಿನಂತೆ ಗಟ್ಟಿ, ಇನ್ನೊಬ್ಬರು ಸಂದರ್ಭಕ್ಕೆ ತಕ್ಕಂತೆ ಬಗ್ಗುವವರು ಎಂಬ ಅರ್ಥವಿರಬಹುದು.
  - *EN: It may mean that one is rock-firm in his stand and the other yields to circumstances.*
- **mT0-large** ✗: The man is a soldier.
- **Qwen3.5-2B** ✓: The proverb "Gandhu Gundu, Hennu Helavu" means that a man's wife is like a snake, and a woman's husband is like a snake, implying that both partners are dangerous and potentially harmful to the other.
- **Sarvam-1** ✓: This means that a man is like a gun and a woman is like a bullet. A gun can be used to kill someone or it can also be used for protection. Similarly, a woman can be used for good things such as love and caring but she can also be used for bad things

## 271. ಗಂಡಸು ಕೂತು ಕೆಟ್ಟ, ಹೆಂಗಸು ತಿರುಗಿ ಕೆಟ್ಟಳು  (figurative)
*EN: The man ruined by sitting, the woman ruined by wandering*

- **Gold:** ಗಂಡು ಸೋಮಾರಿತನದಿಂದ, ಹೆಣ್ಣು ಅತಿಯಾದ ಲಘು ವರ್ತನೆ ಅಥವಾ ಹರಟೆ-ನಗುವಿನಿಂದ ಹಾಳಾಗುತ್ತಾರೆ ಎಂಬ ಅರ್ಥ.
  - *EN: Men are ruined by laziness, women by excessive frivolity or gossip and laughter.*
- **mT0-large** ✓: The man was a bad man, and the woman was a bad woman.
- **Qwen3.5-2B** ✓: The proverb means that a man who is idle and unproductive is considered bad, while a woman who is idle and unproductive is also considered bad.
- **Sarvam-1** ✓: This means that if a man is bad or does something wrong, his wife will be worse than him.

## 272. ಗಂಡ ಇದ್ದಾಗ ಬುದ್ಧಿ ಇಲ್ಲ, ಬುದ್ಧಿ ಬಂದಾಗ ಗಂಡ ಇಲ್ಲ  (figurative)
*EN: When the husband was there, no sense; when sense came, no husband*

- **Gold:** ಅವಕಾಶ ಅಥವಾ ಸಹಾಯ ಇದ್ದಾಗ ಅದರ ಮೌಲ್ಯ ತಿಳಿಯದೆ, ತಿಳಿದಾಗ ಅದು ಕೈತಪ್ಪಿ ಹೋಗಿರುತ್ತದೆ.
  - *EN: When an opportunity or help is there, its value isn't understood; when it is, it has slipped away.*
- **mT0-large** ✓: When the man is a man, he is not a man.
- **Qwen3.5-2B** ✓: The proverb means that a man's intelligence is often overshadowed by his physical presence, and conversely, a man's wisdom is frequently overshadowed by his physical presence.
- **Sarvam-1** ✓: This means that when a man is around, he can be stupid and not think things through; but once his wife leaves him, he will suddenly become very smart and make good decisions.

## 273. ಹರಟೆ ಇಲ್ಲದೆ ಸಂಜೆ ಆಗದು, ಸಂಗತಿ ಇಲ್ಲದೆ ದಾರಿ ಸವೆಯದು  (figurative)
*EN: Evening doesn't come without chatter, the road doesn't wear out without company*

- **Gold:** ಮಾತುಕತೆ, ಒಡನಾಟ ಇದ್ದರೆ ಸಮಯ ಮತ್ತು ದಾರಿ ಸುಲಭವಾಗಿ ಕಳೆಯುತ್ತದೆ ಎಂಬ ಅರ್ಥ.
  - *EN: With conversation and company, time and the road pass easily.*
- **mT0-large** ✓: 'హರಟೆ ಇಲ್ಲದೆ ಸಂಜೆ ಆಗదు, 'ప్రపంచం சவுத்'
  - *EN: [Telugu+Kannada+Tamil mix] 'Without chatter the evening doesn't come, 'world ... (broken)'*
- **Qwen3.5-2B** ✓: ಹರಟೆ ಇಲ್ಲದೆ ಸಂಜೆ ಆಗದು, ಸಂಗತಿ ಇಲ್ಲದೆ ದಾರಿ ಸವೆಯದು
- **Sarvam-1** ✓: This means that you can't have a good time without having something to do or talk about with other people. It also suggests that if you don't spend your time doing things together with others, then you will end up alone and bored.

## 274. ಬೆಕ್ಕಿಗೆ ಚೆಲ್ಲಾಟ ಇಲಿಗೆ ಪ್ರಾಣ ಸಂಕಟ  (figurative)
*EN: Play for the cat, mortal agony for the mouse*

- **Gold:** ಒಬ್ಬರಿಗೆ ಆಟ ಅಥವಾ ತಮಾಷೆಯಾದದ್ದು ಇನ್ನೊಬ್ಬರಿಗೆ ಜೀವ ಹೋಗುವಷ್ಟು ಸಂಕಟ.
  - *EN: What is play or fun for one is life-threatening agony for another.*
- **mT0-large** ✓: The elephant is a lion.
- **Qwen3.5-2B** ✓: ಬೆಕ್ಕಿಗೆ ಚೆಲ್ಲಾಟ ಇಲಿಗೆ ಪ್ರಾಣ ಸಂಕಟ
- **Sarvam-1** ✓: This means that if you try to trick someone, they will get angry and hurt themselves. It's better to be honest with people than trying to deceive them. [/INST]

## 275. ಸವಿ ಕಂಡ ಕೋತಿ ಅಟ್ಟ ಹತ್ತಿದಂಗೆ  (figurative)
*EN: Like the monkey that tasted sweetness climbing the loft*

- **Gold:** ಒಮ್ಮೆ ಲಾಭ ಅಥವಾ ಸುಖದ ರುಚಿ ಕಂಡವನು ಮತ್ತೆ ಮತ್ತೆ ಅದೇ ಕಡೆ ಹೋಗುತ್ತಾನೆ.
  - *EN: One who has once tasted profit or pleasure goes back to the same place again and again.*
- **mT0-large** ✓: ತನ್ನ ಮಗನನ್ನು ಬೈಸಿ ಬಿದ್ದ ಸವಾರಿಯ மேல் ಬಿದ್ದ ಸವಾರಿಯ மேல் ಬಿದ್ದ ಸವಾರಿಯ மேல் ಬಿದ್ದ ಸವಾರಿಯ மேல் ಬಿದ್ದ ಸವಾರಿಯ மேல் ಬಿದ್ದ ಸವಾರಿಯ மேல் ಬಿದ್ದ ಸವಾರಿಯ மேல் ಬಿದ್ದ
  - *EN: [Kannada+Tamil mix] Making his son get scolded, on the fallen ride, on the fallen ride... (repetitive)*
- **Qwen3.5-2B** ✓: ಸವಿ ಕಂಡ ಕೋತಿ ಅಟ್ಟ ಹತ್ತಿದಂಗೆ
- **Sarvam-1** ✓: This means that if you see something once, it is easy to believe and do not think about whether or not it is true. It's like a monkey who has seen a banana before and thinks he can climb up onto a tree just by looking at it. He doesn't

## 276. ಕೊಟ್ಟ ಸಾಲವ ಕೇಳದೆ ಕೆಟ್ಟ, ಬಿತ್ತಿದ ಹೊಲವ ನೋಡದೆ ಕೆಟ್ಟ  (figurative)
*EN: Ruined by not asking for the loan given, ruined by not looking at the field sown*

- **Gold:** ಸಾಲ ಕೊಟ್ಟು ವಸೂಲಿ ಮಾಡದಿರುವುದು, ಬಿತ್ತಿ ಹೊಲದ ಕಾಳಜಿ ವಹಿಸದಿರುವುದು ನಷ್ಟಕ್ಕೆ ಕಾರಣ; ಮಾಡಿದ ವ್ಯವಹಾರದ ಮೇಲೆ ನಿಗಾ ಬೇಕು.
  - *EN: Not collecting a loan given and not caring for a sown field cause loss; one must keep watch over one's dealings.*
- **mT0-large** ✓: ನಿಮ್ಮ ಊಹೆಯನ್ನು ಕೇಳದೆ ಕೆಟ್ಟ, ಬಿತ್ತ ಹೊಲದ ಹೊಲದ ನೋಡದೆ ಕೆಟ್ಟ
  - *EN: Ruined by not asking your guess, ruined by not looking at the sown field field*
- **Qwen3.5-2B** ✗: Here is the explanation in one short sentence:
- **Sarvam-1** ✗: This means that if you don't pay back a loan or repay your debt, then you will be punished for it later on. It is like planting seeds without watering them first - they won't grow well and may even die. Similarly, not paying back a loan can lead

## 277. ಕೈಯಾಗೆ ಕನ್ನಡಿ ಇಟ್ಕೊಂಡು ನೀರಾಗೆ ಮುಖ ನೋಡ್ದಂಗೆ  (figurative)
*EN: Like keeping the mirror in the hand and looking for the face in the water*

- **Gold:** ಹತ್ತಿರದಲ್ಲೇ ಇರುವುದನ್ನು ಗಮನಿಸದೆ ದೂರದಲ್ಲಿ ಹುಡುಕುವುದು.
  - *EN: Searching far away without noticing what's close at hand.*
- **mT0-large** ✗: ನಿಮ್ಮ ಕೈಯಲ್ಲಿ ಕನ್ನಡಿ ಇಟ್ಕೊಂಡು ನೀರಾ ಮುಖ ನೋಡ್ದಂಗೆ
  - *EN: Like holding a mirror in your hand and looking at the face in water(?)*
- **Qwen3.5-2B** ✓: ಕೈಯಾಗೆ ಕನ್ನಡಿ ಇಟ್ಕೊಂಡು ನೀರಾಗೆ ಮುಖ ನೋಡ್ದಂಗೆ
- **Sarvam-1** ✓: This means that you can't see yourself clearly until someone else points it out to you. [/INST]

## 278. ಕೈಗೆ ಬಂದದ್ದು ಬಾಯಿಗೆ ಇಲ್ಲ  (figurative)
*EN: What came to the hand did not reach the mouth*

- **Gold:** ಕೈಗೆ ಸಿಗುವ ಹಂತಕ್ಕೆ ಬಂದ ಲಾಭ ಅಥವಾ ಅವಕಾಶ ಕೊನೆ ಕ್ಷಣದಲ್ಲಿ ತಪ್ಪಿಹೋಗುವುದು.
  - *EN: A gain or opportunity that had come within reach slips away at the last moment.*
- **mT0-large** ✓: The word "hand" is not written in the mouth.
- **Qwen3.5-2B** ✗: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that if you try to do something, but it doesn't work out for you, then you shouldn't be too disappointed or upset about it. You should just move on and keep trying.

## 279. ಕುಂಟು ಅತ್ತವಗೆ ಕುಂಟು ಅಳು, ನಿಂತ ಅತ್ತವಗೆ ನಿಂತ ಅಳು  (figurative)
*EN: A lame cry for one who cries lame, a standing cry for one who cries standing*

- **Gold:** ಪ್ರತಿಯೊಬ್ಬರೂ ತಮ್ಮ ತಮ್ಮ ಸ್ಥಿತಿಗೆ ತಕ್ಕಂತೆ ದೂರು ಅಥವಾ ನೆಪ ಹೇಳುತ್ತಾರೆ ಎಂಬ ಅರ್ಥವಿರಬಹುದು.
  - *EN: It may mean that everyone makes their own complaint or excuse to suit their own condition.*
- **mT0-large** ✓: 'ಅಲ್ಲೆ' ಎಂದು ಕರೆಯಲ್ಪಡುವ ಆರ್ಥವಾದ ಅಳು, ಅಲ್ಲೆ' ಎಂದು ಕರೆಯಲ್ಪಡುವ ಅಳು, ಅಲ್ಲೆ' ಎಂದು ಕರೆಯಲ್ಪಡುವ ಅಳು, ಅಲ್ಲೆ' ಎಂದು ಕರೆಯಲ್ಪಡುವ ಅಳು, ಅಲ್ಲೆ' ಎಂದು ಕರೆಯ
  - *EN: 'Alle', the meaningful crying called 'alle', crying called 'alle', crying called 'alle'... (repetitive)*
- **Qwen3.5-2B** ✓: ಕುಂಟು ಅತ್ತವಗೆ ಕುಂಟು ಅಳು, ನಿಂತ ಅತ್ತವಗೆ ನಿಂತ ಅಳು
- **Sarvam-1** ✓: This means that if you are angry with someone and don't do anything about it, then your anger will grow stronger and make you feel worse than before. It is better to deal with problems quickly and calmly so they don't get out of hand.

## 280. ಕುರುಡನಿಗೆ ಹಗಲೇನು? ಇರುಳೇನು?  (figurative)
*EN: What is day to a blind man? What is night?*

- **Gold:** ವಿವೇಕ ಅಥವಾ ಜವಾಬ್ದಾರಿ ಅರಿಯದವನಿಗೆ ಯಾವ ಸಮಯ, ಸಂದರ್ಭವೂ ಒಂದೇ; ಹೇಳಿ ಪ್ರಯೋಜನವಿಲ್ಲ.
  - *EN: To one who doesn't understand sense or responsibility, every time and occasion is the same; telling him is useless.*
- **mT0-large** ✗: ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ ಕತ್ತಲಿನಲ್ಲಿ
  - *EN: In the darkness, in the darkness, in the darkness... (repetitive)*
- **Qwen3.5-2B** ✓: The proverb asks, "What is the morning for a dog? What is the evening for a dog?" implying that a dog has no concept of time or the passage of days.
- **Sarvam-1** ✓: The proverb means that you can't see what is right under your nose, so don't expect to find something when you are looking for it. It also means that if you want to do something, you should look for it and not just assume that it will happen.

## 281. ಚಿಕ್ಕವನಾದ್ರು ಶಿವನ ಬುದ್ಧಿ  (figurative)
*EN: Though small, Shiva's wisdom*

- **Gold:** ವಯಸ್ಸಿನಲ್ಲಿ ಚಿಕ್ಕವನಾದರೂ ತಿಳುವಳಿಕೆ ಮತ್ತು ವಿವೇಕದಲ್ಲಿ ಹಿರಿಯನಂತೆ ಇರುವವನು.
  - *EN: One who, though small in age, is like an elder in understanding and discernment.*
- **mT0-large** ✗: ಚಿಕ್ಕವನಾದ್ರು ಶಿವನ ಬುದ್ಧಿ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: The meaning of the proverb is:
- **Sarvam-1** ✓: This means that a child is very smart and can learn things quickly, just like how Shiva was known to be wise even as a young boy. </s>

## 282. ತೊರೆ ನೀರು ಇದ್ದರೂ ಬಾವಿ ನೀರು ಹೆಚ್ಚು  (figurative)
*EN: Though there is stream water, well water is better*

- **Gold:** ಹೆಚ್ಚು ಕಾಣುವ ಆದರೆ ಅನಿಶ್ಚಿತ ಮೂಲಕ್ಕಿಂತ ಸುರಕ್ಷಿತ, ನಂಬಿಕೆಯ ಮೂಲವೇ ಉತ್ತಮ ಎಂಬ ಅರ್ಥವಿರಬಹುದು.
  - *EN: It may mean a safe, trusted source is better than an apparently abundant but uncertain one.*
- **mT0-large** ✗: ನೀರು ದಪ್ಪವಾಗಿದ್ದರೂ ಬಾವಿ ನೀರು ಹೆಚ್ಚು
  - *EN: Even if the water is thick, well water is more*
- **Qwen3.5-2B** ✓: The meaning of the proverb is that even if there is a hole in the water, the water level will be higher.
- **Sarvam-1** ✓: This means that if you have a lot of something, but it is not good quality or useful, then having less of it will be better than having more of it which is bad quality.

## 283. ತಾಯ ಹಳಿದರೂ ನೀರ ಹಳಿಯ ಬೇಡ  (figurative)
*EN: Even if you blame your mother, don't blame water*

- **Gold:** ಜೀವಾಧಾರವಾದ ನೀರನ್ನು ನಿರ್ಲಕ್ಷಿಸದೆ, ದೂಷಿಸದೆ ಗೌರವದಿಂದ ಕಾಣಬೇಕು.
  - *EN: Water, the basis of life, should be regarded with respect, not neglected or blamed.*
- **mT0-large** ✓: When the weather is cold, don't forget to wash the water.
- **Qwen3.5-2B** ✗: The meaning of the proverb is that a mother's love and care are so profound and enduring that they cannot be washed away or diluted by the passage of time.
- **Sarvam-1** ✓: This means that you should not give up when things are difficult, even if your mother is trying to make life harder for you.

## 284. ಕಸ ಆದರೂ ರುಚಿ ಮಾಡಿ ತಿನ್ನು  (figurative)
*EN: Even if it is trash, make it tasty and eat it*

- **Gold:** ಇರುವುದು ಸಾಮಾನ್ಯ ವಸ್ತುವಾದರೂ ಜಾಣತನದಿಂದ ಅದನ್ನೇ ಚೆನ್ನಾಗಿ ಬಳಸಿಕೊಂಡು ತೃಪ್ತಿ ಪಡಬೇಕು.
  - *EN: Even if what one has is ordinary, one should use it well with cleverness and be content.*
- **mT0-large** ✓: Tastes like a sauce
- **Qwen3.5-2B** ✓: ಕಸ ಆದರೂ ರುಚಿ ಮಾಡಿ ತಿನ್ನು
- **Sarvam-1** ✓: This means that even if something is bad or unpleasant, you can still enjoy it if you try to make it better.

## 285. ಆರು ಕಾಸಿನ ಸಂಬಳ ಆದರೂ, ಅರಮನೆಯ ಕೆಲಸ ಮಾಡು  (figurative)
*EN: Even if the salary is six kaasu, do palace work*

- **Gold:** ಸಂಬಳ ಕಡಿಮೆಯಾದರೂ ಗೌರವ ಮತ್ತು ಭದ್ರತೆ ಇರುವ ಉದ್ಯೋಗವೇ ಉತ್ತಮ.
  - *EN: A job with respect and security is better even if the salary is low.*
- **mT0-large** ✗: ಆರು ಕಾಸಿನ ಸಂಬಳ ಆದರೂ, ಅರಮನೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಆರು ಕಾಸಿನ ಸಂಬಳ (Six salary)
- **Sarvam-1** ✗: This means that if you are paid a lot for doing something, it is still not enough to do what you want or need to do. It's like having six cents and working at the palace - you can't get anything done!

## 286. ಮಾತು ಹೆಚ್ಚಿ ಮನೆ ಕೆಟ್ಟಿತು, ಬಿತ್ತು ಹೆಚ್ಚಿ ಹೊಲ ಕೆಟ್ಟಿತು  (figurative)
*EN: Talk increased and the house was ruined, seed increased and the field was ruined*

- **Gold:** ಅತಿಯಾದ ಮಾತು ಮನೆಯ ಶಾಂತಿ ಕೆಡಿಸುತ್ತದೆ, ಅತಿಯಾದ ಬೀಜ ಹೊಲ ಹಾಳು ಮಾಡುತ್ತದೆ; ಯಾವುದರಲ್ಲೂ ಅತಿ ಒಳ್ಳೆಯದಲ್ಲ.
  - *EN: Excessive talk spoils the peace of a house, excessive seed spoils a field; excess in anything is not good.*
- **mT0-large** ✓: ಮನೆಯ ಒಳಗಿನಿಂದ ಬಿತ್ತು ಹೊಲದ ಹೊಲ
  - *EN: From inside the house, sown field field (nonsensical)*
- **Qwen3.5-2B** ✓: Here is the explanation in one short sentence:
- **Sarvam-1** ✓: This means that if you talk too much about something or try to make it seem more important than it is, then your words will cause problems and damage instead of solving them. It's like planting a seed in the ground - if you plant a lot of seeds close together without giving them enough space

## 287. ಎತ್ತು ಇಲ್ಲದವಗೆ ಎದೆ ಇಲ್ಲ, ಮಕ್ಕಳು ಇಲ್ಲದವಗೆ ಮನೆ ಇಲ್ಲ  (figurative)
*EN: No chest without a bullock, no home without children*

- **Gold:** ಬೇಕಾದ ಆಧಾರ ಅಥವಾ ಬೆಂಬಲ ಇಲ್ಲದವರಿಗೆ ಧೈರ್ಯ ಹಾಗೂ ಮನೆಯ ಸುಖ ಇರುವುದಿಲ್ಲ ಎಂಬ ಅರ್ಥವಿರಬಹುದು.
  - *EN: It may mean that those without needed support have neither courage nor the comfort of a home.*
- **mT0-large** ✗: ಮಕ್ಕಳಿಲ್ಲದವಗೆ ಮನೆ ಇಲ್ಲ
  - *EN: No house for the childless*
- **Qwen3.5-2B** ✓: The proverb means that if you do not have a cow, you cannot have a cow, and if you do not have a child, you cannot have a child.
- **Sarvam-1** ✓: This means that without a leader or someone to guide you, you will not be able to achieve anything. You need an "elder" (leader) to help you get started and keep going. Without them, your dreams won't come true.

## 288. ಕೆಟ್ಟೆ ಅಂತ ಕೇಡ ತೂರ ಬೇಡ  (figurative)
*EN: Don't scatter ruin saying 'I am ruined'*

- **Gold:** ತನಗೆ ನಷ್ಟ ಅಥವಾ ಕೇಡಾಯಿತೆಂದು ಹತಾಶೆಯಿಂದ ಇತರರಿಗೆ ಕೆಡುಕು ಮಾಡಬಾರದು.
  - *EN: One shouldn't do harm to others out of despair, thinking oneself ruined or wronged.*
- **mT0-large** ✓: A few weeks ago, I was told that I was going to be a jerk.
- **Qwen3.5-2B** ✓: ಕೆಟ್ಟೆ ಅಂತ ಕೇಡ ತೂರ ಬೇಡ
- **Sarvam-1** ✓: ಈ proverb ಹೇಳೋದೇನೆಂದರೆ, ನೀವು ಬೇರೆಯವರ ಮೇಲೆ negative things ಹೇಳಬಾರದು.

## 289. ತಲೆ ತಟ್ಟಿ ನೆಲ ನೋಡಿ ನಡೆ  (literal)
*EN: Pat your head and walk looking at the ground*

- **Gold:** ವಿನಯದಿಂದ, ನೆಲ ನೋಡಿ ಎಚ್ಚರದಿಂದ ಹೆಜ್ಜೆ ಹಾಕಬೇಕು ಎಂಬ ನೇರ ಸಲಹೆ ಎನ್ನಬಹುದು.
  - *EN: It can be called direct advice: step carefully, humbly, looking at the ground.*
- **mT0-large** ✓: They look at the ground and look at the heaven.
- **Qwen3.5-2B** ✓: The proverb means "to look at the ground while walking, implying that one should not be distracted by excessive worry or anxiety."
- **Sarvam-1** ✓: This means that you should not be too proud or arrogant about your achievements, because there is always someone else who has done better than you. It's important to keep a humble attitude and focus on what you can do well rather than trying to compete with others. </s

## 290. ತಲೆಯವನ ಮಾತು, ಮುಂದುಕ್ ಉಪ್ಪು ಹಿಂದುಕ್ ಬೆಲ್ಲ  (figurative)
*EN: The head man's word: salt in front, jaggery behind*

- **Gold:** ಹಿರಿಯರ ಮಾತು ಆರಂಭದಲ್ಲಿ ಕಹಿ (ಉಪ್ಪು) ಎನಿಸಿದರೂ ಕೊನೆಗೆ ಸಿಹಿ (ಬೆಲ್ಲ) ಫಲ ಕೊಡುತ್ತದೆ ಎಂಬ ಅರ್ಥವಿರಬಹುದು.
  - *EN: Elders' words may seem bitter (salt) at first but finally bear sweet (jaggery) fruit.*
- **mT0-large** ✓: ನಿಮ್ಮ ತಲೆಯವನ ಮಾತು, ಹಿಂದುಕ್ ಉಪ್ಪು ಹಿಂದುಕ್ ಬೆಲ್ಲ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: The proverb means that a person's own words are often more persuasive and effective than the arguments or evidence presented by others.
- **Sarvam-1** ✓: This means that people who are more powerful or influential will often get their way because they have a lot of influence over others.

## 291. ಅಪ್ಪನ ಮಾತು, ಆನೆಯ ಬಲ  (literal)
*EN: Father's word, an elephant's strength*

- **Gold:** ತಂದೆಯ ಮಾರ್ಗದರ್ಶನ ಮತ್ತು ಬೆಂಬಲ ಆನೆಯಷ್ಟು ದೊಡ್ಡ ಶಕ್ತಿ ಕೊಡುತ್ತದೆ.
  - *EN: A father's guidance and support give as much strength as an elephant.*
- **mT0-large** ✓: A father's word, the arrow
- **Qwen3.5-2B** ✓: ಅಪ್ಪನ ಮಾತು, ಆನೆಯ ಬಲ
- **Sarvam-1** ✓: This means that your father's advice is very strong and can be difficult to ignore. It is like an elephant - it has a lot of strength and power. </s>

## 292. ಅಣ್ಣ ತಮ್ಮನ ಬೇರೆ ಮಾಡ ಬೇಡ  (literal)
*EN: Don't separate elder and younger brother*

- **Gold:** ಸಹೋದರರನ್ನು ಒಡೆದು ಬೇರೆ ಮಾಡದೆ ಒಗ್ಗಟ್ಟಿನಿಂದ ಇರಲು ಬಿಡಬೇಕು.
  - *EN: Brothers should not be split apart but allowed to stay united.*
- **mT0-large** ✓: A husband and wife should not be separated.
- **Qwen3.5-2B** ✓: ಅಣ್ಣ ತಮ್ಮನ ಬೇರೆ ಮಾಡ ಬೇಡ
- **Sarvam-1** ✓: This means that you should not try to do something for your brother or sister, because they will always be there to help you when you need it.

## 293. ಆರೋಗ್ಯವೇ ಭಾಗ್ಯ  (literal)
*EN: Health is wealth*

- **Gold:** ಒಳ್ಳೆಯ ಆರೋಗ್ಯವೇ ಮನುಷ್ಯನಿಗೆ ಅತಿ ದೊಡ್ಡ ಸಂಪತ್ತು.
  - *EN: Good health is the greatest wealth a person has.*
- **mT0-large** ✓: Health is a pleasure.
- **Qwen3.5-2B** ✓: ಆರೋಗ್ಯವೇ ಭಾಗ್ಯ (Arangya ve Bhagya) means that health is considered the greatest blessing or fortune.
- **Sarvam-1** ✓: This means that good health is a blessing and should be valued. It's not just about being physically fit, but also mentally healthy and happy. [/INST]

## 294. ನಿಧಾನವೇ ಪ್ರಧಾನ  (literal)
*EN: Slowness is the chief thing*

- **Gold:** ಯಾವುದೇ ಕೆಲಸವನ್ನು ಆತುರ ಪಡದೆ ನಿಧಾನವಾಗಿ ಮಾಡುವುದೇ ಮುಖ್ಯ ಮತ್ತು ಸುರಕ್ಷಿತ.
  - *EN: In any task, doing it slowly without haste is what matters and is safe.*
- **mT0-large** ✓: Slow is the most important.
- **Qwen3.5-2B** ✓: **"Slow is the key to success"** (or "Slowness is the key to success").
- **Sarvam-1** ✓: This means that slow and steady wins the race. It is a saying which means that if you are patient, work hard and do not give up easily then you will eventually succeed. If you try to rush things or act too quickly without thinking about what might happen, you may end up fail

## 295. ಕಲಿಕೆಗೆ ವಯಸ್ಸಿಲ್ಲ  (literal)
*EN: There is no age for learning*

- **Gold:** ಕಲಿಯಲು ಯಾವುದೇ ವಯಸ್ಸಿನ ಮಿತಿ ಇಲ್ಲ; ಯಾವ ವಯಸ್ಸಿನಲ್ಲೂ ಹೊಸದನ್ನು ಕಲಿಯಬಹುದು.
  - *EN: There is no age limit for learning; one can learn something new at any age.*
- **mT0-large** ✓: ವಯಸ್ಸಿಲ್ಲ.
  - *EN: No age.*
- **Qwen3.5-2B** ✓: ಕಲಿಕೆಗೆ ವಯಸ್ಸಿಲ್ಲ
- **Sarvam-1** ✓: This means that learning can happen at any age, and it's never too late to learn something new. </s>

## 296. ಒಗ್ಗಟ್ಟಿನಲ್ಲಿ ಬಲವಿದೆ  (literal)
*EN: There is strength in unity*

- **Gold:** ಎಲ್ಲರೂ ಒಟ್ಟಾಗಿ ಸೇರಿದರೆ ದೊಡ್ಡ ಶಕ್ತಿ ಸಿಗುತ್ತದೆ ಮತ್ತು ಕಷ್ಟದ ಕೆಲಸವೂ ಆಗುತ್ತದೆ.
  - *EN: When everyone joins together, great strength comes and even a hard task gets done.*
- **mT0-large** ✓: மக்கள் கூட்டத்தில் சக்தியுடையவர்கள்
  - *EN: [Tamil] Those who have power in the crowd of people*
- **Qwen3.5-2B** ✓: ಒಗ್ಗಟ್ಟಿನಲ್ಲಿ ಬಲವಿದೆ
- **Sarvam-1** ✓: This means that when people work together, they can accomplish more than if they were working alone. </s>

## 297. ಹೇಳುವುದು ಸುಲಭ ಮಾಡುವುದು ಕಷ್ಟ  (literal)
*EN: Saying is easy, doing is hard*

- **Gold:** ಒಂದು ಕೆಲಸವನ್ನು ಬಾಯಿಮಾತಿನಲ್ಲಿ ಹೇಳುವುದು ಸುಲಭ, ಆದರೆ ನಿಜವಾಗಿ ಮಾಡುವುದು ಕಷ್ಟ.
  - *EN: Saying a task is easy, but actually doing it is hard.*
- **mT0-large** ✗: says it's easy to say
- **Qwen3.5-2B** ✓: Here is the explanation:
- **Sarvam-1** ✓: This means that it is easy to say something, but hard to do it. [/INST]

## 298. ಹಲವು ಹನಿ ಕೂಡಿದರೆ ಹಳ್ಳ  (literal)
*EN: Many drops joined make a stream*

- **Gold:** ಚಿಕ್ಕ ಚಿಕ್ಕ ಹನಿಗಳು ಒಟ್ಟಾಗಿ ಸೇರಿದರೆ ಹಳ್ಳವೇ ಹರಿಯುತ್ತದೆ; ಚಿಕ್ಕದರಿಂದ ದೊಡ್ಡದಾಗುತ್ತದೆ.
  - *EN: Small drops, when joined together, make a stream flow; small things add up to something big.*
- **mT0-large** ✓: ಹಲವು ಹನಿ ಕೂಡಿದರೆ ಹಳ್ಳ
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಹಲವು ಹನಿ ಕೂಡಿದರೆ ಹಳ್ಳ
- **Sarvam-1** ✓: This means that if you have a lot of small things, they can add up to make something big and important. It's like when you put many drops of water into a cup - it becomes full! [/INST]

## 299. ಬೆಳೆಯುವ ಸಿರಿ ಮೊಳಕೆಯಲ್ಲಿ  (literal)
*EN: The prosperity of a growing plant is seen in the sprout*

- **Gold:** ಗಿಡ ಮುಂದೆ ಚೆನ್ನಾಗಿ ಬೆಳೆಯುವುದೋ ಇಲ್ಲವೋ ಎಂಬುದು ಮೊಳಕೆಯ ಹಂತದಲ್ಲೇ ಕಾಣುತ್ತದೆ.
  - *EN: Whether a plant will grow well later is seen at the sprout stage itself.*
- **mT0-large** ✓: సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని సన్నని
  - *EN: [Telugu] Thin thin thin thin... (repetitive)*
- **Qwen3.5-2B** ✓: ಬೆಳೆಯುವ ಸಿರಿ ಮೊಳಕೆಯಲ್ಲಿ
- **Sarvam-1** ✗: This means that you can't judge a book by its cover, or to put it another way, don't judge someone based on their appearance. [/INST]

## 300. ಉಪ್ಪಿಗಿಂತ ರುಚಿಯಿಲ್ಲ  (literal)
*EN: There is no taste greater than salt*

- **Gold:** ಅಡುಗೆಯ ರುಚಿಗೆ ಉಪ್ಪು ಅತ್ಯಗತ್ಯ; ಉಪ್ಪಿನಷ್ಟು ರುಚಿ ಕೊಡುವ ಬೇರೆ ವಸ್ತುವಿಲ್ಲ.
  - *EN: Salt is essential to the taste of cooking; nothing gives as much flavor as salt.*
- **mT0-large** ✓: ರುಚಿಯಿಲ್ಲ.
  - *EN: No taste.*
- **Qwen3.5-2B** ✗: ಉಪ್ಪಿಗಿಂತ ರುಚಿಯಿಲ್ಲ
- **Sarvam-1** ✗: This means that something is not worth much if it lacks value or importance. It's like saying "you can't eat salt without water" - you need both to make a meal! Similarly, this proverb suggests that some things are so insignificant they don't even

## 301. ಓತಿಕ್ಯಾತನಿಗೆ ಬೇಲಿ ಸಾಕ್ಷಿ  (literal)
*EN: The fence is witness for the garden lizard*

- **Gold:** ಯಾವುದೇ ವಿಷಯದಲ್ಲಿ ಅತಿ ಹೆಚ್ಚಾಗಿಯೂ ಇಲ್ಲದೆ, ತೀರಾ ಕಡಿಮೆ ಅಥವಾ ಕಳಪೆ ಆಗಿಯೂ ಇಲ್ಲದೆ ಮಿತವಾಗಿ, ಮಧ್ಯಮ ಸ್ಥಿತಿಯಲ್ಲಿ ಇರುವುದನ್ನು ಈ ಗಾದೆ ಸೂಚಿಸುತ್ತದೆ.
  - *EN: This proverb indicates being moderate and in a middle condition, neither excessive nor very low or poor in any matter.*
- **mT0-large** ✗: 'ఓತಿಕ್ಯಾತನಿಗೆ ಬೇಲಿ ಸಾಕ್ಷಿ'
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಓತಿಕ್ಯಾತನಿಗೆ ಬೇಲಿ ಸಾಕ್ಷಿ
- **Sarvam-1** ✓: This means that if you are too stubborn to change your ways, then no matter how much evidence is presented against you, it will not be enough to convince you otherwise. It's like trying to build a wall with bricks - even though you have many bricks,

## 302. ಅಂಗೈ ಹುಣ್ಣಿಗೆ ಕನ್ನಡಿ ಬೇಕೆ?  (figurative)
*EN: Does a sore on the palm need a mirror?*

- **Gold:** ಸ್ಪಷ್ಟವಾಗಿ ಕಾಣುವ ಸತ್ಯಕ್ಕೆ ಅಥವಾ ವಿಷಯಕ್ಕೆ ಯಾವುದೇ ಪ್ರಮಾಣ ಅಥವಾ ಸಾಕ್ಷಿಯ ಅಗತ್ಯವಿರುವುದಿಲ್ಲ ಎಂಬುದನ್ನು ಈ ಗಾದೆ ತಿಳಿಸುತ್ತದೆ.
  - *EN: This proverb says that a plainly visible truth or matter needs no proof or witness.*
- **mT0-large** ✓: ಪಾದವನ್ನು பிடித்துக் கொள்ளಲು ಪಾದವನ್ನು பிடித்துக் கொள்ள வேண்டும்.
  - *EN: [Kannada+Tamil mix] To hold the foot, one must hold the foot.*
- **Qwen3.5-2B** ✓: ಅಂಗೈ ಹುಣ್ಣಿಗೆ ಕನ್ನಡಿ ಬೇಕೆ?
- **Sarvam-1** ✓: This means that if you want to see something, you need to look at it directly. If you don't have a direct view, then you will not be able to understand what is happening or what needs to be done.

## 303. ಕೆಟ್ಟ ಮೇಲೆ ಬುದ್ಧಿ ಬಂತು  (literal)
*EN: Sense came after being ruined*

- **Gold:** ಯಾವುದಾದರೂ ತಪ್ಪು ಮಾಡಿ ಅಥವಾ ನಷ್ಟವನ್ನು ಅನುಭವಿಸಿದ ನಂತರ ಮನುಷ್ಯನಿಗೆ ಸರಿಯಾದ ತಿಳುವಳಿಕೆ ಅಥವಾ ಜ್ಞಾನ ಉಂಟಾಗುತ್ತದೆ ಎಂಬುದನ್ನು ಈ ಗಾದೆ ಸೂಚಿಸುತ್ತದೆ.
  - *EN: This proverb indicates that a person gains proper understanding or knowledge only after making a mistake or suffering a loss.*
- **mT0-large** ✓: 'ಕೆಟ್ಟ ಮೇಲೆ ಬುದ್ಧಿ ಬಂತು'
  - *EN: (repeats the proverb)*
- **Qwen3.5-2B** ✓: ಕೆಟ್ಟ ಮೇಲೆ ಬುದ್ಧಿ ಬಂತು
- **Sarvam-1** ✓: This means that when you are faced with a difficult situation, it is better to think about what you can do than just give up and accept defeat.

## 304. ಎರಡು ಕೈ ಸೇರಿದರೆ ಚಪ್ಪಾಳೆ  (figurative)
*EN: Two hands joined make a clap*

- **Gold:** ಯಾವುದೇ ದೊಡ್ಡ ಕೆಲಸ ಅಥವಾ ಜಗಳ/ಒಪ್ಪಂದ ಯಶಸ್ವಿಯಾಗಲು ಅಥವಾ ಪರಿಹಾರವಾಗಲು ಇಬ್ಬರ ಪರಸ್ಪರ ಸಹಕಾರ ಅಥವಾ ಒಮ್ಮತ ಅತ್ಯಗತ್ಯ ಎಂಬುದನ್ನು ಈ ಗಾದೆ ಸೂಚಿಸುತ್ತದೆ.
  - *EN: This proverb indicates that for any big task, quarrel or agreement to succeed or be resolved, mutual cooperation or consensus of two parties is essential.*
- **mT0-large** ✓: Two hands together make a noise.
- **Qwen3.5-2B** ✓: ಎರಡು ಕೈ ಸೇರಿದರೆ ಚಪ್ಪಾಳೆ
- **Sarvam-1** ✓: Two people working together can accomplish more than either could do alone. [/INST]

## 305. ಆಟಕ್ಕುಂಟು ಲೆಕ್ಕಕ್ಕಿಲ್ಲ  (figurative)
*EN: Counts for the game, not for the reckoning*

- **Gold:** ಯಾವುದಾದರೂ ವಸ್ತು ಅಥವಾ ವ್ಯಕ್ತಿ ಕೇವಲ ಹೆಸರಿಗೆ ಅಥವಾ ಔಪಚಾರಿಕವಾಗಿ ಮಾತ್ರ ಇದ್ದು, ನಿಜವಾದ ಜವಾಬ್ದಾರಿಯಲ್ಲಿ ಅಥವಾ ಲೆಕ್ಕಾಚಾರದಲ್ಲಿ ಪರಿಗಣಿಸಲ್ಪಡದೆ ಇರುವುದನ್ನು ಈ ಗಾದೆ ಸೂಚಿಸುತ್ತದೆ.
  - *EN: This proverb indicates a thing or person that exists only nominally or formally and is not counted in real responsibility or calculation.*
- **mT0-large** ✗: ಆಟ కోసం ಲೆಕ್ಕಿಲ್ಲ
  - *EN: [Kannada+Telugu mix] No accounting for the game*
- **Qwen3.5-2B** ✓: ಆಟಕ್ಕುಂಟು ಲೆಕ್ಕಕ್ಕಿಲ್ಲ means "There is no calculation for the game."
- **Sarvam-1** ✓: This means that you should not worry about small things, because they are insignificant and can be ignored.

# Part 2: English prompts (reviewed translation)

## 1. Where there's a will, there's a way  (figurative)

- **Gold:** If one has strong willpower, a way opens up even for a difficult task.
- **mT0-large** ✓: Where there's a will, there's a way
- **Qwen3.5-2B** ✓: Where there's a will, there's a way
- **Sarvam-1** ✓: This means that if you have a strong desire or determination to do something, then you can find a way to make it happen. It doesn't matter how difficult or impossible it may seem at first - with enough effort and perseverance, anything is possible! </s>

## 2. If the hand gets muddy, the mouth gets curd  (figurative)

- **Gold:** Only by working hard does one get a good life or a reward.
- **mT0-large** ✓: If the hand gets muddy, the mouth gets curd
- **Qwen3.5-2B** ✓: The hand gets muddy, the mouth gets curd
- **Sarvam-1** ✓: This means that if you get involved with something bad or wrong, it will affect your reputation and character. It is like getting dirty hands can make your clothes stained; similarly, doing something wrong can tarnish your good name.

## 3. Speech is silver, silence is gold  (figurative)

- **Gold:** Staying silent as the situation demands is more valuable and wiser than speaking unnecessarily.
- **mT0-large** ✓: Speech is silver, silence is gold
- **Qwen3.5-2B** ✓: The proverb means that while words can be valuable and persuasive, true wisdom and value are found in the power of silence.
- **Sarvam-1** ✓: This means that words are not as valuable as actions and quietness is more important than talking too much.

## 4. Not everything white is milk, not everything that shines is gold  (figurative)

- **Gold:** Not everything that looks attractive or pure on the outside is truly good or valuable.
- **mT0-large** ✗: Nothing white is milk, nothing that shines is gold
- **Qwen3.5-2B** ✓: Not everything white is milk, not everything that shines is gold.
- **Sarvam-1** ✓: This means that you can't always judge something by its appearance or surface. Sometimes things are different than they seem at first glance.

## 5. What doesn't bend as a sapling, will it bend as a tree?  (figurative)

- **Gold:** Any matter or bad habit should be corrected early, at a young age; once one is older or time has passed, correcting it is impossible.
- **mT0-large** ✓: What doesn't bend as a sapling, will it bend as a tree?
- **Qwen3.5-2B** ✓: What doesn't bend as a sapling, will it bend as a tree?
- **Sarvam-1** ✓: This means that if something is not flexible or strong enough to withstand pressure, then it won't be able to handle it when put under stress. It's like saying "if you don't have strength and flexibility, you can't stand up". [/INST]

## 6. One who can be a servant can become a king  (figurative)

- **Gold:** In any system or job, only one who understands the hardships and losses at the lower level and has served honestly becomes worthy of being a good leader or officer in the future.
- **mT0-large** ✓: A servant can become a king.
- **Qwen3.5-2B** ✓: One who can be a servant can become a king
- **Sarvam-1** ✓: This means that anyone can achieve great things if they are willing to work hard and put their mind to it. It's not about being born into wealth or power, but about having the drive and determination to succeed.

## 7. One who endures will thrive  (literal)

- **Gold:** Only those who maintain patience and restraint in difficult situations or hard times find success and peace in life.
- **mT0-large** ✓: One who endures will thrive
- **Qwen3.5-2B** ✓: One who endures will thrive
- **Sarvam-1** ✓: This means that if you are able to withstand hardship and difficulties, then you will be successful in life. It is a way of saying that perseverance pays off.

## 8. Like giving a ruby to a monkey's hand  (figurative)

- **Gold:** When a highly valuable object, authority or responsibility is given to a person without worthiness or qualification, they waste it without knowing its true value or use.
- **mT0-large** ✓: Like giving a ruby to a monkey's hand
- **Qwen3.5-2B** ✓: Like giving a ruby to a monkey's hand
- **Sarvam-1** ✓: This means that you can give something valuable or important, but it won't be appreciated by someone who doesn't understand its value. It is like giving a ruby to a monkey's hand - it will not benefit them at all.

## 9. Even if the Veda proves false, the proverb will not  (literal)

- **Gold:** Proverbs born from long human experience and truth never become false in any age; they are always true.
- **mT0-large** ✓: Even if the Veda proves false, the proverb will not
- **Qwen3.5-2B** ✓: The Veda is a sacred text in Hinduism.
- **Sarvam-1** ✓: The proverb is saying that even if something you believe to be true turns out to be wrong, it doesn't mean your belief was incorrect from the start. It just means that there might have been a mistake or misunderstanding somewhere along the way. This idea can help us keep an open

## 10. Stretch your legs only as far as the bed allows  (figurative)

- **Gold:** One should spend, or hold desires, only in line with one's income, wealth or capacity.
- **mT0-large** ✓: Stretch your legs only as far as the bed allows
- **Qwen3.5-2B** ✓: Stretch your legs only as far as the bed allows
- **Sarvam-1** ✓: This means that you should not go beyond what is reasonable or possible, especially when it comes to taking risks or trying new things. It's important to be realistic and think about the consequences before making a decision.

## 11. Eat what you have made, O lord (you reap what you sow)  (literal)

- **Gold:** A person has to experience for himself the good or bad result of the work, deeds or effort he has done.
- **mT0-large** ✓: Eat what you have made, Lord (you reap what you sow)
- **Qwen3.5-2B** ✓: The proverb means that one's own labor and efforts are the only source of sustenance and success, as the rewards one receives are directly proportional to the work one puts in.
- **Sarvam-1** ✓: This means that if you work hard and make something good or bad, then it will be rewarded to you. If you do not work hard, then you will not get anything from your efforts. It is a way of saying that people should take responsibility for their actions. They should not bl

## 12. Excessive desire leads to a bad end  (literal)

- **Gold:** Excessive desire or greed is never good; it leads a person to destruction.
- **mT0-large** ✗: Excessive desire leads to a bad end
- **Qwen3.5-2B** ✓: Here is the explanation:
- **Sarvam-1** ✓: This means that if you want something too much, it can lead to problems or harm. It's like trying to eat an entire pizza by yourself - you might not be able to finish it and feel sick! The same idea applies here; having too many things at once can cause stress

## 13. A dog's tail is crooked  (figurative)

- **Gold:** The basic nature or bad habits of some people never change no matter how much one tries.
- **mT0-large** ✓: A dog's tail is crooked.
- **Qwen3.5-2B** ✓: A dog's tail is crooked
- **Sarvam-1** ✓: This means that something or someone has a bad habit, and it will be difficult to change their behavior. The phrase comes from an old saying about dogs, which was used as a metaphor for people who have habits they can’t break. It suggests that if you try hard enough to fix your

## 14. Butter for one eye, lime for the other eye  (figurative)

- **Gold:** It is not right for any person or organization to show partiality or discrimination among people.
- **mT0-large** ✗: Butter for one eye, lime for the other eye
- **Qwen3.5-2B** ✓: Butter for one eye, lime for the other eye
- **Sarvam-1** ✗: This means that you should not be too quick to judge something or someone because there is always a chance that your opinion may change later on. It's like having two eyes - if you only have one eye and try to see everything with it, you might miss out on some important details. Similarly

## 15. Inborn nature doesn't go even if burned  (figurative)

- **Gold:** Qualities or habits that come from birth do not change until the end of a person's life.
- **mT0-large** ✓: Inborn nature doesn't go even if burned
- **Qwen3.5-2B** ✓: Inborn nature doesn't go even if burned
- **Sarvam-1** ✓: This means that you can't change your natural characteristics, no matter how much you try to change them. It is a very strong statement and it is not easy to accept. The phrase comes from an old English saying which was used by Shakespeare. He said "In born nature don't

## 16. At the time of destruction, a perverse mind  (figurative)

- **Gold:** When hard times or a bad situation arrive, a person's mind doesn't work and he makes wrong decisions.
- **mT0-large** ✗: A perverse mind is a devil
- **Qwen3.5-2B** ✓: The time of destruction is a time of great danger and uncertainty.
- **Sarvam-1** ✓: This means that when something is going to be destroyed or ruined, someone who has a bad attitude will make it worse. It's like saying "when you are about to lose everything, don't get angry."

## 17. Travel the country and see, read the books and see  (literal)

- **Gold:** By travelling the world to gain experience and by reading good books, a person gains complete knowledge.
- **mT0-large** ✓: Travel the country and see, read the books and see
- **Qwen3.5-2B** ✓: Travel the country and see, read the books and see
- **Sarvam-1** ✓: This means that if you want to learn about something or someone, it is best to go out into the world and experience it yourself rather than just reading about it from a book. It's like saying "experience is the best teacher".

## 18. Like inviting into your house the calamity (Mari) passing by on the street  (figurative)

- **Gold:** Deliberately bringing upon oneself a trouble or danger that has nothing to do with one.
- **mT0-large** ✗: A stranger passing by on the street is like inviting into your house.
- **Qwen3.5-2B** ✓: The calamity (Mari) passing by on the street is a metaphor for a sudden, unexpected event.
- **Sarvam-1** ✓: This means that you should not let bad luck or misfortune come to you, because it will pass eventually and nothing can stop it from happening. It is better to be prepared for what might happen than to have a surprise when something unexpected happens.

## 19. After eating salt, one must drink water  (literal)

- **Gold:** One who has done a wrong or improper act must face its consequences.
- **mT0-large** ✓: After eating salt, one must drink water
- **Qwen3.5-2B** ✓: After eating salt, one must drink water
- **Sarvam-1** ✓: This means that if you eat something salty, then you should also drink some water to balance out the effect. Otherwise, it can cause dehydration or other health problems. </s>

## 20. Yellamma's fair on someone else's money  (figurative)

- **Gold:** Spending lavishly and making merry with others' money without any accounting.
- **mT0-large** ✗: Yellamma's fair on someone else's money
- **Qwen3.5-2B** ✓: Yellamma's fair on someone else's money
- **Sarvam-1** ✓: This means that you shouldn't spend your own money, but instead save it for yourself or use it to help others. It is a reminder not to be greedy and wasteful with our resources. [/INST]

## 21. Everything that happens is for the good  (literal)

- **Gold:** This proverb expresses the assurance that whatever happens in life ultimately turns out for the good.
- **mT0-large** ✓: All that happens is for the good
- **Qwen3.5-2B** ✓: Everything that happens is for the good.
- **Sarvam-1** ✓: This means that everything that happens to you, no matter how bad it may seem at first, will eventually turn out for your benefit. It's a reminder that even when things are tough, there's always something positive lurking around the corner.

## 22. Walk according to the times, dance according to the beat  (literal)

- **Gold:** One should adapt oneself to changing times and circumstances.
- **mT0-large** ✓: Walk according to the times, dance according to the beat
- **Qwen3.5-2B** ✓: The meaning of the proverb is that you should adapt your actions to the current situation and follow the rhythm of the moment.
- **Sarvam-1** ✓: This means that you should follow what is happening around you and not stick to old ways or ideas. You need to adapt to new situations and changes.

## 23. Don't burgle the house that fed you  (figurative)

- **Gold:** A warning that one shouldn't greedily eye the house or property one's elder brother built with hardship.
- **mT0-large** ✓: Don't burgle the house that fed you
- **Qwen3.5-2B** ✓: The house that fed you is the one that provided you with food and shelter.
- **Sarvam-1** ✓: This means don't steal from someone who has helped you or provided for you, because they may be able to help you if you need it later on. It is a reminder not to take advantage of people who have done something good for us.

## 24. Mari's eye is on the bull, the butcher's eye is on the sheep  (figurative)

- **Gold:** Every greedy person keeps his eye on whatever benefits him.
- **mT0-large** ✓: The butcher's eye is on the sheep.
- **Qwen3.5-2B** ✓: Mari's eye is on the bull, the butcher's eye is on the sheep
- **Sarvam-1** ✓: This means that you should pay attention to what others are doing and not worry about your own business. It is a warning against being too concerned with other people's affairs while neglecting your own responsibilities. The phrase comes from an old English saying which has been used for centuries. It was

## 25. What comes to one's lot is paramanna (sweet rice pudding)  (figurative)

- **Gold:** Whatever comes to one's share, one should accept it happily (what comes to one's lot is paramanna).
- **mT0-large** ✓: The sweet rice pudding is a delicious treat.
- **Qwen3.5-2B** ✓: What comes to one's lot is paramanna (sweet rice pudding)
- **Sarvam-1** ✓: This means that what happens to you, whether good or bad, is a matter of luck and not your fault. It is like saying "lucky dip".

## 26. Tell a thousand lies and perform one wedding  (figurative)

- **Gold:** A saying that a little exaggeration or even a lie is no sin if it brings about a wedding, which is a good-intentioned act.
- **mT0-large** ✓: Tell a thousand lies and perform one wedding
- **Qwen3.5-2B** ✓: The meaning of the proverb is that it is better to tell a thousand lies and perform one wedding.
- **Sarvam-1** ✓: This means that if you tell many lies, it is possible to get away with them. However, telling only one lie can be difficult because people will notice when something doesn't add up. It also implies that sometimes we need to make tough decisions about what information to share or keep private.

## 27. Even if you trust a thief, don't trust a short man  (figurative)

- **Gold:** A warning not to trust a shrewd and scheming person; it is also an old, conventional prejudice against short people.
- **mT0-large** ✗: Even if you trust a thief, don't trust a short man
- **Qwen3.5-2B** ✓: The meaning of the proverb is that you should not trust a thief because he is a thief.
- **Sarvam-1** ✓: This is an example of a proverb that means even if someone has good intentions or seems like they are trustworthy, it doesn't mean that they will always be honest and reliable. It can also refer to physical characteristics such as height, which may not necessarily reflect someone's

## 28. Though he fell to the ground, his moustache didn't get dirty  (figurative)

- **Gold:** Not admitting one's defeat and showing off even after losing or being humiliated.
- **mT0-large** ✗: He fell to the ground, his moustache didn't get dirty.
- **Qwen3.5-2B** ✓: The moustache didn't get dirty because he was wearing a mask.
- **Sarvam-1** ✗: This means that even if you make a mistake or fail at something, it doesn't mean your whole life is ruined. You can always learn from your mistakes and move on.

## 29. Which snake is in which anthill  (figurative)

- **Gold:** One cannot know a person's inner nature or hidden danger from outward appearance; one can't say what is hidden in whom.
- **mT0-large** ✓: The snake is in the anthill.
- **Qwen3.5-2B** ✓: The snake is in the anthill.
- **Sarvam-1** ✓: This means that you can't tell what someone else is thinking or doing just by looking at them, because they might be hiding something. It's like trying to figure out where a snake is based on its behavior - it could be anywhere!

## 30. Even if the god is pleased, the priest isn't  (figurative)

- **Gold:** Even if the higher authority or the god himself agrees, the intermediary or subordinate in between creates obstacles.
- **mT0-large** ✓: The priest is not pleased with God.
- **Qwen3.5-2B** ✓: The priest is not the one who is responsible for the god's satisfaction.
- **Sarvam-1** ✓: This means that even when you do something good or right, there are still consequences to your actions. The priest may be happy with what you did, but it could have negative effects on someone else. It's important to consider all aspects of an action before taking it. [/INST]

## 31. We know the truth of our own god  (figurative)

- **Gold:** The meaning may be that people know the inner truth of their own house or matter well enough themselves and have no need of outsiders' talk.
- **mT0-large** ✓: We know the truth of our own god
- **Qwen3.5-2B** ✓: We know the truth of our own god
- **Sarvam-1** ✓: This means that we can only truly understand ourselves and what is right for us, because we are all unique individuals with different experiences and perspectives. It's important to listen to our inner voice and trust our instincts rather than trying to force things on others or impose our beliefs on them

## 32. For the bitter gourd, the neem fruit is the witness  (figurative)

- **Gold:** The wording is unclear; it may mean that one dubious matter is backed by an equally dubious witness.
- **mT0-large** ✗: For the bitter gourd, the neem fruit is the witness
- **Qwen3.5-2B** ✗: The bitter gourd is a plant that grows in the same area as the neem tree.
- **Sarvam-1** ✓: The proverb means that when you are trying to do something difficult or dangerous, it's better to have someone else there who can help and support you. It's like having a "witness" - someone who will see what happens and tell others about it if needed. This idea comes

## 33. The morsel that came to the hand didn't reach the mouth  (figurative)

- **Gold:** An opportunity or gain slips away at the last moment, just as it was about to be obtained.
- **mT0-large** ✗: The morsel that came to the hand didn't reach the mouth
- **Qwen3.5-2B** ✓: The morsel that came to the hand didn't reach the mouth
- **Sarvam-1** ✗: This means that if you don't have enough, you can't get what you want. It is a saying about not being able to get something when you need it most.

## 34. What the patient wanted was milk-rice; what the doctor prescribed was milk-rice  (figurative)

- **Gold:** The unexpected, happy coincidence when what one wanted is exactly what others say as advice or orders.
- **mT0-large** ✗: The patient wanted milk-rice; the doctor prescribed milk-rice
- **Qwen3.5-2B** ✗: The patient wanted milk-rice, but the doctor prescribed milk-rice.
- **Sarvam-1** ✗: This is a common Chinese saying that means "the medicine for the sick is not always the same as the disease". In other words, sometimes you have to give your patients something different from what they want or need. The phrase comes from an old story about a man who had been ill and died because

## 35. A thief always has a petty excuse  (figurative)

- **Gold:** One who has done wrong always finds some small excuse to escape.
- **mT0-large** ✗: A thief always has a petty excuse.
- **Qwen3.5-2B** ✓: A thief always has a petty excuse
- **Sarvam-1** ✓: This means that if you are doing something wrong, there is usually an easy way to justify it. It's like saying "If I can find a reason for what I did, then maybe I shouldn't be punished." [/INST]

## 36. The woman who couldn't dance said the floor is crooked  (figurative)

- **Gold:** Blaming equipment or circumstances instead of accepting one's own incompetence or shortcoming.
- **mT0-large** ✗: The woman who couldn't dance said the floor is crooked
- **Qwen3.5-2B** ✓: The woman who couldn't dance said the floor is crooked
- **Sarvam-1** ✓: This means that if you can't do something well, it doesn't matter how hard you try because there are always going to be people better than you at what you do. It's not about being able to do something perfectly but rather trying your best and accepting when things don'

## 37. Putta went, Putta came back.  (figurative)

- **Gold:** Returning in vain, empty-handed just as one went, without any gain.
- **mT0-large** ✗: Putta went, Putta came back.
- **Qwen3.5-2B** ✓: Putta went, Putta came back.
- **Sarvam-1** ✓: This is a common English saying that means "You can't have your cake and eat it too". It refers to the idea that you cannot do two things at once or you will not be able to complete both tasks successfully. The phrase comes from an old story about a man who wanted

## 38. Like letting a bear loose during Shiva worship  (figurative)

- **Gold:** A saying about people who cause absurd disruption in the middle of a sacred or orderly event.
- **mT0-large** ✓: A bear is loose during Shiva worship.
- **Qwen3.5-2B** ✓: Like letting a bear loose during Shiva worship
- **Sarvam-1** ✓: This means that you should not be too hasty to do something, especially if it is dangerous or harmful. It's better to think things through first before acting on them. </s>

## 39. Say 'pumpkin thief' and he felt his own shoulder  (figurative)

- **Gold:** A guilty person takes others' ordinary words as being about himself and gives away his own crime.
- **mT0-large** ✗: The pumpkin thief felt his own shoulder.
- **Qwen3.5-2B** ✓: The meaning of the proverb is that when you are in a situation where you are being criticized or judged, you should not be defensive. Instead, you should be open and honest about your mistakes.
- **Sarvam-1** ✓: This is a very old saying that means to say something bad about someone else, so they feel like it was said about them personally. It can also be used when you are trying to get someone to do something by making fun of them or telling them how stupid they are. The phrase comes

## 40. 'Malli, Malli, how many legs does the cot have?' 'Three and one more,' she said  (figurative)

- **Gold:** Giving a roundabout, needlessly twisted answer to a simple question, or saying something obvious in another way.
- **mT0-large** ✓: The cot has three legs.
- **Qwen3.5-2B** ✓: 'Malli, Malli, how many legs does the cot have?' 'Three and one more,' she said
- **Sarvam-1** ✓: The proverb is a play on words because it uses two different meanings for the word "legs". It's saying that there are three legs to the chair (the number of legs needed to support the weight of the person sitting on it), but also adding another leg to make four total

## 41. A thief's mind is jittery  (figurative)

- **Gold:** This proverb says a wrongdoer's mind is always full of fear and suspicion and startles at the slightest sound.
- **mT0-large** ✓: A thief's mind is anxious.
- **Qwen3.5-2B** ✓: A thief's mind is jittery
- **Sarvam-1** ✓: This means that a person who steals will be nervous and worried about getting caught, so they are always on edge and ready to do something wrong.

## 42. If the swinging club misses, a hundred years of life  (figurative)

- **Gold:** If a great danger that was about to strike narrowly misses, it is like getting a new life; a consoling word that one will live long.
- **mT0-large** ✓: If the swinging club misses, a hundred years of life
- **Qwen3.5-2B** ✓: The swinging club is a metaphor for a person's life. The swinging club is a metaphor for a person's life.
- **Sarvam-1** ✗: This means that if you don't do something right away and take action when it is needed, then there will be consequences later on. It can also mean that taking time to think about things before acting can help prevent problems down the road.

## 43. If a woman is won over she is a woman, if angered she is a fearsome goddess.  (figurative)

- **Gold:** A woman who is won over with love is an affectionate woman; if angered she takes a terrifying form.
- **mT0-large** ✗: A woman is a woman, if angered she is a fearsome goddess.
- **Qwen3.5-2B** ✓: If a woman is won over she is a woman, if angered she is a fearsome goddess.
- **Sarvam-1** ✓: This means that once you have won someone's heart they are forever yours and no matter what happens to them or how angry they get, they will always be with you. It also implies that women can be very powerful and fierce when they feel threatened or disrespected. </s>

## 44. When the ox pulled uphill, the buffalo pulled into the water  (figurative)

- **Gold:** When two people work together, one pulls in one direction and the other in the opposite direction, spoiling the work.
- **mT0-large** ✓: When the ox pulled uphill, the buffalo pulled into the water
- **Qwen3.5-2B** ✓: The buffalo is a symbol of the people of the land.
- **Sarvam-1** ✗: This is a common English saying that means "It's easier to do something difficult than easy". The phrase comes from an old story about two animals who were trying to pull each other up a hill. One was an ox and the other was a buffalo. The ox worked very hard but couldn

## 45. Though the one who gives kisses has come, don't forget the one who gave you morsels  (figurative)

- **Gold:** When a new attraction or relationship comes along, one should not forget those who fed and raised one in hard times or did one favors.
- **mT0-large** ✓: The one who gave you kisses has come, don't forget the one who gave you morsels.
- **Qwen3.5-2B** ✓: The one who gives kisses has come, don't forget the one who gave you morsels
- **Sarvam-1** ✓: The proverb is saying that even if someone comes to give us something nice like a kiss or a gift, we should not forget about the person who taught us how to do it in the first place. This means that we need to be grateful for what others have done for us and

## 46. The god of Sindhaghatta wavers back and forth  (figurative)

- **Gold:** A proverb in a local dialect whose words are unclear; guessed to mean wavering, uncertain behavior and not standing by one's word (uncertain).
- **mT0-large** ✓: The god of Sindhaghatta wavers back and forth
- **Qwen3.5-2B** ✓: The god of Sindhaghatta wavers back and forth
- **Sarvam-1** ✓: This means that things are not always as they seem to be, or may change quickly. It is a reference to the mythical figure of Sindhaghatta who was said to have been able to move mountains with his power. However, this proverb suggests that even powerful figures can

## 47. What relation is there between Gokulashtami and Imam Saab?  (figurative)

- **Gold:** Bringing an unrelated matter into an unrelated place; that is, an irrelevant remark.
- **mT0-large** ✗: Imam Saab is a religious leader
- **Qwen3.5-2B** ✓: The proverb is a metaphor for the relationship between the two.
- **Sarvam-1** ✓: The answer to this question would be that they are both related, but not directly. They are connected through a common theme or idea, which is the celebration of life and its cycles. However, their relationship is more like a chain than a direct link. Just as how we celebrate Gokul

## 48. One who lives as a servant today will be a king tomorrow  (literal)

- **Gold:** One who works humbly like a servant today will one day rise to a higher position.
- **mT0-large** ✓: A servant who lives as a servant today will be a king tomorrow.
- **Qwen3.5-2B** ✓: One who lives as a servant today will be a king tomorrow.
- **Sarvam-1** ✓: This means that if you work hard and do your best, you can achieve great things in life. It's like saying "the early bird catches the worm". If you start working now, you have a better chance of success later on.

## 49. Everyone's house has holes in the dosa  (figurative)

- **Gold:** Every house has some problem or shortcoming; nobody's house is perfect.
- **mT0-large** ✓: Everyone's house has holes in the dosa
- **Qwen3.5-2B** ✓: Everyone's house has holes in the dosa
- **Sarvam-1** ✓: This means that everyone is vulnerable to problems and difficulties, no matter how strong or successful they may seem. The proverb uses a metaphorical comparison between houses (or homes) and people, suggesting that just as a home can have weak points, so too can individuals. It emphasizes the

## 50. Not a son-in-law, just the daughter's husband  (figurative)

- **Gold:** A remark that the son-in-law is not like one's own son but has come only through the relationship of being the daughter's husban.
- **mT0-large** ✗: A son-in-law is not a son-in-law, just the daughter's husband.
- **Qwen3.5-2B** ✓: The daughter's husband is the son-in-law of the daughter's mother.
- **Sarvam-1** ✓: This means that someone who is not related to you by blood but married into your family is still considered part of your family. It emphasizes the importance of familial bonds and relationships over other factors such as blood ties or legal status. </s>

## 51. If played with, a parrot; if provoked, a cobra  (figurative)

- **Gold:** A saying about those who are like a sweet parrot when treated lovingly and like a tormenting cobra when provoked .
- **mT0-large** ✓: A parrot is a parrot, a cobra is a cobra.
- **Qwen3.5-2B** ✓: The parrot is a bird that is known for its ability to mimic sounds and words. The cobra is a snake that is known for its ability to strike and bite.
- **Sarvam-1** ✓: This is an English saying that means that you should not play around with someone who will get angry or upset easily. It's like playing with fire - it can be dangerous and may cause harm to others. The phrase comes from the idea that just as a cobra (a poisonous

## 52. Don't trust a weeping man or a laughing woman  (figurative)

- **Gold:** The emotion of a man who weeps excessively or a woman who laughs excessively may be put on, so one should not blindly trust such people's words.
- **mT0-large** ✓: Don't trust a weeping man or a laughing woman
- **Qwen3.5-2B** ✓: Don't trust a weeping man or a laughing woman because their emotions are unreliable indicators of their true intentions.
- **Sarvam-1** ✓: This is an example of a proverb, which means that you should not believe everything people say because they might be lying to you. It can also mean that if someone looks sad or happy all the time, it could be a sign that something bad is going on.

## 53. Saying 'oh, poor thing' is half a lifespan  (figurative)

- **Gold:** Even one word of sympathy gives great courage and comfort to those in trouble.
- **mT0-large** ✗: Saying 'oh, poor thing' is half a lifespan
- **Qwen3.5-2B** ✗: Saying 'oh, poor thing' is half a lifespan
- **Sarvam-1** ✗: This means that if you say something like "Oh, poor thing" to someone who has just suffered some misfortune or loss, it will only be half as long as they have been suffering before. It implies that people tend to forget about their problems after a while and move on with life

## 54. If the performer performs, the onlooker feels shame  (figurative)

- **Gold:** The one who does wrong has no shame, but those who watch it feel embarrassed.
- **mT0-large** ✓: The performer performs, the onlooker feels shame
- **Qwen3.5-2B** ✓: If the performer performs, the onlooker feels shame
- **Sarvam-1** ✓: This means that if someone is performing something and they are not doing it well or correctly, then other people will feel embarrassed about them. It's like when you see someone trying to do something really badly, even though they know how to do it properly, and everyone else around

## 55. Like a frog jumping on one who is already frightened  (figurative)

- **Gold:** Another small trouble comes to one already in fear or hardship and unnerves him further.
- **mT0-large** ✓: A frog jumps on a man who is already frightened.
- **Qwen3.5-2B** ✓: The frog jumps on the person who is already frightened.
- **Sarvam-1** ✓: This means that if you are afraid, then others will be even more afraid of you. It's like when someone jumps onto another person who is already scared and they become even more scared.

## 56. If you see a bad dream, get up and sit  (figurative)

- **Gold:** It may mean that on seeing a bad omen or sign of danger, one should wake up and be alert rather than lie down and ignore it.
- **mT0-large** ✓: If you see a bad dream, get up and sit
- **Qwen3.5-2B** ✓: If you see a bad dream, get up and sit
- **Sarvam-1** ✓: This means that if you are having a bad dream or nightmare, it is best to wake up and try to solve your problems instead of staying asleep and letting them continue. It's better to face your fears head-on than to keep running away from them.

## 57. Like placing a lamp on the dividing wall  (figurative)

- **Gold:** It may mean an arrangement that is equally useful to both sides, or one that favors neither side.
- **mT0-large** ✓: A lamp is placed on the dividing wall.
- **Qwen3.5-2B** ✓: Like placing a lamp on the dividing wall
- **Sarvam-1** ✗: This means that you should not put your efforts into something which is already divided or separated, because it will be useless and waste of time. It's like putting a lamp on a wall where there are no walls to separate them.

## 58. If you give six, he's on the mother-in-law's side; if you give three, on the daughter-in-law's side  (figurative)

- **Gold:** One who sides with whoever gives more looks for profit, not justice.
- **mT0-large** ✗: If you give six, he's on the mother-in-law's side; if you give three, he's on the daughter-in-law's side
- **Qwen3.5-2B** ✗: If you give six, he's on the mother-in-law's side; if you give three, on the daughter-in-law's side
- **Sarvam-1** ✗: This is a saying that means that it doesn't matter how much money or resources you have, but what really matters is who your family members are and their relationship to you. The phrase comes from an old English tradition where people would be given gifts based on certain numbers. For example,

## 59. Honor lost over a betel nut won't return even if an elephant is given  (figurative)

- **Gold:** Once one loses honor over a small matter, it cannot be regained however high a price is paid.
- **mT0-large** ✓: Honor lost over a betel nut won't return even if an elephant is given
- **Qwen3.5-2B** ✓: The proverb illustrates that a small, insignificant gain cannot be compared to the value of a significant loss, as the loss of honor is irreversible regardless of any subsequent compensation.
- **Sarvam-1** ✓: This means that once you lose something, it can never be regained. It is like losing your honor or reputation; no matter how much money you give to someone who has cheated you, they will not change their behavior and continue to do wrong things. The same goes for any other loss -

## 60. The grandmother worries about cloth, the daughter worries about marriage  (literal)

- **Gold:** Each person has different worries according to their age and situation.
- **mT0-large** ✗: The grandmother worries about cloth, the daughter worries about marriage
- **Qwen3.5-2B** ✓: The grandmother worries about cloth, the daughter worries about marriage
- **Sarvam-1** ✓: This means that a mother or grandmother will worry more about things like clothing and household chores than her children's future marriages.

## 61. Desire for the rice, love for the relatives  (literal)

- **Gold:** It may mean that the real desire of those who claim love for relatives is for the food and benefit they get there.
- **mT0-large** ✓: Desire for the rice, love for the relatives
- **Qwen3.5-2B** ✓: The desire for the rice, love for the relatives
- **Sarvam-1** ✓: This means that when you have a strong desire or want something, it is easy to forget about other things and focus on getting what you want. It can also mean that if your family members are important to you, they will be more likely to get what you want because you care about them.

## 62. One to trim the moustache of the man who drinks gruel  (figurative)

- **Gold:** A mocking saying about those who indulge in show and luxury beyond their means even in poverty.
- **mT0-large** ✓: One to trim the moustache of the man who drinks gruel
- **Qwen3.5-2B** ✓: One to trim the moustache of the man who drinks gruel
- **Sarvam-1** ✓: This means that if you are drinking something like gruel, then it is better not to drink too much because it will make your mouth feel uncomfortable and also give you a bad taste. It's best to have just enough so that you don't get sick or ruin your

## 63. One way or another, the sons of Kunti don't have eight kingdoms  (figurative)

- **Gold:** It may mean that after so much effort, they didn't get the expected gain in the end.
- **mT0-large** ✗: The sons of Kunti don't have eight kingdoms.
- **Qwen3.5-2B** ✓: The sons of Kunti don't have eight kingdoms.
- **Sarvam-1** ✓: This means that no matter how hard you try to achieve something, it will not always be successful. It is a reminder that sometimes things just won't work out as planned.

## 64. A time for the mother-in-law, a time for the daughter-in-law  (figurative)

- **Gold:** Everyone has their own time of authority; it is not permanent, and as time changes, authority changes hands.
- **mT0-large** ✓: A time for the mother-in-law, a time for the daughter-in-law
- **Qwen3.5-2B** ✓: A time for the mother-in-law, a time for the daughter-in-law.
- **Sarvam-1** ✓: This means that there is no point in trying to change someone's behavior or attitude if they are not willing to change themselves. It suggests that it is better to accept people as they are and focus on improving your own life rather than trying to force them to conform to your expectations. </

## 65. Desire is the root of sorrow  (literal)

- **Gold:** The more desires grow, the more sorrow grows; desire is the cause of sorrow.
- **mT0-large** ✗: Desire is the root of sorrow
- **Qwen3.5-2B** ✓: Desire is the root of sorrow.
- **Sarvam-1** ✓: This means that when you desire something, it can cause sadness or disappointment if you cannot get what you want. It's like a seed that grows into a tree and then produces fruit. If you plant a bad seed (desire), it will grow into a bad tree (sor

## 66. People fell upon people and the neck became empty  (figurative)

- **Gold:** It may mean that since many people rushed and fell over one another, nothing was left in the end.
- **mT0-large** ✓: People fell upon people and the neck became empty
- **Qwen3.5-2B** ✓: The neck became empty
- **Sarvam-1** ✓: This means that when you are angry, your anger can make others feel bad about themselves. It is important to be aware of this so we don't hurt other people with our words or actions.

## 67. Sin done unknowingly has a remedy once known  (literal)

- **Gold:** If one admits and repents of a mistake done unknowingly once one knows of it, there is a remedy for it.
- **mT0-large** ✓: A sin done unknowingly has a remedy once known.
- **Qwen3.5-2B** ✓: Sin done unknowingly has a remedy once known
- **Sarvam-1** ✓: This means that if you do something wrong without knowing it, there is still hope for redemption or forgiveness later on. It's like saying "the sooner you admit your mistake, the better."

## 68. Where there is affection, there is sorrow  (figurative)

- **Gold:** The more one loves someone, the more worry and pain there is about them.
- **mT0-large** ✗: Where there is affection, there is sorrow
- **Qwen3.5-2B** ✓: Where there is affection, there is sorrow
- **Sarvam-1** ✓: This means that when you have a strong feeling for someone or something, it can cause pain and suffering. It's like having two hands on a hot stove - if you want to take care of them both at once, they will get hurt! So sometimes we need to choose which things are

## 69. Even if it is his sister's gold, the goldsmith won't leave without stealing  (figurative)

- **Gold:** One who looks to professional profit won't leave without taking his cut even from his own relatives' work.
- **mT0-large** ✓: Even if it is his sister's gold, the goldsmith won't leave without stealing
- **Qwen3.5-2B** ✓: The goldsmith is a thief.
- **Sarvam-1** ✓: This means that even if someone has something valuable (like a piece of jewelry), they will not give up their possession unless they are forced to do so or have no other choice. The phrase comes from the idea that people who work with precious metals and gems (goldsmiths

## 70. Six bundles of sacred ash for one who doesn't have five bundles  (figurative)

- **Gold:** The meaning is not clear; it may be a saying about the irony of someone lacking a necessity getting an unnecessary extra.
- **mT0-large** ✓: A man who has five bundles of sacred ash
- **Qwen3.5-2B** ✓: The meaning of the proverb is that the person who doesn't have five bundles of sacred ash is not worthy of receiving six bundles of sacred ash.
- **Sarvam-1** ✓: This means that if you don't have something, it is better to have less than nothing. It can also be said as "less is more". The proverb comes from a story about an old man who had six bundles of sacred ash and was asked how many he would give away

## 71. If you marry the one you wanted and wanted, you got a husband who beats  (figurative)

- **Gold:** What one desired so much turns out in the end to be a trouble.
- **mT0-large** ✓: If you marry the one you wanted and wanted, you get a husband who beats
- **Qwen3.5-2B** ✓: If you marry the one you wanted and wanted, you got a husband who beats
- **Sarvam-1** ✓: This means that if you are not happy with your partner or marriage, then it is better to leave than stay. It's like saying "if you don't want something bad enough, you might as well get it".

## 72. Like the fence rising up and grazing the field  (figurative)

- **Gold:** The one who should protect betrays the trust and causes harm.
- **mT0-large** ✓: Like the fence rising up and grazing the field
- **Qwen3.5-2B** ✓: The fence is rising up and grazing the field.
- **Sarvam-1** ✓: This means that when you build a barrier, it will eventually grow over or cover what was intended to be protected. It is not always easy to control something once it has started growing. [/INST]

## 73. A hemp god, a toddy-drinking priest  (figurative)

- **Gold:** Master and servant are both of the same kind of bad quality and are well matched.
- **mT0-large** ✗: A hemp god, a toddy-drinking priest
- **Qwen3.5-2B** ✓: A hemp god, a toddy-drinking priest
- **Sarvam-1** ✓: This is an old English saying that means someone who drinks too much alcohol and doesn't think straight. It was used when people were drunk on beer or wine. The phrase "hemp god" refers to cannabis (a plant), which was once called hemp because it was made

## 74. There are no poor in desire  (literal)

- **Gold:** In the matter of desires nobody is poor; even the rich have desires.
- **mT0-large** ✓: There are no poor in desire.
- **Qwen3.5-2B** ✓: There are no poor in desire
- **Sarvam-1** ✓: This means that if you have enough money to live comfortably, then there is nothing wrong with having a little extra for yourself or your family. It's not about being rich or poor; it's about finding balance and enjoying life without worrying too much about material possessions.

## 75. Like giving charge to a scorpion  (figurative)

- **Gold:** Giving authority or responsibility to someone of a harmful nature is dangerous.
- **mT0-large** ✓: Like giving charge to a scorpion
- **Qwen3.5-2B** ✓: Like giving charge to a scorpion
- **Sarvam-1** ✓: This means that if you give someone too much responsibility, they will become angry and do something bad. It is like giving a scorpion its own stingers so it can attack itself.

## 76. One without worries sleeps even in the marketplace  (figurative)

- **Gold:** One who has no worry at all sleeps peacefully even in the noisiest place.
- **mT0-large** ✓: One without worries sleeps even in the marketplace
- **Qwen3.5-2B** ✓: One without worries sleeps even in the marketplace
- **Sarvam-1** ✓: This means that if you are not worrying about anything, then you will be able to get a good night's rest no matter where you are or what is happening around you. It suggests that having too many things on your mind can make it hard for you to relax and fall asleep.

## 77. Patience is greater than charity  (literal)

- **Gold:** It may mean that patience and calmness are a greater virtue than giving charity.
- **mT0-large** ✓: Patience is greater than charity
- **Qwen3.5-2B** ✓: Patience is greater than charity
- **Sarvam-1** ✓: This means that patience can be more powerful and effective than charity or kindness towards others. It suggests that sometimes, it's better to wait for something rather than giving up too quickly.

## 78. Wherever you go, in whichever direction, sorrow doesn't go away  (literal)

- **Gold:** Wherever one goes, one cannot escape hardships and sorrows; they must be faced.
- **mT0-large** ✓: Wherever you go, in whichever direction, sorrow doesn't go away
- **Qwen3.5-2B** ✓: Wherever you go, in whichever direction, sorrow doesn't go away
- **Sarvam-1** ✓: This means that wherever we are or whatever situation we find ourselves in, there is always going to be some kind of sadness or pain present. It can never be completely eliminated from our lives. [/INST]

## 79. Money is the big uncle (money is supreme)  (literal)

- **Gold:** In the world money carries the most value and respect; everyone honors one who has money.
- **mT0-large** ✓: Money is the big uncle (money is supreme)
- **Qwen3.5-2B** ✓: Money is the big uncle (money is supreme)
- **Sarvam-1** ✓: This means that money is very important and it can do a lot for you, but if you don't have enough money then you will be unable to achieve your goals or dreams. It also implies that having too much money isn't necessarily better than not having any at all. [/INST]

## 80. Even if the god gives a boon, the priest won't  (figurative)

- **Gold:** Even if the higher-ups sanction it, the officer or middleman in between creates obstacles and prevents the work from being done.
- **mT0-large** ✗: The priest will not give a boon.
- **Qwen3.5-2B** ✓: The god gives a boon, but the priest won't.
- **Sarvam-1** ✓: This means that even when you get something good from someone else (like getting money or help), it doesn't mean they will give it to you freely. They might try to keep it for themselves instead. It's like trying to catch fish with your bare hands - no matter how hard you

## 81. The distant hill looks smooth to the eye  (figurative)

- **Gold:** A distant object or place looks good; its hardships are known only when one goes near.
- **mT0-large** ✓: The distant hill looks smooth to the eye
- **Qwen3.5-2B** ✓: The distant hill looks smooth to the eye
- **Sarvam-1** ✓: This means that things appear different from a distance than they really are. It is often used when someone thinks something will be easy or simple, but it turns out to be more difficult than expected.

## 82. When given as charity for dharma, they went to the backyard and measured it by the cubit  (figurative)

- **Gold:** It may refer to people who ungratefully measure and find fault even with what was given for free.
- **mT0-large** ✓: When given as charity for dharma, they went to the backyard and measured it by the cubit
- **Qwen3.5-2B** ✓: The meaning of the proverb is that when given as charity for dharma, they went to the backyard and measured it by the cubit.
- **Sarvam-1** ✓: This means that when you give something away or share with others, you should do so generously without expecting anything in return. It's important to be mindful of how much we are giving and not just focusing on what we get out of it. The phrase "cubit" is

## 83. Everyone does it for the belly, for a span of cloth  (literal)

- **Gold:** Everyone works for food and clothing, that is, for a livelihood.
- **mT0-large** ✓: Everyone does it for the belly, for a span of cloth
- **Qwen3.5-2B** ✓: Everyone does it for the belly, for a span of cloth
- **Sarvam-1** ✓: This means that people do things they shouldn't because they need something more important than what they are doing. For example, if someone is hungry and has to steal food from another person, then this would be an example of "everyone does it for the belly". The phrase

## 84. Not all light is light; the word of truth is the light  (figurative)

- **Gold:** Glitter and show don't point the true path; truthful speech is the real light.
- **mT0-large** ✓: The word of truth is the light
- **Qwen3.5-2B** ✓: The word of truth is the light.
- **Sarvam-1** ✓: The proverb means that not everything we see or hear is true, and it's important to seek out the truth through careful thought and investigation. It encourages us to be discerning and critical thinkers rather than blindly accepting what others tell us.

## 85. If it hits the left crown of the head, it touched the right crown  (figurative)

- **Gold:** The meaning is unclear; it may be that an action or word directed at one person touches another and affects them.
- **mT0-large** ✓: If it hits the left crown of the head, it touched the right crown
- **Qwen3.5-2B** ✓: If it hits the left crown of the head, it touched the right crown
- **Sarvam-1** ✓: This means that if something happens to you on your way up or down, it will happen to someone else too. It is a warning not to be greedy and take advantage of others.

## 86. A foot that has stumbled stumbles more  (figurative)

- **Gold:** One who has once met with an accident or trouble is more likely to meet the same trouble again and again.
- **mT0-large** ✗: A foot that has stumbled stumbles more
- **Qwen3.5-2B** ✓: A foot that has stumbled more
- **Sarvam-1** ✓: This means that if you make a mistake, it will be harder for you to do something else correctly next time. It's like when someone trips and falls - they might not fall again right away, but their chances are lower than if they hadn't fallen at all.

## 87. At eight years, my son turned into a stalk  (figurative)

- **Gold:** It seems to be a parent's lament that at a young age the son has become good for nothing and doesn't listen to what he's told.
- **mT0-large** ✗: At eight years, my son turned into a stalk
- **Qwen3.5-2B** ✓: At eight years, my son turned into a stalk.
- **Sarvam-1** ✓: This means that at an early age, your child can become something you don't want them to be. It is important for parents to teach their children good values and morals from a young age so they will grow up to be responsible adults. </s>

## 88. When even such gods are in distress, will a leg-broken god get Kailasa?  (figurative)

- **Gold:** When even great gods are in difficulty, would a lame god get Kailasa? That is, when even the mighty face hardship, it is hard for the weak to get happiness.
- **mT0-large** ✓: When even such gods are in distress, will a leg-broken god get Kailasa?
- **Qwen3.5-2B** ✓: When even such gods are in distress, will a leg-broken god get Kailasa?
- **Sarvam-1** ✓: This is an example of a proverb that means "If you're not perfect, don't expect perfection from others." It uses the metaphor of a broken leg to illustrate how someone who has been injured or harmed can still be expected to perform well. The phrase comes from the

## 89. All the colors were swallowed by the soot  (figurative)

- **Gold:** Just as one black smudge covers all colors, one big mistake or bad thing hides all the rest of the good.
- **mT0-large** ✗: All the colors were swallowed by the soot
- **Qwen3.5-2B** ✓: The soot is a dark, black substance that covers everything.
- **Sarvam-1** ✓: The phrase means that something has been completely covered or hidden, and nothing can be seen anymore. It is a metaphorical expression used to describe things that have become invisible or unrecognizable due to excessive darkness or pollution.

## 90. If everyone sits in the palanquin, who will carry it?  (figurative)

- **Gold:** If everyone sits in the palanquin, who carries it? That is, if everyone wants to be the boss, who will do the work?
- **mT0-large** ✓: The king will carry it.
- **Qwen3.5-2B** ✓: If everyone sits in the palanquin, who will carry it?
- **Sarvam-1** ✓: The proverb is a reminder that if we all do the same thing without thinking about how to achieve our goals or solve problems, then no one will be able to accomplish anything. It's important to think critically and work together as a team to get things done. </s>

## 91. When two hands clap, there's a sound  (figurative)

- **Gold:** Clapping needs two hands; likewise a quarrel or problem involves both persons; one alone is not the cause.
- **mT0-large** ✗: When two hands clap, there's a sound
- **Qwen3.5-2B** ✓: When two hands clap, there's a sound
- **Sarvam-1** ✗: This means that when people work together or help each other, they can achieve great things. It is like saying "two heads are better than one". [/INST]

## 92. Trusting two Dasas, the blind Dasa was ruined  (figurative)

- **Gold:** 'The blind Dasa who trusted two Dasas was ruined' means that if you rely on two people, each neglects the task thinking the other will see to it, and the one who trusted suffers the loss.
- **mT0-large** ✓: The blind Dasa was ruined by trusting two Dasas.
- **Qwen3.5-2B** ✓: The blind Dasa was ruined because he trusted two Dasas.
- **Sarvam-1** ✓: The proverb is a warning against trusting too many people or things at once. It suggests that if you put your faith in more than one source, it can lead to disaster. This is because each person or thing may have their own agenda and interests, which could ultimately harm you.

## 93. One who has climbed will come down  (figurative)

- **Gold:** One who has risen high must come down one day; that is, power or wealth is not permanent.
- **mT0-large** ✓: A man who has climbed will come down.
- **Qwen3.5-2B** ✓: One who has climbed will come down
- **Sarvam-1** ✓: This means that if you have worked hard to achieve something, then it is likely that you will not be able to keep doing so forever. You may get tired or lose interest and stop trying. It's important to remember why you started and what you hope to achieve before giving up.

## 94. A husband-and-wife quarrel lasts only until they've eaten and gone to sleep  (literal)

- **Gold:** A husband-and-wife quarrel ends by the time they have eaten and gone to bed; it doesn't last long.
- **mT0-large** ✓: A husband-and-wife quarrel lasts only until they've eaten and gone to sleep
- **Qwen3.5-2B** ✓: The husband and wife quarrel lasts only until they've eaten and gone to sleep
- **Sarvam-1** ✓: This means that when you have a disagreement with someone, it is best to let it go because once you stop fighting or arguing, then you can both relax and get on with your lives. It doesn't mean that you should never argue at all, but rather that if you do start

## 95. Like holding the tail of the winning ox  (figurative)

- **Gold:** Like holding on to the tail of the winning ox, an opportunistic nature of joining those who have succeeded and profiting oneself.
- **mT0-large** ✗: Like holding the tail of the winning ox
- **Qwen3.5-2B** ✗: Like holding the tail of the winning ox
- **Sarvam-1** ✗: This means that when you are trying to get something, it is better to be patient and not rush things. It's like waiting for a horse to run before you try to catch its tail. If you do this, you will have more success than if you tried to catch the tail while

## 96. A Brahmastra on a sparrow?  (figurative)

- **Gold:** Using the Brahmastra to kill a sparrow is excessive; that is, it is not right to take a very big step for a small matter.
- **mT0-large** ✗: A Brahmastra on a sparrow?
- **Qwen3.5-2B** ✓: A Brahmastra on a sparrow?
- **Sarvam-1** ✓: This is an expression that means "a nuclear weapon on something as small and harmless as a bird". It's used to describe something so powerful or destructive, it can destroy anything without regard for its size or importance. The phrase comes from Hindu mythology where Brahma was said to have

## 97. Winnow when the wind comes, sell when the price comes  (figurative)

- **Gold:** One must winnow grain only while the wind blows and sell when the price is good; that is, use an opportunity at once when it comes.
- **mT0-large** ✓: Winnow when the wind comes, sell when the price comes
- **Qwen3.5-2B** ✓: The meaning of the proverb is that you should be prepared to take action when the right opportunity arises.
- **Sarvam-1** ✓: This means that you should not try to make money while prices are low and then wait for them to go up before selling your stock or property. You need to be patient and wait until the right time to do so.

## 98. No fuss or noise at all, Govinda Bhatta fell into the well  (figurative)

- **Gold:** This saying describes an event that happens unexpectedly, without any fuss or confusion and without any warning.
- **mT0-large** ✓: Govinda Bhatta fell into the well
- **Qwen3.5-2B** ✓: Govinda Bhatta fell into the well.
- **Sarvam-1** ✓: This means that if you do something without any effort and with no fuss or noise then it is a good thing to do. It's like falling into a well - there will be some noise but nothing else.

## 99. In name the wife is missing, the son's name is Nanjunda  (figurative)

- **Gold:** It seems to be a saying about empty show of name only: a relationship or position exists only in name, with nothing in reality.
- **mT0-large** ✓: In name the wife is missing, the son's name is Nanjunda
- **Qwen3.5-2B** ✓: The wife is missing, the son's name is Nanjunda.
- **Sarvam-1** ✓: This means that when a woman leaves her husband and goes to live with another man, she will be known as his "wife" even though she has no legal rights or responsibilities towards him anymore. The phrase comes from India where it was used for centuries before being translated into English. It

## 100. When told 'Gone, ghost?', it said 'I came back through the window'  (figurative)

- **Gold:** Like saying 'I came through the window' when told 'Have you gone, ghost?'; even if you drive off nuisances, they come back by another route.
- **mT0-large** ✓: When told 'Gone, ghost?', it said 'I came back through the window'
- **Qwen3.5-2B** ✓: The meaning of the proverb is that when told 'Gone, ghost?', it said 'I came back through the window'
- **Sarvam-1** ✓: This means that when someone says they have gone away or left, you should not believe them because they might be lying and come back again. It is like a ghost who comes back through the window after being gone for a while. [/INST]

## 101. In a ruined village, whoever remains is the headman (Gowda)  (figurative)

- **Gold:** When a village is ruined and no one is left, whoever remains becomes the Gowda (headman); when no worthy people are left, even an ordinary person gets a main position.
- **mT0-large** ✗: In a ruined village, whoever remains is the headman (Gowda)
- **Qwen3.5-2B** ✗: The headman is the one who remains after the village is destroyed.
- **Sarvam-1** ✗: This means that if you are left alone after something bad happens to your community or town, then it's up to you to take charge and make things better again. It doesn't matter how big or small your role may be; everyone has an important part to play when trying to rebuild

## 102. Drop by drop becomes a stream, ear by ear becomes paddy  (figurative)

- **Gold:** Drops join into a stream, ears of grain join into a heap of paddy; small efforts or savings add up into something big.
- **mT0-large** ✓: Drop by drop becomes a stream, ear by ear becomes paddy
- **Qwen3.5-2B** ✓: The meaning of the proverb is that small efforts, when repeated consistently, can lead to significant results.
- **Sarvam-1** ✓: This means that small actions can add up to something big over time. It's like dropping water on a rock - it might not seem like much at first, but if you keep adding more and more drops, eventually the rock will be washed away. The same idea applies to learning new

## 103. The wide-mouthed Dasa who sings the same song again and again  (figurative)

- **Gold:** Like a grinning Dasa singing the song he already sang again and again; a boring habit of repeating or doing the same thing over and over.
- **mT0-large** ✗: The wide-mouthed Dasa who sings the same song again and again
- **Qwen3.5-2B** ✓: The wide-mouthed Dasa who sings the same song again and again
- **Sarvam-1** ✓: This means that someone who is always singing the same thing, or doing the same things over and over again, will eventually become bored with it. They are not learning anything new from their actions.

## 104. To the parents the bandicoot is a darling, to the companions the monkey is a darling  (figurative)

- **Gold:** The first half means parents find their children dear however they are; the second half is unclear.
- **mT0-large** ✓: The bandicoot is a darling to the parents, and the companions the monkey is a darling to the companions.
- **Qwen3.5-2B** ✓: The bandicoot is a darling to the parents, but the monkey is a darling to the companions.
- **Sarvam-1** ✓: The first part of this saying means that people like animals who are cute and small. This is because they can be easily taken care of by their owners. In other words, it's easier for them to take care of these animals than larger ones. The second part of the saying refers to

## 105. The eldest brother's habit goes to everyone in the house  (figurative)

- **Gold:** Everyone else in the house imitates the habit of the eldest brother; elders' conduct affects the younger ones.
- **mT0-large** ✗: The eldest brother's habit goes to everyone in the house
- **Qwen3.5-2B** ✓: The eldest brother's habit goes to everyone in the house.
- **Sarvam-1** ✓: This means that when you are older, your habits and ways of doing things will be passed on to others in your family. It is a way of saying that people learn from their parents or other adults who have been around longer than they have.

## 106. A backyard plant is not medicine  (figurative)

- **Gold:** No one considers the plant in one's own backyard to be medicine; the value of nearby acquaintances or things isn't recognized.
- **mT0-large** ✗: A backyard plant is not medicine
- **Qwen3.5-2B** ✗: A backyard plant is not medicine
- **Sarvam-1** ✗: This means that if you don't need something, then it doesn't make sense to spend time or money on it. It also suggests that sometimes things we think are important might not be as valuable as we believe they are.

## 107. Why the club-wielding chief's permission for river water?  (figurative)

- **Gold:** To use river water that belongs to everyone, the headman's permission isn't needed; for what is open to all, no one's permission is necessary.
- **mT0-large** ✓: The club-wielding chief's permission for river water is a very limited amount.
- **Qwen3.5-2B** ✓: The chief's permission for river water is a metaphor for the chief's permission for the people to use the river water.
- **Sarvam-1** ✓: The proverb is a play on words, as "club" can also mean "permission". It refers to someone who has been given permission by their superior (the club) to do something that they would not normally be allowed to do. In this case, it could refer to a person

## 108. In the beginning the washerman lifted the sack again and again and beat it on the stone  (figurative)

- **Gold:** As the washerman at first lifted and beat the sack again and again, one shows excessive enthusiasm at the start of a new task, which doesn't last long.
- **mT0-large** ✗: The washerman lifted the sack again and again and beat it on the stone
- **Qwen3.5-2B** ✓: The washerman lifted the sack again and again and beat it on the stone
- **Sarvam-1** ✓: The proverb is a warning to not repeat mistakes or actions that have already been done, as they may be repeated with similar results. It suggests that if you do something wrong once, you should try to correct your mistake before it becomes too late.

## 109. An old patient is better than a new doctor  (figurative)

- **Gold:** An experienced old patient knows more about the disease than a newly arrived doctor; that is, experience is better than fresh book knowledge.
- **mT0-large** ✓: A new doctor is better than a old patient.
- **Qwen3.5-2B** ✓: An old patient is better than a new doctor because the patient has already experienced the doctor's skills and can recognize when they are ineffective.
- **Sarvam-1** ✓: This means that it's better to have an experienced person who has been through many situations and knows what they are doing, rather than someone who is just starting out with no experience or knowledge. It's like having a veteran athlete instead of a beginner player. The veteran can

## 110. No flour for the belly, jasmine flowers for the hair knot  (figurative)

- **Gold:** Like wearing jasmine flowers on the head though there is no flour to eat; spending on show though there is no money even for basic needs.
- **mT0-large** ✗: A few flowers for the hair knot.
- **Qwen3.5-2B** ✓: No flour for the belly, jasmine flowers for the hair knot.
- **Sarvam-1** ✓: This means that if you don't have enough money to buy food or other necessities, then it is better not to spend your money on things like jewelry or fancy clothes because they will only make you feel worse when you can't afford them anymore. It's like

## 111. The god who gave birth will make you graze grass  (figurative)

- **Gold:** The god who created us will not let us live by grazing grass; that is, the one who gave life also shows the way to live, so there is no need to worry too much.
- **mT0-large** ✓: The god who gave birth will make you graze grass
- **Qwen3.5-2B** ✓: The god who gave birth will make you graze grass
- **Sarvam-1** ✓: This means that if someone is born into a position or situation, they are likely to stay there for a long time. It's like saying "the grass will always be greener on the other side". [/INST]

## 112. At a mad widow's wedding, the one who ate is the clever one  (figurative)

- **Gold:** At a chaotic, crazy wedding, the one who ate and left is clever; that is, one who took the benefit he wanted in a disorderly situation is smart.
- **mT0-large** ✓: A mad widow's wedding, the one who ate is the clever one
- **Qwen3.5-2B** ✓: The one who ate is the clever one.
- **Sarvam-1** ✓: This means that when you are with someone who has no sense or common sense, it can be very dangerous to eat something they offer you because you might end up getting sick. It also implies that if you have any sense and know what not to do, then you will avoid eating anything from this person

## 113. Along with the flower, the fiber reached heaven  (figurative)

- **Gold:** The fiber (thread) joined with the flower also reached the god's feet; through the company of good people, even ordinary ones get good results.
- **mT0-large** ✓: Along with the flower, the fiber reached heaven
- **Qwen3.5-2B** ✓: The fiber is the same as the flower.
- **Sarvam-1** ✓: The phrase means that something is worth more than its appearance or value. It suggests that there are often hidden benefits to things we may not initially see or appreciate. This can be applied to many aspects of life, such as relationships, career choices, and personal growth. For example, someone who works

## 114. Let the festival go well, let the wall be safe, let the visiting in-laws eat and go  (figurative)

- **Gold:** A wish that the festival go well without any trouble, that the house suffer no damage, and that the visiting relatives eat and leave happy.
- **mT0-large** ✓: Let the festival go well, let the wall be safe, let the visiting in-laws eat and go
- **Qwen3.5-2B** ✓: Let the festival go well, let the wall be safe, let the visiting in-laws eat and go.
- **Sarvam-1** ✓: This means that you should not worry about things that are out of your control or can't change. You should focus on what you can do to make sure everything goes smoothly. It is a reminder to stay calm and focused when faced with unexpected challenges. </s>

## 115. Worry at night ruins sleep, worry in the day ruins work  (literal)

- **Gold:** If you worry at night, sleep is ruined; if you worry in the day, work is ruined.
- **mT0-large** ✓: Worry at night ruins sleep, worry in the day ruins work
- **Qwen3.5-2B** ✓: Worry at night ruins sleep, worry in the day ruins work.
- **Sarvam-1** ✓: This means that if you are worried about something during the day, it will affect your ability to do things well and make you tired or stressed out by the time you get home. It's like trying to run a race while carrying a heavy backpack - you won't be able to

## 116. Say it as it is and thunder strikes Siddappa  (figurative)

- **Gold:** Telling things as they are angers some people; the plain truth isn't liked by everyone.
- **mT0-large** ✗: Say it as it is and thunder strikes Siddappa
- **Qwen3.5-2B** ✓: The meaning of the proverb is that the truth is often misunderstood or misinterpreted by people.
- **Sarvam-1** ✗: This means that if you say something directly, then people will take notice. If they don't like what you said, they might get angry or upset with you. But if you keep quiet about your feelings, no one knows how you feel. It can be hard to know when to speak

## 117. Like falling in the daytime into a well you saw at night  (figurative)

- **Gold:** Like falling by day into a well one saw at night; the folly of getting caught in a danger or mistake despite knowing of it.
- **mT0-large** ✓: Like falling into a well you saw at night
- **Qwen3.5-2B** ✓: Like falling in the daytime into a well you saw at night
- **Sarvam-1** ✓: This means that if you do something without thinking about it, then you will end up with bad consequences. It is like trying to jump into a deep well when there are no lights and only darkness around. You might not even realize how far down you have fallen until it's too late

## 118. Even if the whole body sinks, the nose stays up  (figurative)

- **Gold:** Like holding the nose up even when the whole body sinks in water; not giving up one's arrogance and pride even when completely ruined.
- **mT0-large** ✗: Even if the whole body sinks, the nose stays up
- **Qwen3.5-2B** ✓: The nose is the most important part of the body.
- **Sarvam-1** ✗: This means that even when you are facing a difficult situation or problem, it is important to keep your head up and not give up. It's like saying "don't let go of hope" because no matter how bad things get, there will always be something good left for us to hold

## 119. Will the one who was merely kept stay? Will the one who was wedded be cut off?  (figurative)

- **Gold:** It may mean that those kept temporarily are not permanent and those wedded cannot easily be abandoned; but the gender and form of the text are unclear.
- **mT0-large** ✗: The one who was kept alone will stay.
- **Qwen3.5-2B** ✓: The one who was merely kept stay? Will the one who was wedded be cut off?
- **Sarvam-1** ✓: This is a Chinese saying that means "the person who has been married will not be separated from his or her spouse". It's used to describe someone who has been married and cannot be separated from their spouse, even if they want to leave. The phrase comes from an old story about

## 120. News of the town you are in shouldn't be raised where you are; news of the town you have left shouldn't be raised where you have gone  (figurative)

- **Gold:** It seems to be a saying that news of the town where one lives shouldn't be spread there, and news of another town shouldn't be told where one has gone; the text is incomplete.
- **mT0-large** ✗: The news of the town you are in shouldn't be raised where you are; the news of the town you have left shouldn't be raised where you have gone
- **Qwen3.5-2B** ✓: The town you are in shouldn't be raised where you are; news of the town you have left shouldn't be raised where you have gone
- **Sarvam-1** ✓: This means that if you want to keep your good reputation, don't talk about things that happened to you when you were away from it. If you do, people will think badly of you and they might start talking about what you did while you were away.

## 121. Said it as it was, and the face turned hawk-like  (figurative)

- **Gold:** When you say things as they are, the listener makes an angry, hawk-like face; telling the truth displeases some people.
- **mT0-large** ✗: The face turned hawk-like.
- **Qwen3.5-2B** ✓: Said it as it was, and the face turned hawk-like
- **Sarvam-1** ✓: This means that if you say something directly and honestly, people will take you seriously. If they don't like what you said, they won't be able to hide their feelings anymore. They might even look a bit "hawkish" or aggressive because they are trying to

## 122. What existed was lost through the medicine's effect  (figurative)

- **Gold:** Even the health one had was lost through the effect of the medicine; the remedy tried to fix things and ruined even the good that existed.
- **mT0-large** ✓: What existed was lost through the medicine's effect
- **Qwen3.5-2B** ✓: The medicine's effect was the cause of the loss of what existed.
- **Sarvam-1** ✓: The proverb means that if something is not done, it will be lost forever. It emphasizes the importance of taking action to prevent regret or loss. </s>

## 123. A headman (Gowda) where he is, deaf where he goes  (figurative)

- **Gold:** This proverb describes a person who acts big in his own place and stays silent, as if speechless, when he goes elsewhere.
- **mT0-large** ✓: A headman (Gowda) where he is, deaf where he goes
- **Qwen3.5-2B** ✓: A headman (Gowda) where he is, deaf where he goes
- **Sarvam-1** ✓: This means that a person who has authority over others will not listen to them when they are away from their position or office. They may be able to do what they want while they are at work but once they leave it, they have no control and can't get anyone else to follow their orders

## 124. Kin as far as Ikkeri, but no cloth to cover his shame  (figurative)

- **Gold:** This saying suggests a state where one's name is spread all over town outside but inside there isn't even basic comfort.
- **mT0-large** ✓: Kin as far as Ikkeri, but no cloth to cover his shame
- **Qwen3.5-2B** ✓: Kin as far as Ikkeri, but no cloth to cover his shame
- **Sarvam-1** ✓: This means that even if you are very close to someone or something, it doesn't mean much if they don't have anything good about them. It is like saying "Kin as far as Ikkeri" which means "as near as possible". But this person has nothing good

## 125. Don't set the house on fire because the rats have increased  (figurative)

- **Gold:** This saying says one shouldn't take an extreme step like setting fire to the whole house out of fear of a small trouble.
- **mT0-large** ✓: The rats have increased in the house.
- **Qwen3.5-2B** ✓: The house is on fire because the rats have increased.
- **Sarvam-1** ✓: This means that you shouldn't do something to your business or home, just because it might cause problems for someone else. It is better to be safe than sorry.

## 126. A cat as witness in the rat's dispute  (figurative)

- **Gold:** This proverb says there is no justice when the weak person's enemy is the witness or judge in his dispute.
- **mT0-large** ✓: A cat is witness in the rat's dispute.
- **Qwen3.5-2B** ✗: A cat as witness in the rat's dispute
- **Sarvam-1** ✓: This means that a person who is not involved in an argument can be asked to testify about what they saw, and their word will carry more weight than someone else’s.

## 127. Better to live three days as a tiger than a hundred days as a rat  (figurative)

- **Gold:** Better to live a short time with self-respect than a long time in fear and humiliation.
- **mT0-large** ✓: Better to live three days as a tiger than a hundred days as a rat
- **Qwen3.5-2B** ✓: The tiger is a symbol of strength and power, while the rat represents weakness and cowardice, so the proverb means that it is better to live a short life with courage and bravery than to live a long life with fear and submission.
- **Sarvam-1** ✓: This means that it is better to be alive for just a few days or hours, rather than living a long time but being unhappy and miserable. It's like saying "the grass is always greener on the other side". The idea behind this proverb is that people often

## 128. Said 'come here, come here' and he snatched even the house that was there  (figurative)

- **Gold:** This proverb describes a cheat who, if given a little shelter, grabs the very place the giver has.
- **mT0-large** ✓: He said 'Come here, come here' and he snatched even the house that was there.
- **Qwen3.5-2B** ✓: The meaning of the proverb is that the speaker is trying to get the attention of the listener.
- **Sarvam-1** ✓: This means to be too greedy or selfish for what you want. If someone is always trying to get something they don't have, then eventually it will catch up with them. It can also mean that if you try to take more than you need from a situation, you may end up

## 129. Though the wrestler fell, his moustache didn't get dirty  (literal)

- **Gold:** A saying about a person who doesn't admit defeat even after losing and keeps up his arrogance.
- **mT0-large** ✗: The wrestler fell, his moustache didn't get dirty.
- **Qwen3.5-2B** ✗: The wrestler fell, but his moustache didn't get dirty.
- **Sarvam-1** ✗: This means that even if you lose a battle or fight, your pride and self-respect will not be damaged. You can still keep your sense of honor and dignity.

## 130. Are the people mad or is the fair mad?  (figurative)

- **Gold:** This saying suggests people going mindlessly in the frenzy of the crowd.
- **mT0-large** ✗: People are mad, or is the fair mad?
- **Qwen3.5-2B** ✓: The people are mad because they are not fair.
- **Sarvam-1** ✓: This means that you can't tell if someone is crazy just by looking at them, so don't judge a book by its cover! It also suggests that sometimes things aren't as they seem on the surface. [/INST]

## 131. If there's money, Kailasa; if not, exile in the forest  (literal)

- **Gold:** This proverb says the importance of money: with money, happiness; without it, hardship.
- **mT0-large** ✓: If there's money, Kailasa; if not, exile in the forest
- **Qwen3.5-2B** ✓: If there's money, Kailasa; if not, exile in the forest
- **Sarvam-1** ✓: This is a saying that means you can get what you want by using your resources wisely or by being creative and finding new ways to achieve it. It also suggests that when things are difficult, you should find another way to survive. The phrase comes from India, where Kailasa is a myth

## 132. Hardship and happiness are the two faces of life  (literal)

- **Gold:** This saying says that in life both hardship and happiness naturally come one after the other.
- **mT0-large** ✓: Hardship and happiness are the two faces of life
- **Qwen3.5-2B** ✓: Hardship and happiness are the two faces of life
- **Sarvam-1** ✓: This means that hardships or difficulties can be a part of our lives, but they don't have to define us. Happiness is also an important aspect of life, and it doesn't always come easily. The phrase suggests that we should learn to appreciate both aspects of life.

## 133. One who couldn't manage what was in hand took a lease on a kombe tree  (figurative)

- **Gold:** This saying criticizes someone who can't handle what is in his hands taking on an even bigger responsibility.
- **mT0-large** ✓: One who couldn't manage what was in hand took a lease on a kombe tree
- **Qwen3.5-2B** ✓: The meaning of the proverb is that one who couldn't manage what was in hand took a lease on a kombe tree.
- **Sarvam-1** ✗: This means that if you don't have control over something, then it is better to take a chance and try to get your hands on it rather than giving up completely. The proverb uses an example from nature (a kombe tree) to illustrate this point. A kombe tree

## 134. The sin of killing is remedied by eating  (figurative)

- **Gold:** This saying points to the senseless justification of claiming to fix the damage from a mistake by profiting from it.
- **mT0-large** ✓: The sin of killing is remedied by eating
- **Qwen3.5-2B** ✓: The sin of killing is remedied by eating
- **Sarvam-1** ✗: This means that if you do something wrong, it can be fixed or made right through doing something good. It's like saying "the pen is mightier than the sword". If someone does something bad, they can make up for it by doing something good.

## 135. A stalk in the hand is better than the bundle inside the mirror  (figurative)

- **Gold:** This proverb says a small thing in hand now is better than a big gain that may or may not come.
- **mT0-large** ✓: A stalk in the hand is better than the bundle inside the mirror
- **Qwen3.5-2B** ✓: A stalk in the hand is better than the bundle inside the mirror
- **Sarvam-1** ✓: This means that it's better to have something you can use right now, rather than having a lot of things you don't need or can't use. It's like picking up a stalk of grass instead of trying to get all the dirt out of your hands and then

## 136. Wisdom came after being ruined  (literal)

- **Gold:** This saying says that a person gains wisdom only after suffering loss or harm.
- **mT0-large** ✓: Wisdom came after being ruined.
- **Qwen3.5-2B** ✓: Wisdom came after being ruined
- **Sarvam-1** ✓: This means that sometimes you have to learn from your mistakes before you can become wise. It's like learning how to ride a bike - it takes practice and falls off many times before you get it right!

## 137. Though the pin is small, it runs the wind  (figurative)

- **Gold:** A saying meaning that a thing or person small in size is what runs a big system.
- **mT0-large** ✓: The pin is small, it runs the wind.
- **Qwen3.5-2B** ✓: The pin is small, but it can still run the wind.
- **Sarvam-1** ✓: This means that even though something may seem insignificant or unimportant at first glance, it can still have a significant impact on others. The phrase comes from an old English saying which was used to describe how a tiny object like a needle could be very powerful if you were able to

## 138. Fame is Kailasa, infamy is hell  (figurative)

- **Gold:** This proverb says the importance of a good reputation: a good name is heaven, a bad name is hell.
- **mT0-large** ✓: Fame is Kailasa, infamy is hell
- **Qwen3.5-2B** ✓: Fame is Kailasa, infamy is hell
- **Sarvam-1** ✓: This means that fame and infamy are both very bad things to have. They can be so powerful that they make you do terrible things.

## 139. Can a nose cut off in anger be restored in peace?  (figurative)

- **Gold:** This saying warns that the consequences of what is done in anger can't be fixed once one has calmed down.
- **mT0-large** ✓: A nose cut off in anger can be restored in peace.
- **Qwen3.5-2B** ✓: Can a nose cut off in anger be restored in peace?
- **Sarvam-1** ✓: No, it cannot. The phrase is saying that you can't undo something once it has happened. It also means that if someone hurts your feelings or makes you angry, there's no way to fix things between you two afterwards. You need time and patience to heal those

## 140. The monkey not only ruined itself but ruined the forest too  (figurative)

- **Gold:** This proverb describes a person who not only ruins himself but ruins those around him as well.
- **mT0-large** ✓: The monkey ruined itself and ruined the forest too.
- **Qwen3.5-2B** ✓: The monkey not only ruined itself but ruined the forest too
- **Sarvam-1** ✓: This means that if you do something wrong, it will affect everyone around you and even yourself. It's like a domino effect where one action leads to another.

## 141. A monkey-like fellow provoked, got struck by the pestle, and writhed  (figurative)

- **Gold:** A saying about one who provokes those stronger than himself, gets hurt and suffers.
- **mT0-large** ✓: A monkey-like fellow provoked, got struck by the pestle, and writhed
- **Qwen3.5-2B** ✓: A monkey-like fellow provoked, got struck by the pestle, and writhed.
- **Sarvam-1** ✓: This is a very old English saying that means to be angry or upset with someone who has done something wrong, you should not get involved in their problems because it will only make things worse for both of you. It's like getting hit by a heavy object - you can't do anything

## 142. She had the baby's gown stitched before the baby was born  (figurative)

- **Gold:** This proverb mocks hasty preparation made before the result is known.
- **mT0-large** ✗: She had the baby's gown stitched before the baby was born
- **Qwen3.5-2B** ✗: She had the baby's gown stitched before the baby was born.
- **Sarvam-1** ✓: This means that she made sure to have everything ready for when the baby arrived, so it would be a smooth transition from her old life to her new role as mother. It is like having a plan or preparation for something important. </s>

## 143. A pot of gold is not enough for one who sits and eats  (figurative)

- **Gold:** This saying says that however much wealth there is, it gets spent and runs out for those who sit and eat without working.
- **mT0-large** ✓: A pot of gold is not enough for one who sits and eats
- **Qwen3.5-2B** ✓: A pot of gold is not enough for one who sits and eats
- **Sarvam-1** ✗: This means that you need more than just a small amount to be happy or satisfied. You might have to work hard, save money, or do something special to get what you want. It's like trying to find a pot of gold at the end of a rainbow - it's

## 144. One who holds back when great anger comes is the wise one  (literal)

- **Gold:** One who patiently bears it even when very angry is truly wise.
- **mT0-large** ✓: The one who holds back when great anger comes is the wise one
- **Qwen3.5-2B** ✓: One who holds back when great anger comes is the wise one
- **Sarvam-1** ✓: This means that if you are able to control your temper and keep calm, then you will be seen as a person of wisdom. If you let your emotions get the better of you, people may think you're not very smart or strong.

## 145. Not seeing what you saw is best, seeing what you saw is middling, claiming to see what you didn't see is lowest  (literal)

- **Gold:** It is best to pretend not to see others' faults even when you have seen them; telling what you saw is middling; claiming to have seen what you didn't is bad.
- **mT0-large** ✗: The lowest thing you see is not seeing what you saw.
- **Qwen3.5-2B** ✓: The meaning of the proverb is that the best way to avoid mistakes is to not see what you saw, the middling way is to see what you saw, and the lowest way is to claim to see what you didn't see.
- **Sarvam-1** ✓: This means that it is better not to make a mistake than to be wrong about something and then have to correct your mistake later. It also suggests that if you don't know something, it may be better to just say nothing rather than making an incorrect statement.

## 146. Like pushing other people's children into a well to see how deep it is  (figurative)

- **Gold:** This proverb criticizes putting others in danger for one's own test or curiosity.
- **mT0-large** ✗: Like pushing other people's children into a well to see how deep it is
- **Qwen3.5-2B** ✓: Like pushing other people's children into a well to see how deep it is
- **Sarvam-1** ✓: This means that if you want something, you should try your best and not give up easily. If someone else has already done what you wanted to do, then don't be afraid to try harder than them. It will only make things worse for yourself.

## 147. Even if destitute, one should not become beholden  (literal)

- **Gold:** This saying says that however poor or troubled one is, one shouldn't fall into the debt of obligation to others' favors.
- **mT0-large** ✓: Even if destitute, one should not become beholden
- **Qwen3.5-2B** ✓: The meaning of the proverb is that one should not become dependent on others.
- **Sarvam-1** ✓: This means that even when you are poor or have nothing, it is important to stay strong and keep your head up. It's better to be able to help yourself than to rely on others for everything.

## 148. One can guard the threshing floor, but one cannot guard a corpse  (literal)

- **Gold:** This saying seems to say that a heap of grain can be guarded, but a dead body cannot be kept waiting for long.
- **mT0-large** ✗: One can guard the threshing floor, but one cannot guard a corpse
- **Qwen3.5-2B** ✗: One can guard the threshing floor, but one cannot guard a corpse
- **Sarvam-1** ✓: This means that you can protect your property and assets from harm or damage, but you cannot guarantee their safety against death or loss. It is often used to remind people not to take unnecessary risks or put too much trust in others. </s>

## 149. A built tank can't avoid its spillway; the house one was born in can't avoid parting  (figurative)

- **Gold:** This proverb says a daughter leaving her parental home after marriage is as inevitable as a tank overflowing through its spillway.
- **mT0-large** ✓: A built tank can't avoid its spillway; the house one was born in can't avoid parting
- **Qwen3.5-2B** ✓: The house one was born in can't avoid parting.
- **Sarvam-1** ✓: This means that you cannot escape your past, no matter how hard you try to change it or move on from it. It is like a tank with a spillway - if it has been filled up and put into use, there will always be some water coming out. Similarly, people are shaped

## 150. To get the work done, hold the donkey's feet  (figurative)

- **Gold:** This saying says that to get one's work done, one must bow even before the unworthy.
- **mT0-large** ✓: To get the work done, hold the donkey's feet
- **Qwen3.5-2B** ✓: The donkey's feet are the most important part of the donkey.
- **Sarvam-1** ✗: This means that if you want to get something done, then you need to make sure that someone is doing it for you or else they will not do it at all. It can also be used as a warning against being too lazy and letting things slide.

## 151. To the jaundiced eye, everything seen is yellow  (figurative)

- **Gold:** This proverb says that to one who has prejudice or a fault-finding eye, everything looks wrong.
- **mT0-large** ✓: The yellow is a very strange thing to see.
- **Qwen3.5-2B** ✓: The meaning of the proverb is that the jaundiced eye is a metaphor for a person who is biased or prejudiced.
- **Sarvam-1** ✓: This means that if you are not happy with something or someone, it will always seem to be bad and ugly. It's like looking at a person through tinted glasses - they look yellow because your eyes are seeing them as yellow!

## 152. If the sugarcane is crooked, is its sweetness crooked?  (figurative)

- **Gold:** Even if sugarcane is crooked, its sweetness is not crooked; that is, though appearance isn't good, quality does not spoil.
- **mT0-large** ✓: If the sugarcane is crooked, is its sweetness crooked?
- **Qwen3.5-2B** ✓: If the sugarcane is crooked, is its sweetness crooked?
- **Sarvam-1** ✓: This means that if something isn't perfect or straight, it may still have some good qualities. It doesn't mean you should ignore problems and focus only on what's right; instead, it encourages looking for the positive aspects even when things aren't ideal.

## 153. A biting dog doesn't bark, a barking dog doesn't bite  (figurative)

- **Gold:** Those who make noise do little harm; it is those who stay silent who are truly dangerous.
- **mT0-large** ✓: A biting dog doesn't bark, a barking dog doesn't bite
- **Qwen3.5-2B** ✓: A biting dog doesn't bark, a barking dog doesn't bite
- **Sarvam-1** ✓: This means that if you are not prepared for something bad to happen, then it won't happen. If you don't expect trouble, then there will be no trouble. It is like saying "Don't look before you leap" or "Better safe than sorry

## 154. The morsel that came to the hand is not for the mouth  (figurative)

- **Gold:** This saying expresses the disappointment when what came into one's hand slips away just as it seemed obtained.
- **mT0-large** ✗: The morsel that came to the hand is not for the mouth
- **Qwen3.5-2B** ✓: The morsel that came to the hand is not for the mouth
- **Sarvam-1** ✓: This means that if you take something without thinking about it, then you will regret it later on. It's like saying "don't eat your cake and have it too". You can't do both!

## 155. A salutation in the hand, a club under the arm  (figurative)

- **Gold:** This proverb describes one who shows humility and respect outwardly while holding harmful or deceitful intentions inside.
- **mT0-large** ✗: A salutation in the hand, a club under the arm
- **Qwen3.5-2B** ✓: A salutation in the hand, a club under the arm
- **Sarvam-1** ✓: This means that if you have something good to say about someone or something, then they will be more likely to listen and take your advice seriously. But if you are not happy with them, then they may ignore what you say.

## 156. When there's a stone there's no dog; when there's a dog there's no stone  (figurative)

- **Gold:** This proverb says that when one thing is needed, the other thing needed with it isn't there; it is rare to get both together.
- **mT0-large** ✗: When there's a stone there's no dog; when there's a dog there's no stone
- **Qwen3.5-2B** ✓: The proverb means that when one person is present, the other is absent, and vice versa.
- **Sarvam-1** ✓: This means that if you have something bad, it is better to deal with it than ignore it or pretend it doesn't exist. The proverb uses two examples - stones and dogs - which are both things people often try to avoid dealing with because they can be difficult or unpleasant.

## 157. If camphor is put in the dungheap, does it lose its own smell?  (figurative)

- **Gold:** Even if camphor is put in a garbage heap, it does not lose its fragrance; a good person does not give up his qualities even in a bad environment.
- **mT0-large** ✓: If camphor is put in the dungheap, does it lose its own smell?
- **Qwen3.5-2B** ✓: If camphor is put in the dungheap, does it lose its own smell?
- **Sarvam-1** ✓: The answer to this question is no. Camphor has a strong and distinctive odour that can be detected even when mixed with other substances. Therefore, if camphor is placed in the dungheap, it will not lose its own smell.

## 158. To tell a story there must be those who say 'hum'; to live upright there must be those who say 'chee'  (figurative)

- **Gold:** It may mean that to tell a story you need listeners who say 'hmm', but to live on the right path you need elders who say 'chee' and correct you when you err.
- **mT0-large** ✓: To tell a story there must be those who say 'hum' and to live upright there must be those who say 'chee'
- **Qwen3.5-2B** ✓: The meaning of the proverb is that there must be those who say 'hum' and those who say 'chee'
- **Sarvam-1** ✓: The first part of this saying is about telling stories, and the second part is about living an honest life. Both parts are important for success. If you want people to believe your stories, they need to hear them from someone who has lived by their own rules. And if you want to live an

## 159. No sense at the time of ruin, no medicine at the time of death  (literal)

- **Gold:** When the time of ruin comes, the mind doesn't work; at the time of death, no medicine saves.
- **mT0-large** ✓: The devil is a devil.
- **Qwen3.5-2B** ✗: No sense at the time of ruin, no medicine at the time of death.
- **Sarvam-1** ✓: This means that it is better to do something now than later when you are already sick or injured. It's like saying "don't wait until things get worse before doing anything".

## 160. A forest can be burned by a spark  (figurative)

- **Gold:** Just as one small spark can burn a whole forest, even a small matter can cause great harm or a quarrel.
- **mT0-large** ✗: A forest can be burned by a spark
- **Qwen3.5-2B** ✓: A forest can be burned by a spark
- **Sarvam-1** ✗: This means that even small things can have big effects, and it's important to think about what we are doing before we do something.

## 161. Even the axe's handle is death to its clan  (figurative)

- **Gold:** Just as the handle of an axe comes from the very tree's clan, if one's own people join in betrayal, the whole kin is destroyed.
- **mT0-large** ✗: The axe's handle is death to its clan.
- **Qwen3.5-2B** ✓: The handle of the axe is the part that is used to hold the axe.
- **Sarvam-1** ✓: This means that even if you are doing something wrong, it can still be bad for your family or group. It's like an ax with a sharp edge - just because it doesn't cut right away, it can still hurt someone else.

## 162. The bull buffalo's pain of kosey, the she-buffalo's pain of giving birth  (figurative)

- **Gold:** It can be taken to mean that while one person truly suffers, another shows that he suffers just as much.
- **mT0-large** ✗: The bull buffalo's pain of kosey, the she-buffalo's pain of giving birth
- **Qwen3.5-2B** ✓: The bull buffalo's pain of kosey, the she-buffalo's pain of giving birth
- **Sarvam-1** ✓: This is a Japanese proverb that means "The pain of giving birth to a calf is greater than the pain of having to kill it". It refers to the fact that when you have to give up something valuable (in this case, your own life), it can be more painful than losing something

## 163. The giver is a clown, the taker is Veerabhadra  (figurative)

- **Gold:** It means the lender becomes meek and laughable, while the borrower takes a fierce form.
- **mT0-large** ✗: The giver is a clown, the taker is Veerabhadra
- **Qwen3.5-2B** ✓: The giver is a clown, the taker is Veerabhadra
- **Sarvam-1** ✓: This means that if you give something to someone else, they will take it away from you. It's like giving them your wallet and then they steal it!

## 164. A dog that had seen no order licked the skull  (figurative)

- **Gold:** One who doesn't know proper conduct and etiquette behaves improperly without regard for place and occasion.
- **mT0-large** ✓: A dog that had seen no order licked the skull
- **Qwen3.5-2B** ✓: A dog that had seen no order licked the skull
- **Sarvam-1** ✓: This means a person who has never been taught or trained will do things without thinking about them, and may even be dangerous to others.

## 165. A year for the potter; a minute for the club  (figurative)

- **Gold:** Making a thing takes much time and effort, but a moment is enough to ruin it.
- **mT0-large** ✗: A year for the potter, a minute for the club
- **Qwen3.5-2B** ✓: A year for the potter; a minute for the club
- **Sarvam-1** ✓: This means that it takes time to make something, but once made, it can be used or thrown away quickly. It is like saying "a year for the potter" because you need time and effort to create something, just as with making a pottery piece. And then there's this

## 166. A squint eye is better than a blind eye  (figurative)

- **Gold:** Having something, even incomplete or of lower quality, is better than having nothing.
- **mT0-large** ✓: A squint eye is better than a blind eye
- **Qwen3.5-2B** ✓: A squint eye is better than a blind eye
- **Sarvam-1** ✓: This means that it's better to have some knowledge or experience rather than none at all, even if you don't know everything. It suggests that having an open mind and being willing to learn can be more valuable than not knowing anything at all. </s>

## 167. There's no woman to call 'hey', yet the son's name is Muddu-Ranga  (figurative)

- **Gold:** This proverb mocks those who build big plans for the future when the basics don't yet exist.
- **mT0-large** ✗: There's no woman to call 'hey', but the son's name is Muddu-Ranga
- **Qwen3.5-2B** ✓: There's no woman to call 'hey', yet the son's name is Muddu-Ranga
- **Sarvam-1** ✗: This means that even though you don't have a wife, your child has a good name. It also implies that having a good reputation can be more important than material possessions or wealth. </s>

## 168. Know the world, learn accounts  (literal)

- **Gold:** To get ahead in life one must understand the ways of people and the world and learn to account for money.
- **mT0-large** ✓: Learn the world, learn accounts
- **Qwen3.5-2B** ✓: The proverb means that one must understand the broader context of the world while simultaneously mastering the specific details of financial records.
- **Sarvam-1** ✓: This means that if you know how to do something well and have a good understanding of what is going on around you, then you will be able to get better at it. It's like knowing your way around town so you can find your way back home more easily.

## 169. Give a bribe and climb the cot, cheat and climb Kailasa  (figurative)

- **Gold:** A sarcastic saying about people who gain comfort or position by bribery and rise through cheating.
- **mT0-large** ✗: A man climbs a cot and a woman climbs a ladder.
- **Qwen3.5-2B** ✓: The meaning of the proverb is that if you give a bribe to climb the cot, you will cheat and climb Kailasa.
- **Sarvam-1** ✓: This is an English saying that means to give someone money or something valuable in order to get what you want. It's like trying to climb up on top of a ladder by offering someone else a piece of rope (or "cot") to hold onto while they do it for

## 170. Business without profit is like a donkey scratching its body  (figurative)

- **Gold:** In a business that brings no profit, however much one works, it is like a donkey scratching its body: only the effort remains, with no fruit.
- **mT0-large** ✗: Business without profit is like a donkey scratching its body
- **Qwen3.5-2B** ✓: Business without profit is like a donkey scratching its body
- **Sarvam-1** ✓: This means that if you are doing something just for your own benefit, it's not really worthwhile. It's like trying to scratch yourself with a donkey - it won't work! You need to be motivated by more than just personal gain. [/INST]

## 171. Even if it's greens sambar, eat a counted ragi ball  (figurative)

- **Gold:** Even if the meal is a simple greens sambar, one should eat a counted ragi ball without exceeding the measure; keep account and limit even in small matters.
- **mT0-large** ✓: Even if it's greens sambar, eat a counted ragi ball
- **Qwen3.5-2B** ✓: The meaning of the proverb is that even if it's a small or insignificant thing, it's still important to take care of it.
- **Sarvam-1** ✓: This means that even if something is not very good or tasty, you should still try to enjoy it because there are other things out there that might be better. It also suggests that trying new foods can be fun and rewarding.

## 172. After the lingam is torn, what obligation is there to the Jangama?  (figurative)

- **Gold:** Once a bond is severed, the obligation or restriction tied to that bond no longer exists.
- **mT0-large** ✓: a servant
- **Qwen3.5-2B** ✓: The Jangama is a type of boat.
- **Sarvam-1** ✓: The lingam represents the male organ and the jangama refers to a Hindu god who has no physical form but can be seen as an embodiment of the divine power within all living things. When the lingam is torn, it means that the divine energy or life force (j

## 173. A club blow for the fool, a word blow for the wise  (figurative)

- **Gold:** One without understanding learns after being beaten; one word is enough for the wise.
- **mT0-large** ✓: A club blows for the fool, a word blows for the wise
- **Qwen3.5-2B** ✓: A club blow for the fool, a word blow for the wise
- **Sarvam-1** ✗: This means that if you are being treated badly by someone who is not very smart or clever, then it's better to be angry with them than to get mad at them because they might actually be trying to help you out! It's like when you have a cold and your

## 174. A calamity (Mari) at home, a benefactor to the town  (figurative)

- **Gold:** This proverb describes a person who troubles his family but appears good only to outsiders in town.
- **mT0-large** ✗: A good man is a good friend to the town.
- **Qwen3.5-2B** ✓: A calamity (Mari) at home, a benefactor to the town
- **Sarvam-1** ✓: This means that when something bad happens at home it can be good for your community or city. It is like saying "a problem at home is a blessing in disguise".

## 175. The one who comes falling on you is last among the three 'kaami'  (figurative)

- **Gold:** It may mean that those who impose themselves uninvited are valued less.
- **mT0-large** ✗: The one who comes falling on you is last among the three 'kaami'
- **Qwen3.5-2B** ✓: The one who comes falling on you is last among the three 'kaami'
- **Sarvam-1** ✓: This means that if someone has a bad intention, they will try to get what they want by any means possible and it doesn't matter how many times they fail or succeed. They are not afraid to do anything wrong because they think they can get away with it.

## 176. One who has given up the three is big in the town  (figurative)

- **Gold:** One who gives up concerns of shame, honor and dishonor gets ahead in the world quickly and influences everyone.
- **mT0-large** ✗: One who has given up the three is big in the town
- **Qwen3.5-2B** ✗: One who has given up the three is big in the town
- **Sarvam-1** ✗: This means that if you have lost your way, it's better to give up and move on than to keep trying to find a solution when there isn't any. It's like giving up on something because you can't do it or don't want to try harder - this

## 177. Does wrong, but has a Brindavan in front of the house  (figurative)

- **Gold:** This proverb criticizes a hypocrite who keeps bad conduct within but shows himself as pious outside.
- **mT0-large** ✗: He does not do anything wrong, but has a Brindavan in front of his house.
- **Qwen3.5-2B** ✓: The Brindavan is a type of house in India.
- **Sarvam-1** ✗: This means that even if you do something bad or wrong, there is always some good thing coming out of it. It's like having a "Brindavan" (a place where Lord Krishna was born) right outside your doorstep. Even though you might be facing

## 178. One who knows speech has no quarrel; one who knows eating has no disease  (literal)

- **Gold:** One who knows when and how to speak doesn't get into quarrels; one who knows what to eat and how much doesn't get disease.
- **mT0-large** ✓: One who knows speech has no quarrel; one who knows eating has no disease
- **Qwen3.5-2B** ✓: One who knows how to speak and eat has no quarrel or disease.
- **Sarvam-1** ✓: This means that if you know how to speak, there is nothing wrong with you and if you know how to eat, there is nothing wrong with you. It's a saying about people who are healthy and happy because they have good health and knowledge.

## 179. Speech ruined the house, the hole ruined the stove  (figurative)

- **Gold:** Thoughtless speech breaks the family itself; as a stove with a hole is ruined for cooking, even a small defect brings great harm.
- **mT0-large** ✓: The hole in the stove ruined the speech.
- **Qwen3.5-2B** ✓: The house was ruined by the hole, the stove was ruined by the speech.
- **Sarvam-1** ✓: This means that if you speak badly about someone or something, it can cause problems for them and their reputation. It's like damaging a part of your home by speaking poorly about it. If you damage something important to someone else, they might not be able to fix it easily. Similarly,

## 180. Perform a wedding and see, build a house and see  (literal)

- **Gold:** How hard conducting a wedding and building a house are is known only to those who have done them.
- **mT0-large** ✗: A man does a wedding and see a house.
- **Qwen3.5-2B** ✓: Perform a wedding and see, build a house and see
- **Sarvam-1** ✗: This means that you should try to do something before you know whether it will work or not. It is better to be safe than sorry.

## 181. When told 'Gunda is getting married', he said 'you yourself are my wife'  (figurative)

- **Gold:** It seems this proverb refers to one who gives a funny or irrelevant reply unrelated to what was said.
- **mT0-large** ✗: When told 'Gunda is getting married', he said 'you yourself are my wife'
- **Qwen3.5-2B** ✓: When told 'Gunda is getting married', he said 'you yourself are my wife'
- **Sarvam-1** ✓: This means that when someone says something, it can be taken as a fact or an opinion. In this case, the person saying "Gunda is getting married" might not actually know if Gunda is getting married or not, but they believe what they just heard and assume it to be

## 182. Smitten on seeing the face, moved away on seeing the character  (figurative)

- **Gold:** One who is charmed by outward beauty and goes near becomes disappointed after learning the inner qualities and drifts away.
- **mT0-large** ✓: Smitten on seeing the face, moved away on seeing the character
- **Qwen3.5-2B** ✓: The meaning of the proverb is that the first impression is important.
- **Sarvam-1** ✓: This means that when you see someone's face and are attracted to them, but then they don't have the same qualities as what you expected or hoped for, it can be disappointing. It is like being smitten by their looks, only to find out later that there

## 183. They dug a well when the house caught fire  (figurative)

- **Gold:** Starting to prepare for a danger after it has come is a late and futile effort.
- **mT0-large** ✗: They dug a well when the house caught fire
- **Qwen3.5-2B** ✓: They dug a well when the house caught fire
- **Sarvam-1** ✓: This means that you should do something before it is too late, or else you will be sorry later on. It's like saying "Don't wait until it's too late to fix things".

## 184. Remove a thorn with a thorn, remove enmity with enmity  (figurative)

- **Gold:** One enemy or trouble should be removed by another enemy or a similar means.
- **mT0-large** ✓: Remove a thorn with a thorn, remove enmity with enmity
- **Qwen3.5-2B** ✓: Remove a thorn with a thorn, remove enmity with enmity.
- **Sarvam-1** ✓: This means that you should deal with your problems by dealing with them directly and not letting other people's actions affect you. If someone is trying to hurt or harm you, it may be best to respond in kind so as not to get caught up in their negativity. However, this

## 185. Pregnant out of deference, with no place to give birth  (figurative)

- **Gold:** It can be interpreted that if one agrees to everything out of deference, one is finally stuck with no way out.
- **mT0-large** ✓: Pregnant out of deference, with no place to give birth
- **Qwen3.5-2B** ✓: The meaning of the proverb is that a person who is pregnant is not allowed to give birth.
- **Sarvam-1** ✗: This means that someone is being treated very nicely but they are not getting what they want or need from it. They are pregnant without a safe and comfortable place to have their baby.

## 186. A pearl once broken is gone, a word once spoken is gone  (figurative)

- **Gold:** A broken pearl cannot be joined again; likewise a word once spoken cannot be taken back.
- **mT0-large** ✓: A pearl once broken is gone, a word once spoken is gone
- **Qwen3.5-2B** ✓: A pearl once broken is gone, a word once spoken is gone
- **Sarvam-1** ✓: This means that if you lose something valuable or precious, it will be lost forever. If you say something important and then regret it later, there's no way to get it back. It's like losing a pearl - once it breaks, it can never be fixed again.

## 187. The monkey's rule is on the tree branch  (figurative)

- **Gold:** A petty person's authority works only within his small sphere, and like the monkey's court at the top of a tree, it has no security.
- **mT0-large** ✓: The monkey's rule is on the tree branch
- **Qwen3.5-2B** ✗: The monkey's rule is on the tree branch
- **Sarvam-1** ✗: This means that if you are not careful, your plans will fail because you were too careless or lazy to do something important. It can also mean that someone who does not work hard enough may end up being taken advantage of by others.

## 188. The talkative Brahma is like a pot with holes  (figurative)

- **Gold:** A very talkative person, like a pot with holes, cannot hold anything, not even a secret.
- **mT0-large** ✓: The talkative Brahma is like a pot with holes
- **Qwen3.5-2B** ✓: The talkative Brahma is like a pot with holes
- **Sarvam-1** ✓: This means that if you are always talking, people will eventually stop listening to what you have to say. It's better to be quiet and listen than to keep talking all the time.

## 189. Our own eye ruined it for us  (figurative)

- **Gold:** It may mean that harm came through our own choice or through our own people.
- **mT0-large** ✓: Our own eye ruined it for us
- **Qwen3.5-2B** ✓: Our own eye ruined it for us
- **Sarvam-1** ✓: This means that if we make a mistake or do something wrong, then our actions can cause others to suffer as well. It's important to think about how our choices affect those around us before making them.

## 190. Speech ancient, conduct that of a Kirata  (figurative)

- **Gold:** Speech sounds like a virtuous person narrating the Puranas, but conduct is rough and bad like a Kirata (hunter-tribesman); saying one thing and doing another.
- **mT0-large** ✗: The ancient speech is conducted as a Kirata.
- **Qwen3.5-2B** ✓: The Kirata is a Japanese term for a person who is a member of the Kirata community, which is a group of people who are known for their unique and distinctive style of living. The Kirata community is known for their unique and distinctive style of living.
- **Sarvam-1** ✓: This means that if you are not careful with your words and actions, then people will think you are old-fashioned or outdated. It is like saying "speak softly and carry a big stick". The idea behind this proverb is to be mindful of how we communicate

## 191. What is rain, what is cold, to one who has fallen into the water?  (figurative)

- **Gold:** To one already immersed in great trouble, the small troubles that come along with it don't matter much.
- **mT0-large** ✗: The rain is cold, to one who has fallen into the water.
- **Qwen3.5-2B** ✓: The proverb means that for someone who has already suffered a great loss or been deeply hurt, the pain of new hardships is often too great to bear.
- **Sarvam-1** ✓: This means that if you are not careful when doing something, it can lead to a bad outcome. The proverb uses an analogy with water and ice to explain this idea. If someone falls into water without being prepared or cautious, they will likely end up getting wet and cold. Similarly

## 192. Even fallen underneath, the nose is up  (figurative)

- **Gold:** A saying about one who, even after losing or falling by mistake, doesn't admit defeat and shows arrogance and rough stubbornness.
- **mT0-large** ✗: Even fallen underneath, the nose is up
- **Qwen3.5-2B** ✓: The nose is up, even when the head is down.
- **Sarvam-1** ✗: This means that even if you are not successful or have failed at something, there is always a chance for improvement and success to come your way. It's like when someone falls down but then gets back up again - they still have an opportunity to succeed!

## 193. A dog's tail is always crooked  (figurative)

- **Gold:** No matter how much one tries to correct a person of bad nature, his nature does not change.
- **mT0-large** ✗: A dog's tail is always crooked
- **Qwen3.5-2B** ✓: The tail is always crooked because the dog is always walking on the ground.
- **Sarvam-1** ✓: This means that a person or thing will never be perfect, and they are likely to have flaws or problems. The phrase comes from an old saying about dogs, which was used as a way to describe someone who was not very good at something. It has been adapted over time to apply to people

## 194. If a dog barks, is heaven ruined?  (figurative)

- **Gold:** No harm comes to the great, or to a good work, just because petty-minded people criticize.
- **mT0-large** ✗: A dog barks, is heaven ruined?
- **Qwen3.5-2B** ✓: If a dog barks, is heaven ruined?
- **Sarvam-1** ✓: This means that if something bad happens, it doesn't mean everything else will be ruined too. It just means there might be some problems.

## 195. Learning conduct is an uphill rock, losing conduct is a slide  (figurative)

- **Gold:** Learning good conduct takes as much effort as climbing a hill, but bad conduct comes very easily, like a slide.
- **mT0-large** ✓: Learning conduct is an uphill rock, losing conduct is a slide
- **Qwen3.5-2B** ✓: Learning conduct is an uphill rock, losing conduct is a slide
- **Sarvam-1** ✓: This means that learning good behavior or habits can be difficult and hard to do but once you have learned them they are easier to keep than if you had not learned them. It's like climbing a mountain - it takes effort and energy to get there, but once you reach the top you don

## 196. The dog has no work, no time to stand  (figurative)

- **Gold:** A saying about those who, though they have no real work, run around always acting busy.
- **mT0-large** ✓: The dog has no work, no time to stand
- **Qwen3.5-2B** ✗: The dog has no work, no time to stand
- **Sarvam-1** ✗: This means that if you don't have anything to do or nothing to think about, then you will be bored and unhappy. It is a warning against idleness. [/INST]

## 197. One who becomes courteous will become victorious  (literal)

- **Gold:** One who behaves with humility and courtesy achieves victory in life.
- **mT0-large** ✓: One who becomes courteous will become victorious
- **Qwen3.5-2B** ✓: One who becomes courteous will become victorious
- **Sarvam-1** ✓: This means that being polite and respectful can help you achieve your goals or win over others. It's like saying, "If you want to succeed, be kind."

## 198. Invite all the relatives, but don't put your hand into the kantale bag  (figurative)

- **Gold:** It seems to be a proverb meaning that you may invite all the relatives, but shouldn't dip excessively into the money bag in the name of celebration.
- **mT0-large** ✓: Invite all the relatives, but don't put your hand into the kantale bag
- **Qwen3.5-2B** ✓: Invite all the relatives, but don't put your hand into the kantale bag
- **Sarvam-1** ✓: This means that you should not invite everyone to a party or event because it will be too much work for you and also might cause problems with other people. It is better to choose who you want to come based on their importance to you rather than just inviting anyone.

## 199. Speaking the truth brings resentment  (literal)

- **Gold:** If you state the truth directly, the listener gets angry and the relationship may be spoiled.
- **mT0-large** ✓: Speaking the truth brings resentment
- **Qwen3.5-2B** ✓: The truth is often misunderstood by those who are not prepared to listen to it.
- **Sarvam-1** ✓: This means that telling someone something they don't want to hear can make them angry or upset with you. It is better not to speak badly about people, even if it might be true.

## 200. No prosperity for those without honesty  (literal)

- **Gold:** Those without honesty get no growth or profit.
- **mT0-large** ✓: Without honesty, no prosperity.
- **Qwen3.5-2B** ✓: No prosperity for those without honesty
- **Sarvam-1** ✓: This means that if you don't have good character and integrity, then your success will be limited. It is a warning to not put all your eggs in one basket (or investment) and always keep some backup plans just in case things go wrong.

## 201. Pickle that isn't there at mealtime is equal to dirt  (figurative)

- **Gold:** Help or a thing not available at the time of need has no value even if it arrives later.
- **mT0-large** ✗: Pickle that isn't there at mealtime is equal to dirt
- **Qwen3.5-2B** ✓: The meaning of the proverb is that if you don't have a pickle at the time of eating, it is as if you have dirt on your plate.
- **Sarvam-1** ✓: This means that if you don't use something, it will become worthless or unimportant. It can also be used as a warning about wasting time and resources on things that aren't useful. </s>

## 202. Lime for one eye, butter for the other eye  (figurative)

- **Gold:** This proverb describes partial behavior, treating two people differently: favor for one, harshness for the other.
- **mT0-large** ✗: A few drops of lime and butter are served in a cup of tea.
- **Qwen3.5-2B** ✓: The proverb means that one should be cautious and careful with one's eyes, as they can be easily deceived by the world.
- **Sarvam-1** ✓: This means that if you do something to one person it will affect them and also someone else. It is a way of saying that people are interconnected with each other.

## 203. If you fall into a well in one fit of anger, you can't get up even in seven fits of anger  (figurative)

- **Gold:** It seems to be a proverb meaning that an act done thoughtlessly in a burst of anger harms oneself.
- **mT0-large** ✗: If you fall into a well in one fit of anger, you can't get up even in seven fits of anger
- **Qwen3.5-2B** ✓: The proverb means that if you fall into a well in one fit of anger, you can't get up even in seven fits of anger.
- **Sarvam-1** ✓: This means that if you are angry and act on it without thinking about what will happen next, then you won't be able to control your actions when things go wrong later. It is like falling down a well - once you're there, getting out isn't easy!

## 204. Fire eats the dry tree, worry eats the green tree  (figurative)

- **Gold:** Just as fire eats a dry tree, worry melts a living, green person from within.
- **mT0-large** ✓: Fire eats the dry tree, worry eats the green tree
- **Qwen3.5-2B** ✓: The fire eats the dry tree, worry eats the green tree
- **Sarvam-1** ✓: This means that when you are worried about something, it will make things worse for you and not help them get better. It is like a fire burning up a dry tree; if there was no water to put out the fire, then the tree would be destroyed. Similarly, worrying about problems

## 205. What comes to one's lot is panchamrita  (figurative)

- **Gold:** Whatever comes to one's share, one should accept contentedly, like panchamrita (a sweet sacred offering).
- **mT0-large** ✗: A lot of bread is a pancake
- **Qwen3.5-2B** ✓: What comes to one's lot is panchamrita
- **Sarvam-1** ✓: This means that whatever happens to you, it is a blessing or a curse. It can be good or bad. You cannot change what has happened. The only thing you can do is how you react to it. If you are happy with your lot, then you have been lucky.

## 206. What does it matter what happens to what isn't in one's share?  (figurative)

- **Gold:** It seems to be a proverb meaning: whatever happens to something that isn't part of my share, I have no worry about it.
- **mT0-large** ✓: What does it matter what happens to what is not in one's share?
- **Qwen3.5-2B** ✓: What does it matter what happens to what isn't in one's share?
- **Sarvam-1** ✓: This means that if something is not important or doesn't affect you, then don't worry about it. It's like saying "don't sweat the small stuff".

## 207. Say 'poor thing' and karma comes  (figurative)

- **Gold:** It seems to be a proverb meaning that if you step into others' trouble out of pity, their trouble falls on your own shoulders.
- **mT0-large** ✓: Say 'poor thing' and karma comes
- **Qwen3.5-2B** ✓: The meaning of the proverb is that when you say 'poor thing' to someone, karma comes.
- **Sarvam-1** ✓: This means that if you say something bad about someone, they will probably get back at you somehow. It is a way to warn people not to be too mean or critical towards others.

## 208. Bought a curse so that sin wouldn't come  (figurative)

- **Gold:** It seems to mean that in trying to avoid sin, one paid a price and brought another trouble upon oneself.
- **mT0-large** ✓: A curse is a curse that does not come.
- **Qwen3.5-2B** ✓: The meaning of the proverb is that the person who bought a curse so that sin wouldn't come is a person who is trying to avoid sin by buying a curse.
- **Sarvam-1** ✓: This means that if you buy something bad, then it will be used against you. It is like buying a curse to protect yourself from sinning.

## 209. Mocked others and got called a monkey  (figurative)

- **Gold:** One who ridicules others finally becomes the target of ridicule himself.
- **mT0-large** ✓: A monkey called a monkey.
- **Qwen3.5-2B** ✓: Mocked others and got called a monkey
- **Sarvam-1** ✓: This means that if you mock or make fun of someone else, then they will eventually call you a fool for it. It is like being made fun of yourself.

## 210. When youth came, the measure was lost  (figurative)

- **Gold:** This proverb says that by the time youth arrives, self-control and discretion are lost.
- **mT0-large** ✓: When youth came, the measure was lost
- **Qwen3.5-2B** ✓: When youth came, the measure was lost
- **Sarvam-1** ✓: This means that when you are young and full of energy and enthusiasm, it is easy to make mistakes or take risks because you don't think about the consequences. As you get older, your experience and wisdom help you to be more careful and thoughtful.

## 211. Everything the virtuous one touches is gold  (figurative)

- **Gold:** Whatever a fortunate person does brings success and profit.
- **mT0-large** ✓: All the virtuous one touches is gold
- **Qwen3.5-2B** ✓: Everything the virtuous one touches is gold.
- **Sarvam-1** ✓: This means that if you are good and do good things, then people will be happy to help you out. They will give you what they can because they know you have done something good for them. It's like when someone does a kind thing for another person, it makes both of them feel

## 212. Though Putya's sorghum is finished, Hotya's song isn't finished  (figurative)

- **Gold:** It seems to be a proverb meaning that even when wealth runs out, desires and demands don't end.
- **mT0-large** ✓: Putya's sorghum is finished, Hotya's song isn't finished
- **Qwen3.5-2B** ✓: Though Putya's sorghum is finished, Hotya's song isn't finished.
- **Sarvam-1** ✓: This means that even if something has been completed or done, there may still be more to do. It can also mean that you shouldn't give up on a task once it seems like it's over.

## 213. The free husband ate to his belly's fill, the house husband fell down groaning  (figurative)

- **Gold:** It seems to mean that when an outsider gets a lavish free treat, the member of the house is neglected.
- **mT0-large** ✗: The free husband ate to his belly's fill, the house husband fell down groaning
- **Qwen3.5-2B** ✓: The free husband ate to his belly's fill, the house husband fell down groaning
- **Sarvam-1** ✓: This means that if you are not careful with your money and spend it all on yourself, then when you need help or support from others, they will be there for you less than they would have been otherwise. It also implies that being selfish can lead to financial ruin.

## 214. The civet cat, not knowing its own scent, is said to wander the whole forest and die  (figurative)

- **Gold:** This proverb is about those who, not knowing the quality or ability within themselves, wander outside looking for it.
- **mT0-large** ✓: The civet cat, not knowing its own scent, is said to wander the whole forest and die
- **Qwen3.5-2B** ✗: The civet cat, not knowing its own scent, is said to wander the whole forest and die
- **Sarvam-1** ✓: This means that if you don't know what your weaknesses are, then you will be easily caught by them. It also implies that it is better to have a good sense of self-awareness than to rely on luck or chance.

## 215. If you tell a Purana, will flowers fall?  (figurative)

- **Gold:** No fruit comes from mere talk, preaching or speeches; action is needed.
- **mT0-large** ✓: If you tell a Purana, will flowers fall?
- **Qwen3.5-2B** ✓: If you tell a Purana, will flowers fall?
- **Sarvam-1** ✓: This is an example of a Proverb that means if you try to do something difficult or impossible, it won't work out well for you. It can also be used as a warning against trying to impress others with your knowledge and skills when they are not really needed. The phrase comes from

## 216. Will the brinjal in the book come to the curry?  (figurative)

- **Gold:** Knowledge read in a book is not useful in real life without hands-on experience.
- **mT0-large** ✗: The brinjal in the book will come to the curry.
- **Qwen3.5-2B** ✓: The brinjal in the book will never come to the curry.
- **Sarvam-1** ✓: The proverb is a way of saying that something will not happen or be successful if it cannot get what it needs. It's like asking, "Will the brinjal in the book come to the curry?" If you don't have the right ingredients for your dish,

## 217. Though he doesn't know the manner, he knows the talk  (figurative)

- **Gold:** It seems to be about one who, though not knowing the right way of conduct, is ahead in giving advice to others.
- **mT0-large** ✗: He knows the manner, but he knows the talk.
- **Qwen3.5-2B** ✓: The speaker is saying that the speaker is not familiar with the specific details of the situation, but he is familiar with the general conversation or topic.
- **Sarvam-1** ✓: This means that even if someone is not aware of how they are being treated or spoken to, they will still be able to tell what kind of person they are dealing with. It suggests that people can often tell a lot about others based on their behavior and actions, rather than just by looking at them

## 218. Talk without propriety is a headache  (figurative)

- **Gold:** Speech without context or courtesy irritates the listener like a headache.
- **mT0-large** ✓: Talking without propriety is a headache
- **Qwen3.5-2B** ✓: Talk without propriety is a headache
- **Sarvam-1** ✓: This means that if you talk to someone about something important, but do it in an unprofessional way, then you will have problems with them. It's like having a headache because you are talking about something serious and not doing it properly.

## 219. There is medicine for disease, there is no medicine for character  (literal)

- **Gold:** There is medicine for illness, but no medicine for a flaw of bad conduct or character.
- **mT0-large** ✗: There is no medicine for disease, there is no medicine for character
- **Qwen3.5-2B** ✓: The meaning of the proverb is that there is no cure for bad character.
- **Sarvam-1** ✓: This means that you can't cure someone with a pill or treatment if they have bad character. You need to change their behaviour and attitude first before you can help them.

## 220. Those smitten by beauty have no fear of sin  (literal)

- **Gold:** Those infatuated by beauty are not afraid of doing wrong.
- **mT0-large** ✓: They are smitten by beauty.
- **Qwen3.5-2B** ✓: The meaning of the proverb is that those who are attracted to beauty are not afraid of sin.
- **Sarvam-1** ✓: This means that people who are attracted to beautiful things will not be afraid of doing something wrong because they think it is just a small mistake. They might do something bad, but they won't feel guilty about it.

## 221. Royal pomp is the mark of a pauper  (figurative)

- **Gold:** A saying about one who shows grandeur like a king outside but has beggar-like poverty within.
- **mT0-large** ✓: The royal pomp is the mark of a pauper
- **Qwen3.5-2B** ✓: The meaning of the proverb is that a person who is poor is often mistaken for a rich person.
- **Sarvam-1** ✓: This means that if you want to be important, you have to act like someone who is important. If you are not rich or powerful, then it's better to pretend to be so. It's easier than trying to become something you can never achieve.

## 222. As long as the king lives, the queen enjoys  (literal)

- **Gold:** The wife gets comforts and luxuries only as long as the husband lives and earns to support her.
- **mT0-large** ✓: As long as the king lives, the queen enjoys
- **Qwen3.5-2B** ✓: The king and queen are the two most important people in the kingdom.
- **Sarvam-1** ✗: This means that if someone is important and powerful, they will be protected by those who are also important and powerful. The phrase comes from a time when kings had queens to protect them. If the king was killed or injured, his wife would have no protection and could easily become an easy target for

## 223. If the gem is good, it grows in the very place it is  (figurative)

- **Gold:** Those who have real talent or worth shine wherever they are.
- **mT0-large** ✗: If the gem is good, it grows in the very place it is
- **Qwen3.5-2B** ✓: The gem is good, it grows in the very place it is.
- **Sarvam-1** ✓: This means that if something has a lot of value or quality, then it will grow and improve over time. It's like how diamonds are formed deep underground and they become more valuable as they get older.

## 224. The bird that eats gems fell in with the crow and became a guest at the leftover leaf  (figurative)

- **Gold:** Even those of good qualities, if they fall in bad company, lose their value and respect.
- **mT0-large** ✗: The bird that eats gems fell in with the crow and became a guest at the leftover leaf
- **Qwen3.5-2B** ✓: The bird that eats gems fell in with the crow and became a guest at the leftover leaf
- **Sarvam-1** ✓: This means that if you try to do something difficult or risky, it will probably fail because there are other people who can help you succeed instead. It's like trying to eat all your own food when you have friends around - they might be able to give you some extra help!

## 225. The winner lost, the loser died  (figurative)

- **Gold:** Even the one who wins a quarrel or lawsuit suffers great loss and is as good as defeated; the loser is ruined even more.
- **mT0-large** ✓: The winner lost, the loser died
- **Qwen3.5-2B** ✓: The winner lost, the loser died
- **Sarvam-1** ✓: This means that if you lose something or someone important to you, it can be very painful and difficult for you. It is a way of saying that losing something valuable can cause great emotional pain.

## 226. When told 'say something auspicious, Soma', he said 'an owl is visible, uncle'  (figurative)

- **Gold:** This proverb is about an ill-omened person who speaks words of bad portent even when asked to say something good.
- **mT0-large** ✗: When told 'say something auspicious, Soma', he said 'an owl is visible, uncle'
- **Qwen3.5-2B** ✓: The owl is a symbol of wisdom and knowledge.
- **Sarvam-1** ✗: This means that when someone says good things about you, it can be taken as an omen or sign that your words are true and will come to pass. It suggests that if someone praises you, there may be some truth behind their words. </s>

## 227. The ascetic's wife is neither a widow nor a married woman  (figurative)

- **Gold:** The ascetic's wife is neither widow nor a woman whose husband lives; it points to a limbo state of being neither.
- **mT0-large** ✓: The ascetic's wife is neither a widow nor a married woman
- **Qwen3.5-2B** ✓: The ascetic's wife is neither a widow nor a married woman
- **Sarvam-1** ✓: This means that an ascetic (a person who lives a very simple life) does not have to worry about being either a widow or a married woman because they are already free from those things. They can focus on their spiritual growth instead. [/INST]

## 228. Worldly life is a river of the ocean; to one who can swim, it's chest-deep  (literal)

- **Gold:** Even the ocean of worldly life is only chest-deep water to one who knows swimming; to the skillful, family troubles are easy.
- **mT0-large** ✓: Worldly life is a river of the ocean; to one who can swim, it's chest-deep
- **Qwen3.5-2B** ✓: The meaning of the proverb is that the world is vast and complex, and it is difficult to navigate without guidance.
- **Sarvam-1** ✓: This means that worldly things are like water flowing downstream - they come and go quickly but don't last long. If you try to hold onto them too tightly, you will lose your sense of what really matters. The proverb suggests that we should focus on our spiritual wellbeing rather

## 229. Keep family matters secret, disease matters out  (literal)

- **Gold:** Internal household matters should be kept secret, but illness should not be hidden; it must be disclosed and treated.
- **mT0-large** ✓: Keep family matters secret, disease matters out
- **Qwen3.5-2B** ✓: Keep family matters secret, disease matters out
- **Sarvam-1** ✓: This means that you should keep your personal problems and secrets to yourself because they can affect other people's lives negatively. It is better not to share them with others so as not to cause any harm or trouble. </s>

## 230. Worldly life is an ocean; one must swim, stay, and win  (figurative)

- **Gold:** Worldly life is an ocean; one must swim in it, stay there, face the troubles and win.
- **mT0-large** ✓: The world is an ocean.
- **Qwen3.5-2B** ✓: The meaning of the proverb is that one must be prepared for the challenges of life, stay focused on the present, and strive for success.
- **Sarvam-1** ✓: This means that worldly things are like a big ocean to be swam through. You can't just sit on top of it or ignore it. You have to go through it and make use of what you find there.

## 231. Associating with a householder spoiled the ascetic  (figurative)

- **Gold:** By associating with worldly people, even one who was self-controlled goes astray.
- **mT0-large** ✓: A householder shared a healthy relationship with a sick ascetic.
- **Qwen3.5-2B** ✓: Associating with a householder spoiled the ascetic
- **Sarvam-1** ✓: This means that if you associate yourself with someone who is not good, it will affect your own character and morals. It's like trying to eat poisonous food - even though you might be able to get away with eating small amounts at first, eventually it will harm you. In this case

## 232. Asked what worries an ascetic: the only worry is food  (figurative)

- **Gold:** This saying says that however detached one is, everyone has the worry of food.
- **mT0-large** ✗: The only worry of an ascetic is food.
- **Qwen3.5-2B** ✓: The only worry is food
- **Sarvam-1** ✗: An ascetic is someone who lives a very simple life, without many material possessions or pleasures. They are often focused on spirituality and self-discipline rather than worldly things like wealth or fame. The proverb means that even though there may be other concerns or worries

## 233. The ways of those touched by wealth are different  (figurative)

- **Gold:** The behavior and attitude of those who have come into wealth change; they are not as before.
- **mT0-large** ✗: The ways of those touched by wealth are different
- **Qwen3.5-2B** ✓: The ways of those touched by wealth are different
- **Sarvam-1** ✗: This means that people who have money or power will behave differently than others, and they may not always act honestly or fairly.

## 234. Home stay for the daughter-in-law, exile for the mother-in-law  (figurative)

- **Gold:** Household authority passes to the daughter-in-law and the mother-in-law, once mistress of the house, becomes like a stranger in her own home.
- **mT0-large** ✓: The daughter-in-law stays at home, exile for the mother-in-law.
- **Qwen3.5-2B** ✓: The daughter-in-law is welcome, but the mother-in-law is not.
- **Sarvam-1** ✓: This is a Chinese saying that means "a home stay for your daughter-in-law and an exile for your mother-in-law". It's used to describe situations where someone has been forced to leave their hometown or country because they have married into another family. The phrase

## 235. Independence went, dependence came  (literal)

- **Gold:** This indicates a state of losing freedom and coming under another's control.
- **mT0-large** ✓: Independence went, dependence came
- **Qwen3.5-2B** ✓: Independence went, dependence came
- **Sarvam-1** ✓: This means that when you are independent and do things on your own, then you will be able to rely on yourself for support later on. If you don't have this independence, then you may find it difficult to get help or assistance from others.

## 236. A woman's form is the form, adornment is the rasa  (figurative)

- **Gold:** A saying admiringly claiming that a woman's beauty is the finest beauty and adornment is its essence (rasa).
- **mT0-large** ✗: A woman's form is the form, adornment is the rasa
- **Qwen3.5-2B** ✓: A woman's form is the form, adornment is the rasa
- **Sarvam-1** ✗: This means that a person's appearance and behavior are more important than their clothes or accessories. The proverb suggests that people should focus on being themselves rather than trying to impress others with fancy clothing or jewelry. It emphasizes the importance of inner beauty and character over external appear

## 237. Sorrow after joy, joy after sorrow  (literal)

- **Gold:** In life, sorrow follows joy and joy follows sorrow, again and again.
- **mT0-large** ✓: Joy after sorrow.
- **Qwen3.5-2B** ✓: Sorrow after joy, joy after sorrow, is a saying that describes the natural cycle of human emotions, where happiness is often followed by sadness and vice versa.
- **Sarvam-1** ✓: This means that when you are sad or upset about something bad happening to you, it will make your happiness even more special and wonderful. It's like adding a little bit of salt to your happiness!

## 238. Even if you lie, say it as if hitting the crown of the truth  (figurative)

- **Gold:** Even if one must lie, it should be said so firmly, outdoing the truth itself, that everyone believes it.
- **mT0-large** ✗: Even if you lie, say it as if hitting the crown of truth
- **Qwen3.5-2B** ✓: The meaning of the proverb is that even if you lie, say it as if hitting the crown of the truth.
- **Sarvam-1** ✓: This means that even when we are lying or trying to deceive someone, we should still speak honestly and directly about what is true. It's like saying "even if I don't have a crown on my head, I will still wear it."

## 239. A false god, a thieving priest  (figurative)

- **Gold:** A fraudulent institution fittingly has a fraudster as its head; both are fake.
- **mT0-large** ✓: A false god, a thieving priest
- **Qwen3.5-2B** ✓: A false god, a thieving priest
- **Sarvam-1** ✓: This is an example of a proverb that means someone who pretends to be something they are not or has no real value. The phrase "false god" refers to a person who claims to have power and authority but does not actually possess it. The term "thieving priest" suggests that this

## 240. I've become pregnant, once in a blue moon; don't move, husband  (figurative)

- **Gold:** Using a rare opportunity as an excuse to expect everyone to pamper one and assign no work.
- **mT0-large** ✗: Once in a blue moon, I've become pregnant. Don't move, husband
- **Qwen3.5-2B** ✓: The husband should not move because the wife is pregnant.
- **Sarvam-1** ✗: This means that it is very rare to have something happen more than once or twice. It can also be used when someone has done something wrong and they are trying not to get caught again. The phrase "once in a blue moon" refers to an event that happens rarely. In this case,

## 241. Even if you miss your own dharma, don't commit adharma  (literal)

- **Gold:** Even if one cannot fully follow one's duty, one should not do a wrong or unethical act.
- **mT0-large** ✓: Even if you miss your own dharma, don't commit adharma
- **Qwen3.5-2B** ✓: The meaning of the proverb is that even if you miss your own dharma, don't commit adharma.
- **Sarvam-1** ✓: This means that even when we make mistakes or do something wrong, it is important to not repeat those actions and instead try to correct them. It emphasizes the importance of doing what is right and following our moral compass. </s>

## 242. Both heaven and fort were lost  (figurative)

- **Gold:** It describes a state of having lost both options, with no support on either side.
- **mT0-large** ✓: Both heaven and fort were lost
- **Qwen3.5-2B** ✓: Both heaven and fort were lost
- **Sarvam-1** ✓: This means that both good things (heaven) and bad things (fortune) have been taken away from someone or something. It is a way to say that everything has its ups and downs, and nothing lasts forever.

## 243. A title for every head, but ruined with nothing for the belly  (figurative)

- **Gold:** A state of mere show: everyone has titles and posts, but there's no food actually to eat.
- **mT0-large** ✓: A title for every head, but ruined with nothing for the belly
- **Qwen3.5-2B** ✓: A title for every head, but ruined with nothing for the belly.
- **Sarvam-1** ✗: This means that if you have a lot of titles or positions and responsibilities, it is not enough to fill your stomach. You need something more than just having power over others. It's like trying to eat an elephant - you can only do so much at once!

## 244. When the orphan shaved his head, hailstones rained  (figurative)

- **Gold:** It describes the misfortune of another trouble striking one who is already in distress and helpless.
- **mT0-large** ✗: When the orphan shaved his head, hailstones rained
- **Qwen3.5-2B** ✓: The orphan shaved his head, hailstones rained
- **Sarvam-1** ✗: This is a very old English saying that means when you do something to get rid of your problems (like cutting off all your hair), then bad things will happen to you. It's like if you cut down all the trees on your farm and there are no more trees left, it might start

## 245. He who cannot live in his own town, will he live in another's town?  (figurative)

- **Gold:** The sense: one who hasn't succeeded in his own town won't succeed merely by going to another.
- **mT0-large** ✗: He who cannot live in his own town, will he live in another's town?
- **Qwen3.5-2B** ✓: He who cannot live in his own town, will he live in another's town?
- **Sarvam-1** ✓: This means that if you don't like where you are living, then it is better to leave than stay there and suffer. It suggests that people should try to improve their situation rather than just accepting things as they are.

## 246. A Ranga in his own town, a monkey in another's town  (figurative)

- **Gold:** One who is a big hero in his own town becomes an unnoticed ordinary person outside.
- **mT0-large** ✗: A monkey in another's town.
- **Qwen3.5-2B** ✓: A Ranga in his own town, a monkey in another's town
- **Sarvam-1** ✓: This means that if you are good at something where you live, then it is easy for you to succeed and get ahead. But if you try to do something different from what you know how to do, or move somewhere else, it will be much harder. It might even seem impossible!

## 247. Went to do a favor, trouble came  (figurative)

- **Gold:** It indicates the situation of getting into trouble oneself while trying to help.
- **mT0-large** ✓: A man went to do a favor, trouble came.
- **Qwen3.5-2B** ✓: The proverb means that when you do a favor for someone, it can lead to trouble.
- **Sarvam-1** ✓: This means that when you try to help someone or do something for them, it can sometimes lead to problems or difficulties. It's like trying to fix a leaky faucet with your finger - it might work at first, but eventually, more water will come out than goes in!

## 248. One can fast, but cannot bear harassment  (literal)

- **Gold:** One can bear the hardship of hunger, but cannot bear others' harassment and nuisance.
- **mT0-large** ✓: One can fast, but cannot bear harassment
- **Qwen3.5-2B** ✓: One can fast, but cannot bear harassment
- **Sarvam-1** ✗: This means that you may be able to do something for a long time without being bothered or disturbed, but if someone keeps trying to make you do it, eventually they will succeed. It's like when you try to run away from a dog - you might be able to keep running

## 249. Like filling salt into a burning belly  (figurative)

- **Gold:** It indicates an act that gives yet more pain to one who is already hurting.
- **mT0-large** ✗: Like filling salt into a burning belly
- **Qwen3.5-2B** ✓: Like filling salt into a burning belly
- **Sarvam-1** ✓: This is an idiom that means to add something unnecessary or unimportant to something already bad, like adding salt to a wound. It's often used when someone is trying to fix a problem but adds more trouble instead. The phrase comes from the idea of putting too much salt on food

## 250. What does the day of the week matter for dealing? What does the time matter for trade?  (literal)

- **Gold:** There is no need to wait for an auspicious day to start a business; any day will do.
- **mT0-large** ✓: The day of the week is important for dealing.
- **Qwen3.5-2B** ✓: The day of the week matters for dealing. The time matters for trade.
- **Sarvam-1** ✓: The proverb is saying that it doesn't really matter what day or time you do something, as long as you do it well and with a good attitude. It emphasizes the importance of doing things right rather than worrying about when they should be done. </s>

## 251. Swaying doll, float when you fall into water  (figurative)

- **Gold:** It may indicate a nature that adapts like a doll and, even when falling into trouble, doesn't sink but floats back up.
- **mT0-large** ✓: A floating doll floats when you fall into water.
- **Qwen3.5-2B** ✗: The doll is a symbol of a person who is easily influenced by others.
- **Sarvam-1** ✓: This means that if someone is trying to do something but they are not very good at it and then they fail, they will still be able to recover from their failure because they have a strong foundation on which to build themselves back up again.

## 252. A cow that won't, a calf that won't eat  (figurative)

- **Gold:** A cow that won't give milk and a calf that won't drink it; a state where both sides refuse and the matter doesn't move.
- **mT0-large** ✓: A cow that won't eat a calf that won't eat
- **Qwen3.5-2B** ✓: A cow that won't, a calf that won't eat
- **Sarvam-1** ✓: This means that if you don't do something or try to achieve something, then it will not happen. It is like saying "if you don't work hard at school, you won't get good grades". If you don't study and learn, you can't become smart

## 253. The forest became fruit, the parrot's mouth got ulcers  (figurative)

- **Gold:** It may indicate bringing trouble on oneself by overusing what was found in abundance.
- **mT0-large** ✓: The forest became fruit, the parrot's mouth got ulcers
- **Qwen3.5-2B** ✓: The forest became fruit, the parrot's mouth got ulcers
- **Sarvam-1** ✓: This means that when you do something wrong or make a mistake, it will have consequences for you later on. It is like saying "the forest became fruit" because if you cut down trees without planting new ones, then eventually there won't be any more forests left. Similarly, if someone

## 254. Why do you get ruined listening to whose words? Listen to me and live  (literal)

- **Gold:** A direct piece of advice from an elder: don't be ruined by listening to others; hear my advice and live well.
- **mT0-large** ✓: Listen to me and live
- **Qwen3.5-2B** ✓: The meaning of the proverb is that you should not listen to people who are not good for you.
- **Sarvam-1** ✓: This means that if you listen to someone who is not a good person, they will eventually hurt or damage your life. It's better to be careful about whom you listen to. [/INST]

## 255. Who knows which snake is in which anthill  (figurative)

- **Gold:** One cannot know where an unseen danger lies hidden, so one must be careful.
- **mT0-large** ✗: The snake is in the anthill.
- **Qwen3.5-2B** ✓: Who knows which snake is in which anthill.
- **Sarvam-1** ✓: This means that you can't tell what someone else is thinking or doing, because they might be hiding something bad about themselves. It's like trying to figure out if a snake is in its hole by looking at it - you won't know for sure until you look inside!

## 256. Whatever season fails, the season of death never fails  (literal)

- **Gold:** Even if all other seasons fail, the season of death does not fail; death will surely come.
- **mT0-large** ✓: The season of death never fails.
- **Qwen3.5-2B** ✓: The season of death never fails.
- **Sarvam-1** ✓: This means that no matter what happens or how bad things get, there will always be a time when everything is over and done with. It's like saying "the end of the rainbow" - even if you can't see it right now, it's still out there somewhere."

## 257. Like learning sword-play in the time of war  (figurative)

- **Gold:** Trying to learn when the need arises is too late; one must prepare beforehand.
- **mT0-large** ✗: Like learning sword-play in the time of war
- **Qwen3.5-2B** ✓: Like learning sword-play in the time of war
- **Sarvam-1** ✓: This means that it is better to learn something when you need it, rather than waiting until later. It's like practicing your sword skills during a battle - if you wait too long, you might not be able to use them effectively.

## 258. Learn a wise word even from children  (literal)

- **Gold:** Wise words should be heard and understood no matter who says them, even children.
- **mT0-large** ✓: Learn a wise word even from children
- **Qwen3.5-2B** ✓: The meaning of the proverb is that children are often the best teachers of wisdom.
- **Sarvam-1** ✓: This means that you should learn something valuable, no matter how small or insignificant it may seem to be. It's important not to underestimate the value of knowledge and wisdom, especially when they come from unexpected sources.

## 259. Enjoyment only as much as destiny allows  (literal)

- **Gold:** One gets to enjoy only as much happiness as is written in one's fortune.
- **mT0-large** ✓: Enjoyment only as much as destiny allows
- **Qwen3.5-2B** ✓: Enjoyment only as much as destiny allows
- **Sarvam-1** ✓: This means that you should enjoy life to its fullest, but not at the expense of your own happiness or well-being. If something is beyond your control, it's best to accept it and move on.

## 260. What the ascetic brought is for the ascetic, what the pleasure-seeker brought is for the pleasure-seeker  (figurative)

- **Gold:** Earned wealth gets spent according to the nature of whoever's hands it falls into.
- **mT0-large** ✓: The ascetic brought what the ascetic brought, what the pleasure-seeker brought what the pleasure-seeker brought.
- **Qwen3.5-2B** ✓: The ascetic brought what the ascetic brought, what the pleasure-seeker brought is for the pleasure-seeker.
- **Sarvam-1** ✓: This means that people who are looking to find spiritual enlightenment or a higher purpose will often bring their own beliefs and values with them when they seek out new experiences or opportunities. On the other hand, those who are focused on personal enjoyment and self-gratification may be more

## 261. A ruler who doesn't know worth and a doctor who doesn't know disease are the same  (figurative)

- **Gold:** A ruler who cannot identify people's abilities fails in his work, like a doctor who cannot identify disease.
- **mT0-large** ✗: A ruler who doesn't know worth and a doctor who doesn't know disease are the same
- **Qwen3.5-2B** ✓: A ruler who doesn't know worth and a doctor who doesn't know disease are the same.
- **Sarvam-1** ✓: This means that someone who is not good at something will be bad at it, just like how a ruler who doesn't know what is valuable won't know what is important, and a doctor who doesn't know what causes diseases won't know how to treat them.

## 262. Like going to a town where nobody is and wanting water and buttermilk  (figurative)

- **Gold:** It is futile to expect help or hospitality where there is nobody.
- **mT0-large** ✓: Like going to a town where nobody is and wanting water and buttermilk
- **Qwen3.5-2B** ✓: Like going to a town where nobody is and wanting water and buttermilk.
- **Sarvam-1** ✓: This means that if you go somewhere without knowing anyone, it will be difficult to find what you need. It's like trying to get something from an empty place.

## 263. To a house where no one is, he said 'I am Jogappa'  (figurative)

- **Gold:** Strutting about as a big man where there is no one to question him.
- **mT0-large** ✓: He said to a house where no one is, he said 'I am Jogappa'
- **Qwen3.5-2B** ✓: To a house where no one is, he said 'I am Jogappa'
- **Sarvam-1** ✗: This means that if you are not there to help or support someone then they will be left alone and forgotten about. It can also mean that when people don't have anyone else to turn to for advice or help then they may end up making bad decisions because they feel like nobody cares

## 264. As the king, so the subjects  (literal)

- **Gold:** As the king is, so are the subjects; people follow the leader's conduct.
- **mT0-large** ✗: As the king, so the subjects
- **Qwen3.5-2B** ✓: The king is the head of the state, and the subjects are the people.
- **Sarvam-1** ✓: This means that if a person is powerful or important, they will have more power over others. It's like saying "the bigger fish eats the smaller ones". The phrase comes from an old English poem called 'The King and His Subjects'. In this story, the king has all

## 265. When he told his sorrow to his sister's husband, he said 'leave your children and come'  (figurative)

- **Gold:** If you tell your sorrow to the wrong person, he gives improper advice suited to his own selfishness.
- **mT0-large** ✓: When he told his sister's husband, he said 'leave your children and come'
- **Qwen3.5-2B** ✓: When he told his sorrow to his sister's husband, he said 'leave your children and come'
- **Sarvam-1** ✓: This is a very old saying that means when you are sad or upset about something, it can be helpful to talk to someone who will not judge you but will listen to what you have to say. It also suggests that sometimes people need help from others more than they realize. So if you feel

## 266. Like raising a pumpkin and giving it to the pot-maker  (figurative)

- **Gold:** The fruit of what one raised with effort goes to those who don't deserve it.
- **mT0-large** ✓: Like raising a pumpkin and giving it to the pot-maker
- **Qwen3.5-2B** ✓: Like raising a pumpkin and giving it to the pot-maker
- **Sarvam-1** ✓: This is an English saying that means you can't take something back once you have given it away, or offered it up for someone else to use. It comes from the idea of trying to make a big change by using your own efforts (like growing a large pumpkin), but then realising

## 267. After death, what if he went anywhere?  (figurative)

- **Gold:** The sense: after everything has gone beyond reach, regret, or going anywhere, is of no use.
- **mT0-large** ✗: He would go to heaven.
- **Qwen3.5-2B** ✓: After death, what if he went anywhere?
- **Sarvam-1** ✓: This means that when someone dies, they can't go to heaven or hell anymore. They are gone forever.

## 268. Will a dead hen peck at paddy?  (figurative)

- **Gold:** One who is already powerless or sunk cannot harm anyone.
- **mT0-large** ✗: A dead hen will peck at a paddy.
- **Qwen3.5-2B** ✓: A dead hen cannot peck at paddy because it is already dead.
- **Sarvam-1** ✓: This is an old English saying that means "a person who has nothing to lose will do anything". It's used when someone does something stupid or dangerous because they are not afraid of getting hurt, just like how a chicken might peck at rice if it thinks there isn't any

## 269. Like the herdsmen building a monastery  (figurative)

- **Gold:** Taking on a big undertaking that doesn't suit one's background and qualifications and becoming a laughing stock.
- **mT0-large** ✗: Like the herdsmen building a monastery
- **Qwen3.5-2B** ✓: Like the herdsmen building a monastery
- **Sarvam-1** ✓: This is an idiom that means to build something on top of other things without knowing what you are doing or where it will end up. It can also mean to do something with little planning and preparation, which may lead to problems later on. The phrase comes from the idea of people who were

## 270. The male is a boulder, the female is lame  (figurative)

- **Gold:** It may mean that one is rock-firm in his stand and the other yields to circumstances.
- **mT0-large** ✓: The male is a boulder, the female is lame
- **Qwen3.5-2B** ✓: The male is a boulder, the female is lame
- **Sarvam-1** ✓: This means that men are strong and powerful while women are weak and fragile. It's not meant to be taken literally but rather as an expression of how society often views these two genders.

## 271. The man ruined by sitting, the woman ruined by wandering  (figurative)

- **Gold:** Men are ruined by laziness, women by excessive frivolity or gossip and laughter.
- **mT0-large** ✓: The man ruined by sitting, the woman ruined by wandering
- **Qwen3.5-2B** ✓: The man ruined by sitting, the woman ruined by wandering
- **Sarvam-1** ✓: This is a saying that means if you waste your time on something or someone, then they will be hurt as well. It's like when you sit around and do nothing, it can make you feel lazy and unproductive. If you spend too much time with someone who isn'

## 272. When the husband was there, no sense; when sense came, no husband  (figurative)

- **Gold:** When an opportunity or help is there, its value isn't understood; when it is, it has slipped away.
- **mT0-large** ✓: When the husband was there, no sense came.
- **Qwen3.5-2B** ✓: The husband was there, no sense; when sense came, no husband
- **Sarvam-1** ✓: This means that if you have a problem or need help with something and your partner is not around to assist you, then it's useless because they won't be able to help you once they return home. But if you are facing a challenge and your spouse is available to lend

## 273. Evening doesn't come without chatter, the road doesn't wear out without company  (figurative)

- **Gold:** With conversation and company, time and the road pass easily.
- **mT0-large** ✓: A few people went to the woods to talk about their evening.
- **Qwen3.5-2B** ✓: The road doesn't wear out without company
- **Sarvam-1** ✓: This means that even when you are waiting for something to happen or expecting it to be done, there is still a lot going on around you and things can change quickly. It also suggests that having people with you makes life more enjoyable and less boring. [/INST]

## 274. Play for the cat, mortal agony for the mouse  (figurative)

- **Gold:** What is play or fun for one is life-threatening agony for another.
- **mT0-large** ✓: Play for the cat, mortal agony for the mouse
- **Qwen3.5-2B** ✓: The cat is a symbol of the wealthy, the mouse is a symbol of the poor.
- **Sarvam-1** ✓: This means that you should not try to do something difficult or dangerous if it will cause harm to yourself. It is better to play safe and easy than risk your life trying to win a prize.

## 275. Like the monkey that tasted sweetness climbing the loft  (figurative)

- **Gold:** One who has once tasted profit or pleasure goes back to the same place again and again.
- **mT0-large** ✗: Like the monkey that tasted sweetness climbing the loft
- **Qwen3.5-2B** ✓: The monkey that tasted sweetness climbing the loft
- **Sarvam-1** ✓: This means to try something new and risky, even if it seems appealing or enjoyable at first. The monkey's actions are a metaphor for taking risks, as climbing up high can be dangerous.

## 276. Ruined by not asking for the loan given, ruined by not looking at the field sown  (figurative)

- **Gold:** Not collecting a loan given and not caring for a sown field cause loss; one must keep watch over one's dealings.
- **mT0-large** ✓: The poor man was ruined by not asking for the loan given.
- **Qwen3.5-2B** ✓: The meaning of the proverb is that if you do not ask for the loan given, you will not get the loan given.
- **Sarvam-1** ✓: This means that if you don't ask for help or advice when you need it, then you will end up with a problem. It is like planting seeds without watering them - they won't grow well and may even die. Similarly, if we don't take advantage of opportunities

## 277. Like keeping the mirror in the hand and looking for the face in the water  (figurative)

- **Gold:** Searching far away without noticing what's close at hand.
- **mT0-large** ✗: Like keeping the mirror in the hand and looking for the face in the water
- **Qwen3.5-2B** ✓: Like keeping the mirror in the hand and looking for the face in the water
- **Sarvam-1** ✗: This means that you should not look at things from a distance, but rather try to see them as they are right now. It's like holding a mirror up to something so you can see it clearly without any distortion or misinterpretation. </s>

## 278. What came to the hand did not reach the mouth  (figurative)

- **Gold:** A gain or opportunity that had come within reach slips away at the last moment.
- **mT0-large** ✗: The word came to the hand did not reach the mouth.
- **Qwen3.5-2B** ✓: The meaning of the proverb is that the person who has the opportunity to do something is the one who will do it.
- **Sarvam-1** ✓: This means that if you do something, it will be a waste of time and effort because you cannot get what you want from it. It is like trying to catch fish with your hands instead of using a fishing rod. You might try hard but you won't succeed.

## 279. A lame cry for one who cries lame, a standing cry for one who cries standing  (figurative)

- **Gold:** It may mean that everyone makes their own complaint or excuse to suit their own condition.
- **mT0-large** ✓: A lame cry for one who cries lame, a standing cry for one who cries standing
- **Qwen3.5-2B** ✓: A lame cry for one who cries lame, a standing cry for one who cries standing.
- **Sarvam-1** ✓: This means that if you are not doing anything to solve your problem or make things better, then it is pointless to complain about it. It's like trying to stand on ice when you can't walk - it won't work!

## 280. What is day to a blind man? What is night?  (figurative)

- **Gold:** To one who doesn't understand sense or responsibility, every time and occasion is the same; telling him is useless.
- **mT0-large** ✓: A day to a blind man is a day to a night.
- **Qwen3.5-2B** ✓: The proverb illustrates that a person who lacks knowledge or vision cannot perceive the fundamental differences between day and night.
- **Sarvam-1** ✓: This means that you can't see what isn't there, and you can't know what isn't known. It also implies that if you don't have any information about something, it doesn't matter how much time passes because you still won't be able to find

## 281. Though small, Shiva's wisdom  (figurative)

- **Gold:** One who, though small in age, is like an elder in understanding and discernment.
- **mT0-large** ✓: The wisdom of Shiva is small.
- **Qwen3.5-2B** ✓: Though small, Shiva's wisdom
- **Sarvam-1** ✓: This means that even though someone is very young or small, they can still have a lot of knowledge and understanding about things. It's like saying "even a tiny seed can grow into a big tree."

## 282. Though there is stream water, well water is better  (figurative)

- **Gold:** It may mean a safe, trusted source is better than an apparently abundant but uncertain one.
- **mT0-large** ✓: Well water is better than stream water.
- **Qwen3.5-2B** ✓: Though there is stream water, well water is better.
- **Sarvam-1** ✓: This means that if you have a choice between two things and both are good but only one can be used at a time, then it's best to use the thing that will not get spoiled or wasted. In this case, using the stream water would mean that you could drink it

## 283. Even if you blame your mother, don't blame water  (figurative)

- **Gold:** Water, the basis of life, should be regarded with respect, not neglected or blamed.
- **mT0-large** ✓: Even if you blame your mother, don't blame water
- **Qwen3.5-2B** ✓: The proverb means that even if you blame your mother, don't blame water.
- **Sarvam-1** ✗: This means that even when we are angry with someone or something, it is not a good idea to blame them for everything. We should try to understand why they did what they did and find ways to solve our problems without blaming others.

## 284. Even if it is trash, make it tasty and eat it  (figurative)

- **Gold:** Even if what one has is ordinary, one should use it well with cleverness and be content.
- **mT0-large** ✗: Even if it is trash, make it tasty and eat it
- **Qwen3.5-2B** ✓: Even if it is trash, make it tasty and eat it
- **Sarvam-1** ✓: This means that even if something seems bad or useless to you, there may be a way to turn it into something useful or enjoyable. It's important to look for opportunities where others might see only problems.

## 285. Even if the salary is six kaasu, do palace work  (figurative)

- **Gold:** A job with respect and security is better even if the salary is low.
- **mT0-large** ✗: Even if the salary is six kaasu, do palace work
- **Qwen3.5-2B** ✗: The salary is six kaasu, do palace work.
- **Sarvam-1** ✓: This means that even though you are paid a lot for your job, it doesn't mean that you should be doing something that isn't important or valuable to the company. It's better to focus on what really matters and not get distracted by things that aren't as important.

## 286. Talk increased and the house was ruined, seed increased and the field was ruined  (figurative)

- **Gold:** Excessive talk spoils the peace of a house, excessive seed spoils a field; excess in anything is not good.
- **mT0-large** ✓: The increase in talk and the house was ruined.
- **Qwen3.5-2B** ✓: The house was ruined because of the increased talk.
- **Sarvam-1** ✓: This means that if you talk too much or make a lot of noise about something then it will cause problems for you. It is like saying that talking too much can lead to trouble. The phrase comes from an old English poem called "The House That Jack Built". In this poem, there are

## 287. No chest without a bullock, no home without children  (figurative)

- **Gold:** It may mean that those without needed support have neither courage nor the comfort of a home.
- **mT0-large** ✗: A few dogs are without a collar, and a few dogs are without a home.
- **Qwen3.5-2B** ✓: No chest without a bullock, no home without children.
- **Sarvam-1** ✓: This means that you need to have something valuable or important before you can achieve anything else. It is like saying that if you want to be successful, you must first have your own resources and support system. If you don't have these things, then it will be difficult for you to succeed.

## 288. Don't scatter ruin saying 'I am ruined'  (figurative)

- **Gold:** One shouldn't do harm to others out of despair, thinking oneself ruined or wronged.
- **mT0-large** ✓: Don't scatter ruin saying 'I am ruined'
- **Qwen3.5-2B** ✓: Don't scatter ruin saying 'I am ruined'
- **Sarvam-1** ✓: This means that if you say something is ruined, it will be true because you have already destroyed what was once good or valuable. It can also mean that when someone says they are ruined, others may believe them and not try to help them get better.

## 289. Pat your head and walk looking at the ground  (literal)

- **Gold:** It can be called direct advice: step carefully, humbly, looking at the ground.
- **mT0-large** ✗: Walk looking at the ground.
- **Qwen3.5-2B** ✓: Pat your head and walk looking at the ground
- **Sarvam-1** ✓: This means that if you are feeling down or upset, it is best to stop what you are doing and take a break from whatever you were doing. It can be hard to do this when we feel like we need to keep going, but taking a break will help us think more clearly and come

## 290. The head man's word: salt in front, jaggery behind  (figurative)

- **Gold:** Elders' words may seem bitter (salt) at first but finally bear sweet (jaggery) fruit.
- **mT0-large** ✓: The head man's word: salt in front, jaggery behind
- **Qwen3.5-2B** ✓: The head man's word: salt in front, jaggery behind
- **Sarvam-1** ✓: This means that if someone is a leader or has authority over others, they are expected to be honest and follow through on their promises. If they don't keep their promise, it can damage their reputation and trustworthiness among those who look up to them.

## 291. Father's word, an elephant's strength  (literal)

- **Gold:** A father's guidance and support give as much strength as an elephant.
- **mT0-large** ✓: The word of the father is a strength of an elephant.
- **Qwen3.5-2B** ✓: Father's word, an elephant's strength
- **Sarvam-1** ✓: This means that children will listen to their parents and follow what they say because it is important for them to do so. It also suggests that if a child does not want to obey his father or mother, he should try harder to change his mind.

## 292. Don't separate elder and younger brother  (literal)

- **Gold:** Brothers should not be split apart but allowed to stay united.
- **mT0-large** ✓: Don't separate elder and younger brother
- **Qwen3.5-2B** ✓: Don't separate elder and younger brother
- **Sarvam-1** ✓: This means that you should not treat your older or younger siblings differently, because they are all brothers to each other.

## 293. Health is wealth  (literal)

- **Gold:** Good health is the greatest wealth a person has.
- **mT0-large** ✓: Health is wealth
- **Qwen3.5-2B** ✓: Health is wealth.
- **Sarvam-1** ✓: This means that good health is more important than money or material possessions. It's better to be healthy and happy than rich but unhealthy and poor.

## 294. Slowness is the chief thing  (literal)

- **Gold:** In any task, doing it slowly without haste is what matters and is safe.
- **mT0-large** ✓: Slowness is the chief thing
- **Qwen3.5-2B** ✓: Slowness is the chief thing
- **Sarvam-1** ✓: This means that slowness can be a good thing, and it's better to take your time than rush through things. It's not always about being fast or quick; sometimes taking your time can lead to better results.

## 295. There is no age for learning  (literal)

- **Gold:** There is no age limit for learning; one can learn something new at any age.
- **mT0-large** ✓: There is no age for learning
- **Qwen3.5-2B** ✓: There is no age for learning
- **Sarvam-1** ✓: This means that you should never stop learning, even if you are old or have already learned everything. It's important to keep an open mind and continue to learn new things throughout your life.

## 296. There is strength in unity  (literal)

- **Gold:** When everyone joins together, great strength comes and even a hard task gets done.
- **mT0-large** ✓: There is strength in unity
- **Qwen3.5-2B** ✓: There is strength in unity
- **Sarvam-1** ✓: This means that when people work together, they can achieve more than if they worked alone. It's a reminder to be united and support each other. </s>

## 297. Saying is easy, doing is hard  (literal)

- **Gold:** Saying a task is easy, but actually doing it is hard.
- **mT0-large** ✗: Saying is easy, doing is hard
- **Qwen3.5-2B** ✓: Saying is easy, doing is hard.
- **Sarvam-1** ✓: This means that it's easier to say something than actually do it. It takes more effort and work to accomplish a goal or task. [/INST]

## 298. Many drops joined make a stream  (literal)

- **Gold:** Small drops, when joined together, make a stream flow; small things add up to something big.
- **mT0-large** ✓: Many drops joined make a stream
- **Qwen3.5-2B** ✓: Many drops joined together make a stream.
- **Sarvam-1** ✓: This means that when many people work together, they can achieve great things. It is like how water flows downhill to become a river. If you want something big and important, it takes more than just one person or group working alone. You need lots of people who are willing to help each

## 299. The prosperity of a growing plant is seen in the sprout  (literal)

- **Gold:** Whether a plant will grow well later is seen at the sprout stage itself.
- **mT0-large** ✓: The prosperity of a growing plant is seen in the sprout
- **Qwen3.5-2B** ✓: The prosperity of a growing plant is seen in the sprout
- **Sarvam-1** ✓: This means that when something grows, it shows its potential to grow more and become bigger. It's like how plants start as tiny seeds and then grow into big trees or flowers. Similarly, people can also show their potential by working hard and achieving success.

## 300. There is no taste greater than salt  (literal)

- **Gold:** Salt is essential to the taste of cooking; nothing gives as much flavor as salt.
- **mT0-large** ✓: There is no taste greater than salt
- **Qwen3.5-2B** ✓: The meaning of the proverb is that salt is the most basic and essential ingredient in cooking.
- **Sarvam-1** ✗: This means that there is nothing more important or valuable than something you love and enjoy doing, like eating food with a lot of salt. It's not just about tasting good; it's also about having fun and being happy!

## 301. The fence is witness for the garden lizard  (literal)

- **Gold:** This proverb indicates being moderate and in a middle condition, neither excessive nor very low or poor in any matter.
- **mT0-large** ✓: The fence is witness for the garden lizard
- **Qwen3.5-2B** ✓: The fence is witness for the garden lizard
- **Sarvam-1** ✓: A fence can be used to keep animals out, but it also keeps people from seeing what's happening inside the garden. This means that sometimes we need to hide things or protect them so they don't get hurt or lost.

## 302. Does a sore on the palm need a mirror?  (figurative)

- **Gold:** This proverb says that a plainly visible truth or matter needs no proof or witness.
- **mT0-large** ✓: A sore on the palm need a mirror.
- **Qwen3.5-2B** ✓: Does a sore on the palm need a mirror?
- **Sarvam-1** ✓: A sore is an injury or wound, and mirrors are used to see what’s wrong with your appearance. This means that if you have a problem (a “sore”), it might be better to talk about it rather than trying to fix it yourself. It can also mean

## 303. Sense came after being ruined  (literal)

- **Gold:** This proverb indicates that a person gains proper understanding or knowledge only after making a mistake or suffering a loss.
- **mT0-large** ✓: The sense came after being ruined.
- **Qwen3.5-2B** ✓: The meaning of the proverb is that the sense of the situation is not the same as the situation itself.
- **Sarvam-1** ✓: This means that if you lose something valuable, it is better to get it back than to keep losing more and more things. It's like a saying that "you can't make up for what has been lost".

## 304. Two hands joined make a clap  (figurative)

- **Gold:** This proverb indicates that for any big task, quarrel or agreement to succeed or be resolved, mutual cooperation or consensus of two parties is essential.
- **mT0-large** ✓: Two hands joined make a clap
- **Qwen3.5-2B** ✓: Two hands joined make a clap
- **Sarvam-1** ✓: This means that when two people work together, they can accomplish more than if each person worked alone. It is often used to encourage teamwork and cooperation between individuals or groups. </s>

## 305. Counts for the game, not for the reckoning  (figurative)

- **Gold:** This proverb indicates a thing or person that exists only nominally or formally and is not counted in real responsibility or calculation.
- **mT0-large** ✗: The players count for the game, not for the reckoning.
- **Qwen3.5-2B** ✓: The game is the game, not the game.
- **Sarvam-1** ✓: This means that it is more important to do something well than to worry about what will happen afterwards. It's like a sports player who does their best and tries hard even if they don't win - because doing well matters more than being perfect.
