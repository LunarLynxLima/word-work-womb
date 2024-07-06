## Comparison between Laplace and Kneser ney smoothing techniques

- Laplace smoothing is easier to implement while Kneser ney is more complicated.
-  Laplace takes away too much probability mass from seen events and assign too much probability mass to unseen events. While Kneser key uses absolute discounting (based on good turing) dont affect the probability of more recurring events much thus results in better outputs. It corrects this by considering the frequency of the unigram in relation to possible words preceding it.

## Generated samples

### anger
- occured dangerous impatient sarcastic rushed
- ive disrespected selfish spite idiocy disagreement enraged frustrated hostile toward hateful

### fear
- during hyperventilating timid restless vibrations disoriented unprepared skeptical unclear sinus apprehensive
- a cautious scares spider unprotected hesitant encountered sinus nervous speculation vibrations

### joy
- no creativity exhilarated exciting cool optimism pleased vibrant confident popular excited
- im invigorated insatiably excited invigorated insatiably optimism brave wonderfully harmonious cute

### love
- ill admiration passionately adoring empathize kissed forgiving dear liked soft desires
- id fond loving wishing soft tempting longing warmth longingly tempting amorous

### sadness
- occured inadequate disillusioned devastated lame disadvantaged boring
- heated listless aching overworked regretful regretful dull lacking low marginalised unhappy

### surprise
- a population visitors library surprised fruits remembering surprised popped mineral strange
- no shocked crystal proved unexpected surprisingly visiting interacting tales wax awe


## Accuracy and macro F1 score of extrinsic evaluation
- Train Accuracy = 99.66666666666667 %
- Test Accuracy = 92.66666666666666 %
- F1 Score = 0.92120017108667

## Reasoning for method used for including emotion component
We have added the emotion of the unigram(next word) to the bigram probability resulting in combined/modified probability which is used by taking one the most probable to get subsequent words given a seed word for a sentence.

Bigram_modified(w_i,w_(i-1)) = (count(w_(i-1),w_i)/count(w_(i-1))  +  b_i
= bigram_prob(w_(i),w_(i-1)) + emotion(w_i)

Using this we get 6 different matrices for 6 different emotions and based on the input emotion respective matrix is considered for scentence generation.

## Top 5 bigrams before smoothing

('kg', 'for'): 1.0 \
('slopes', 'thats'): 1.0 \
('gods', 'plan'): 1.0 \
('dust', 'to'): 1.0 \
('uw', 'school'): 1.0 \

## Top 5 bigrams after Laplace smoothing:
('i', 'feel'): 0.11043610327619874 \
('feel', 'like'): 0.0350976507217662 \
('i', 'am'): 0.03189412019960946 \
('that', 'i'): 0.02650602409638554 \
('and', 'i'): 0.023103748910200523


## Credit

### More of less everyone has contributed to the every part of the assignment. For the sake of submission we are providing the following credits
- Task 1
  - Manav Mittal (2021538), Utkarsh Venaik (2021570), Akash Kushwaha (2021514) Lakshay Kumar (2021061)
- Task 2
1. Akash Kushwaha (2021514), Lakshay Kumar (2021061)
1. Akash Kushwaha (2021514), Utkarsh Venaik (2021061)
1. Manav Mittal (2021514), Lakshay Kumar (2021061)
1. Manav Mittal (2021514), Utkarsh Venaik (2021061)

