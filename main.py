import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


#sample gene data
genes = ["BRCA1", "TP53", "EGFR", "BRCA1", "TP53", "MYC"]

#count genes
gene_count = {}

for gene in genes:
    if gene in gene_count:
        gene_count[gene] += 1
    else:
        gene_count[gene] = 1

#separate keys and values for plotting
genes_names = list(gene_count.keys())
counts = list(gene_count.values())

#Print report
print("Gene Frequency Report")
for gene, count in gene_count.items():
    print(f"{gene}: {count}")


#plotting
plt.figure(figsize=(8,5))

#creat alternating colors
colors = ["#6C5CE7" if i % 2 == 0 else "#00b894" for i in range(len(genes_names))]

plt.bar(genes_names, counts, color=colors)

plt.title("Gene Frequency Distribution", fontsize=14)
plt.xlabel("Genes", fontsize=12)
plt.ylabel("Count", fontsize=12)

#grid
plt.grid(axis='y', linestyle='--', alpha=0.5)

for i in range(len(counts)):
    plt.text(i, counts[i]+0.05, str(counts[i]), ha='center', fontsize=11)

plt.tight_layout()
plt.show()
