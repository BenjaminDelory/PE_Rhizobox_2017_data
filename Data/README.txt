This README.txt file was generated on 20210807 by Benjamin Delory

-------------------
GENERAL INFORMATION
-------------------

1. Raw data used for the following paper: Alonso-Crespo et al (2021) Assembly history modulates vertical root distribution in grassland communities.  

2. Author Information

  Principal Investigator Contact Information
        Name: Benjamin M. Delory
        Institution: Institute of Ecology, Leuphana University
        Address: Universitaetsallee 1, 21335 Lueneburg, Germany
        Email: benjamin.delory@leuphana.de

  Associate or Co-investigator Contact Information
        Name: Inés Alonso-Crespo, Emanuela W.A. Weidlich, Vicky M. Temperton
        Institution: Institute of Ecology, Leuphana University
        Address: Universitaetsallee 1, 21335 Lueneburg, Germany

3. Date of data collection (harvest): 27-28 September 2017 

4. Geographic location of data collection: Lueneburg, Germany

5. Data collected by Benjamin M. Delory, Emanuela W.A. Weidlich and Inés Alonso-Crespo

-----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: Data_shoot_biomass_RZ_PE_2017.txt
-----------------------------------------------------------------

1. Number of variables: 16

2. Number of cases/rows: 35

3. Variable List
    A. Name: Treatment
       Description: plant functional group order of arrival. This factor has 5 levels:
	- Sync1: forbs, grasses and legumes sown simultaneously at the first sowing event
	- Sync2: forbs, grasses and legumes sown simultaneously at the second sowing event
	- F-first: forbs sown 10 days before grasses and legumes
	- G-first: grasses sown 10 days before forbs and legumes
	- L-first: legumes sown 10 days before forbs abd grasses

    B. Name: Replicate
       Description: the replicate number
       Type: integer (1 to 7)

    C. Name: Rz
       Description: the rhizobox ID number
       Type: integer

    D. Name: Tp
       Description: shoot dry weight of Trifolium pratense
       Type: numeric
       Unit: g

    E. Name: Lc
       Description: shoot dry weight of Lotus corniculatus
       Type: numeric
       Unit: g
       Missing values: NA

    F. Name: Ms
       Description: shoot dry weight of Medicago sativa
       Type: numeric
       Unit: g

    G. Name: Fr
       Description: shoot dry weight of Festuca rubra
       Type: numeric
       Unit: g

    H. Name: Hl
       Description: shoot dry weight of Holcus lanatus
       Type: numeric
       Unit: g

    I. Name: Dg
       Description: shoot dry weight of Dactylis glomerata
       Type: numeric
       Unit: g

    J. Name: Cj
       Description: shoot dry weight of Centaurea jacea
       Type: numeric
       Unit: g

    K. Name: Lv
       Description: shoot dry weight of Leucanthemum vulgare
       Type: numeric
       Unit: g

    L. Name: Am
       Description: shoot dry weight of Achillea millefolium
       Type: numeric
       Unit: g

    M. Name: Legumes
       Description: shoot dry weight of legumes
       Type: numeric
       Unit: g

    N. Name: Grasses
       Description: shoot dry weight of grasses
       Type: numeric
       Unit: g

    O. Name: Forbs
       Description: shoot dry weight of forbs
       Type: numeric
       Unit: g

    O. Name: Total
       Description: total shoot dry weight
       Type: numeric
       Unit: g

----------------------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: Data_root_biomass_RZ_PE_2017.txt
----------------------------------------------------------------

1. Number of variables: 6

2. Number of cases/rows: 186

3. Variable List
    A. Name: Rz
       Description: the rhizobox ID number
       Type: integer

    B. Name: Treatment
       Description: plant functional group order of arrival. This factor has 5 levels:
	- Sync1: forbs, grasses and legumes sown simultaneously at the first sowing event
	- Sync2: forbs, grasses and legumes sown simultaneously at the second sowing event
	- F-first: forbs sown 10 days before grasses and legumes
	- G-first: grasses sown 10 days before forbs and legumes
	- L-first: legumes sown 10 days before forbs abd grasses

    C. Name: Replicate
       Description: the replicate number
       Type: integer (1 to 7)

    D. Name: Layer
       Description: the soil layer in which roots were collected
       Description: roots were collected from 6 layers: 0-10 cm, 10-20 cm, 20-30 cm, 30-40 cm, 40-50 cm and 50-60 cm (or >50 cm)

    E. Name: maxDepth
       Description: the maximum soil depth of each layer
       Type: integer
       Unit: cm

    F. Name: RDW
       Description: total root dry weight measured in each layer
       Type: numeric
       Unit: g

--------------------------------------------------
DATA-SPECIFIC INFORMATION FOR: Date_TimePoint.txt
--------------------------------------------------

1. Number of variables: 2

2. Number of cases/rows: 43

3. Variable List
    A. Name: Date
       Description: the date of each day between the start and end of the experiment
       Format: YYYY-MM-DD

    B. Name: Day
       Description: the day number
       Type: integer

--------------------------------------------
DATA-SPECIFIC INFORMATION FOR: Image_RZ.txt
--------------------------------------------

1. Number of variables: 2

2. Number of cases/rows: 35

3. Variable List
    A. Name: Image
       Description: the image number in the sequence of root images
       Type: integer

    B. Name: RZ
       Description: the rhizobox ID number
       Type: integer

-------------------------------------------
DATA-SPECIFIC INFORMATION FOR: results.csv
-------------------------------------------

1. Number of variables: 2

2. Number of cases/rows: 665

3. Variable List
    A. Name: image
       Description: the name of each image segmented by RootPainter
       Type: character
       Format: YYYY-MM-DD-RZ-ImageNumber.png

    B. Name: mrd
       Description: the mean rooting depth estimated using image analysis (see Figure 1 of the paper)
       Type: numeric
       Unit: cm