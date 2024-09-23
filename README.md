# Opensource PDF toolkit

This project aims to provide pdf tooling that free of charge to users. The scripts work using bash. 

## Project Structure
- [Merging PDFs](#merging-pdfs)
- other tools coming soon... 

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Triples92/PDF_tools
    ```

2. **Change directory to match user's workspace:**
  <br> Replace the directory link in the <code>source</code> and <code>python</code> lines in <code>merge_pdf.sh</code>to match the directory your cloned repository is in. 

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Merging PDFs

### Usage

#### Using `merge_pdf.sh`

To merge PDF files using the `merge_pdf.sh` script, simply run the script as below. You must start the first variable with the file name and ensure that you add the extension. See example below:

 **Run the `merge_pdf.sh`script:**
 <br>
    ```
    ./merge_pdf.sh <output-file> <input-file-1> <input-file-2> <input-file-3> <input-file-4> <input-file-5>
    ```

    Example:

    ```
    ./merge_pdf.sh merged.pdf file1.pdf file2.pdf file3.pdf file4.pdf file5.pdf
    ```

    This will merge the specified input PDF files into a single output file named `merged.pdf`.

