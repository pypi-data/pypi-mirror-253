import os
import pandas as pd

def read_sequences_from_file(file_path):
    """从文件中读取序列，忽略带有 '>' 的行"""
    with open(file_path, 'r') as file:
        return [line.strip().replace('-', 'N') for line in file.readlines() if line.strip() and '>' not in line]

def calculate_specificity(barcode_sequence, species_sequences):
    total_nucleotide_diffs = 0
    total_species_specificity = 0
    barcode_length = len(barcode_sequence)
    num_species = len(species_sequences)
    specificity_cases = {n_diffs: 0 for n_diffs in range(1, 11)}

    for species_seq in species_sequences:
        # 检查物种核酸序列长度
        if len(species_seq) < barcode_length:
            continue  # 如果物种核酸序列短于条形码片段，则跳过

        nucleotide_diffs = sum(1 for i in range(barcode_length) if species_seq[i] != barcode_sequence[i])
        total_nucleotide_diffs += nucleotide_diffs

        # 计算不同差异数下的特异度
        for n_diffs in specificity_cases:
            specificity_cases[n_diffs] += 100 if nucleotide_diffs >= n_diffs else 0

    average_nucleotide_specificity = (total_nucleotide_diffs / barcode_length / num_species) * 100
    average_specificity_cases = {n_diffs: (specificity / num_species) for n_diffs, specificity in specificity_cases.items()}

    return round(average_nucleotide_specificity, 4), average_specificity_cases

def process_files(barcode_file_path, species_folder_path, output_excel_path):
    """处理所有文件并导出结果到Excel文件"""
    barcodes = read_sequences_from_file(barcode_file_path)
    results = []

    for i, barcode in enumerate(barcodes):
        species_file_name = f"modified_sequences_{i+1}.txt"
        species_file_path = os.path.join(species_folder_path, species_file_name)

        # 检查文件是否存在
        if not os.path.exists(species_file_path):
            continue  # 如果文件不存在，则跳过

        species_sequences = read_sequences_from_file(species_file_path)
        avg_nuc_spec, avg_specificity_cases = calculate_specificity(barcode, species_sequences)

        result = {
            'Barcode': barcode,
            'Species File': species_file_name,
            'Average Nucleotide Specificity': avg_nuc_spec
        }
        result.update({f'Avg Specificity (Diff >= {n_diffs})': spec for n_diffs, spec in avg_specificity_cases.items()})
        results.append(result)

    df = pd.DataFrame(results)
    df.to_excel(output_excel_path, index=False)