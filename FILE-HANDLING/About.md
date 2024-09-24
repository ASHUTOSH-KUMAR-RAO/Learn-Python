# File I/O :-

- it can be used to perform operation on a file (read and write data)

## Types of Files :-

- Text Files :- .txt, .docx, .log etc (iska mtlb hota hai ki iske andar data Caracter ke form mein store hota hai ✅)

- Binary Files :- .mp4, .mov, .png, .jpeg etc (iska mtlb hota hai ki jo kuch bhi data text file ke andar nhi store hota hai wo data hai binary files mein store hota hai 🐻‍❄️ )

- Notes :- Data Chahe kuch bhi but wo system andar "Bite" ke form mein store hota hai means (0,1).

### File Open :-

##  (Read Mode) 

- we have open a file before read and write

```python

: Synatx :-

f = open("File_name","mode")
data = f.read()
data = f.readline() # Ye line by Line Read krte hai saab data ko
print(data)
print(type(data))

- file name = ashu.txt,awash.docx etc
- mode - r:read mode , w: write mode

```

## Write Mode :-

**Note** :- yedi kabhi hum aise file mein kuch likh rehe hai jo file exist hi nhi krti hai to iss case mein , python ek new file create kr deta hai usi name ka 👍

truncate :- iska mtlb hota hai ki file dlt ho jana

```python

f = open("File path /Name","w")

f = open("file path/Name","a")  # means append krna

f.write("Anything Write here")

f.close()

```

##  Read and Write mode :-

**Note** :- aur isme begning position  se update hona shuru hota hai .

```python

f = open("file path","r+")
f.write("write any thing here")
print(f.read()) # aur saab kaam krne ke baad file ko read bhi kr sekte hai 
f.close()
```

***Important Battein***

- r = for reading

- r+=  opens for reading and writing (cannot truncate a file)

- w = for writing

- w+ = for writing and reading (can truncate a file)

- rb = for reading a binary file. The file pointer is placed at the beginning of the file.

- rb+ = reading or writing a binary file

- wb+ = writing a binary file

- a+ = opens for appending

- ab+ = Opens a file for both appending and reading in binary. The file pointer is at the end of the file if the file exists. The file opens in the append mode.

- x = open for exclusive creation, failing if the file already exists (Python 3)