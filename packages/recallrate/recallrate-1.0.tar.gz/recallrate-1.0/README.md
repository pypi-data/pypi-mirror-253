method of application:
    from recall.main_module import process_files

    barcode_file_path = 'barcodes batch-input.txt'
    species_folder_path = 'test sequences'
    output_file_path = 'output.xlsx'

    process_files(barcode_file_path, species_folder_path, output_file_path)

Remark: test sequences are folders containing original files, barcodes batch-input.txt contain all target sequences, and the results are output to output.xlsx
//////
The algorithm was as follows: average species nucleic acid level recall: the sum of the nucleic acid of the same site of all species and single species of barcode fragment/the total length of barcode fragment/the number of species; Average species-level recall: when the recall rate of nucleic acid level of a single species was more than 90%, the recall rate of nucleic acid level of a single species was directly 100%, otherwise it was 0%. After that, the sum (single species nucleic acid level recall)/number of species was added.
