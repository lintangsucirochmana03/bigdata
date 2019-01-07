# minggu-11

# Melakukan Clone repo Pandas Cookbook di direktori Pandas-Cookbook

	lenovo@user MINGW64 /d/Pandas-Cookbook
	$ git clone https://github.com/PacktPublishing/Pandas-Cookbook.git
	Cloning into 'Pandas-Cookbook'...
	remote: Enumerating objects: 100, done.
	remote: Total 100 (delta 0), reused 0 (delta 0), pack-reused 100
	Receiving objects: 100% (100/100), 33.40 MiB | 97.00 KiB/s, done.
	Resolving deltas: 100% (19/19), done.
	Checking connectivity... done.
	Checking out files: 100% (70/70), done.

# Melakukan Copy notebook Jupyter untuk bab 3 di direktori praktik pada folder minggu-11

# Menjalankan notebook Jupyter untuk bab 3 :

	(base) C:\Users\lenovo>D:
	(base) D:\>cd databigdataku
	(base) D:\databigdataku>cd bigdata
	(base) D:\databigdataku\bigdata>cd minggu-11
	(base) D:\databigdataku\bigdata\minggu-11>cd praktik
	(base) D:\databigdataku\bigdata\minggu-11\praktik>activate name_of_my_env
	(name_of_my_env) D:\databigdataku\bigdata\minggu-11\praktik>jupyter notebook
	[I 22:27:00.640 NotebookApp] The port 8888 is already in use, trying another por
	t.
	[I 22:27:01.871 NotebookApp] Serving notebooks from local directory: D:\databigd
	ataku\bigdata\minggu-11\praktik
	[I 22:27:01.871 NotebookApp] The Jupyter Notebook is running at:
	[I 22:27:01.871 NotebookApp] http://localhost:8889/?token=2b4bdbaf2ea22cb55fa3aa
	dc0579bec6cb9424bdefe769cc
	[I 22:27:01.872 NotebookApp] Use Control-C to stop this server and shut down all
	 kernels (twice to skip confirmation).
	[C 22:27:01.891 NotebookApp]


# Mengerjakan berbagai source code yang ada di notebook Jupyter pada bab 3 di direktori praktik dan setiap satu source code menempati 1 file python: (Sebelum membuat skrip program meng-cpykan terlebuh dahulu folder data dari clone Pandas-Cookbook)
### 1. Untitled.ipynb

	import pandas as pd
	import numpy as np
	from IPython.display import display
	pd.options.display.max_columns = 50

	college = pd.read_csv('data/college.csv')

	college.head()

### Output:

	INSTNM	CITY	STABBR	HBCU	MENONLY	WOMENONLY	RELAFFIL	SATVRMID	SATMTMID	DISTANCEONLY	UGDS	UGDS_WHITE	UGDS_BLACK	UGDS_HISP	UGDS_ASIAN	UGDS_AIAN	UGDS_NHPI	UGDS_2MOR	UGDS_NRA	UGDS_UNKN	PPTUG_EF	CURROPER	PCTPELL	PCTFLOAN	UG25ABV	MD_EARN_WNE_P10	GRAD_DEBT_MDN_SUPP
	0	Alabama A & M University	Normal	AL	1.0	0.0	0.0	0	424.0	420.0	0.0	4206.0	0.0333	0.9353	0.0055	0.0019	0.0024	0.0019	0.0000	0.0059	0.0138	0.0656	1	0.7356	0.8284	0.1049	30300	33888
	1	University of Alabama at Birmingham	Birmingham	AL	0.0	0.0	0.0	0	570.0	565.0	0.0	11383.0	0.5922	0.2600	0.0283	0.0518	0.0022	0.0007	0.0368	0.0179	0.0100	0.2607	1	0.3460	0.5214	0.2422	39700	21941.5
	2	Amridge University	Montgomery	AL	0.0	0.0	0.0	1	NaN	NaN	1.0	291.0	0.2990	0.4192	0.0069	0.0034	0.0000	0.0000	0.0000	0.0000	0.2715	0.4536	1	0.6801	0.7795	0.8540	40100	23370
	3	University of Alabama in Huntsville	Huntsville	AL	0.0	0.0	0.0	0	595.0	590.0	0.0	5451.0	0.6988	0.1255	0.0382	0.0376	0.0143	0.0002	0.0172	0.0332	0.0350	0.2146	1	0.3072	0.4596	0.2640	45500	24097
	4	Alabama State University	Montgomery	AL	1.0	0.0	0.0	0	425.0	430.0	0.0	4811.0	0.0158	0.9208	0.0121	0.0019	0.0010	0.0006	0.0098	0.0243	0.0137	0.0892	1	0.7347	0.7554	0.1270	26600	33118.5


### Install package pandas-datareader
#### conda install -c anaconda pandas-datareader, package yang diinstall adalah :
The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    cffi-1.11.5                |   py36h74b6da3_1         201 KB  anaconda
    pyopenssl-18.0.0           |           py36_0          83 KB  anaconda
    win_inet_pton-1.0.1        |           py36_1           6 KB  anaconda
    pandas-datareader-0.7.0    |           py36_0         142 KB  anaconda
    pysocks-1.6.8              |           py36_0          23 KB  anaconda
    idna-2.7                   |           py36_0         132 KB  anaconda
    chardet-3.0.4              |           py36_1         209 KB  anaconda
    cryptography-2.4.1         |   py36h7a1dbc1_0         493 KB  anaconda
    urllib3-1.23               |           py36_0         153 KB  anaconda
    asn1crypto-0.24.0          |           py36_0         155 KB  anaconda
    libiconv-1.15              |       hc4a7105_7         654 KB  anaconda
    libxslt-1.1.32             |       hf6f1972_0         338 KB  anaconda
    requests-2.20.1            |           py36_0          85 KB  anaconda
    libxml2-2.9.8              |       hadb2253_1         2.2 MB  anaconda
    lxml-4.2.5                 |   py36hef2cd61_0         938 KB  anaconda
    pycparser-2.19             |           py36_0         174 KB  anaconda
    wrapt-1.10.11              |   py36hfa6e2cd_2          42 KB  anaconda
    ------------------------------------------------------------
                                           Total:         6.0 MB

## Memulai Data Analisis 
## Beberapa perintah :
### - head untuk membaca data set dan melihat lima baris pertama
### - shape untuk mendapatkan dimensi DataFrame.
### - info untuk melihat tipe data setiap kolom, jumlah nilai yang tidak hilang.
### - memory_usage untuk menemukan penggunaan memori setiap kolom.
### - astype untuk mengkonversi kolom menjadi integer berapa bit sesuai dengan kebutuhan.
### - Kolom STABBR adalah kandidat yang baik untuk dikonversi ke Kategorikal kurang dari satu persen nilainya unik.