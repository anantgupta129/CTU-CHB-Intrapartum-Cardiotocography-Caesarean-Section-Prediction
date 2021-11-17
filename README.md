# CTU-CHB Intrapartum Cardiotocography (Caesarean Section or Normal Delivery Prediction)


This database, from the Czech Technical University (CTU) in Prague and the University Hospital in Brno (UHB), contains 552 cardiotocography (CTG) recordings, which were carefully selected from 9164 recordings collected between 2010 and 2012 at UHB.

The dataset can be found at [*MIT Physio Net Database*](https://physionet.org/content/ctu-uhb-ctgdb/1.0.0/)

## Data Description

The CTG recordings start no more than 90 minutes before actual delivery, and each is at most 90 minutes long. Each CTG contains a fetal heart rate (FHR) time series and a uterine contraction (UC) signal, each sampled at 4 Hz.

The priority was to create as homogeneous a set as possible; thus only recordings fulfilling the following criteria were included:

- Singleton pregnancy
- Gestational age >36 weeks
- No a priori known developmental defects
- Duration of stage 2 of labor ≤ 30 minutes
- FHR signal quality (i.e. percentage of the recording during which FHR data were available) > 50% in each 30 minute window
- Available analysis of biochemical parameters of umbilical arterial blood sample (i.e. pH)
- Majority of vaginal deliveries (only 46 cesarean section (CS) deliveries included)

Additional parameters were collected for all recordings, and are available in the (text) .hea files of the records:

- Maternal data: age; parity; gravidity;
- Delivery data: type of delivery (vaginal; operative vaginal; CS); duration of delivery; meconium stained fluid; type of measurement (i.e. ultrasound or direct scalp electrode);
- Fetal data: sex; birth weight;
- Fetal outcome data: analysis of umbilical artery blood sample (i.e. pH; pCO2; pO2; base excess and computed BDecf); Apgar score; neonatology evaluation (i.e. need for O2; seizures; admission to NICU)
- Expert evaluation of the CTG data "Gold Standard" evaluation based on annotation of the signals by 9 expert obstetricians (following FIGO guidelines used in the Czech Republic) including variability/confidence for each signal (Note: these data are not yet available!)


## Procedure

* [data analysis](01-data_analysis.ipynb): analysing signals using power spectrum to remove noise. The power spectrum results did not show any noise in the data hence to remove the noise interpolation was used. The idea is to use fill the gaps with the interpolation values as we noticed there is no actual noise in the data, we are seeing 0 may due to changing in placement of scope to another position or rotation of the baby or any other value.
* [De-Noising Signals using Interpolation](create_interpolated_df.py): take all the signals in database and apply interpolation over it and store them in [seperate csv files in](database/signals-interpolated/)
* [Class Balancing](class_balancing_adasyn.ipynb): There is high imbalanc between the classes. Class balancing is done using ADASYN Technique.
* [Feature Extraction](feature_extraction.py)
* [Model Training using original data](train.ipynb) and [Model Training on Interpolated Signals](train-interpolated.ipynb)