
import matplotlib.pyplot as plt

vcffile = open('brca1.vcf','r')


fig = plt.figure(frameon = False)
fig.set_size_inches(16, 8)

colors = {
	'A':'red',
	'C':'yellow',
	'G':'green',
	'T':'blue',
}

genotypes_dict = {
	'0|0':'green',
	'0|1':'yellow',
	'1|0':'yellow',
	'0|2':'yellow',
	'2|0':'yellow',
	'1|1':'black',
	'2|2':'black',
	'2|1':'black',
	'1|2':'black',
}

individuals_genotypes = {}
#example
#individuals_genotypes['NA2647']['182635271'] = colors['']

#get individuals names
count = 0

snps = [
'rs1799950',
'rs4986850',
'rs2227945',
'rs16942',
'rs1799966',
]

causal_snps = [
'rs80357713',
'rs28897696',
'rs55770810',
'rs76171189',
'rs80357906',
]

for line in vcffile:
	if line.startswith('#CHROM'):
		individuals = line.strip().split('\t')[9:]
		for individual in individuals:
			individuals_genotypes[individual] = {}
	if not line.startswith('#'):
		# print count
		count += 1
		row = line.strip().split('\t')
		pos = int(row[1])
		snp = row[2]
		genotypes = row[9:]
		# if pos == '41196363':
		if snp in snps:
			for k, individual in enumerate(individuals):
				# print k, individual
				# individuals_genotypes[individual][pos] = genotypes_dict[genotypes[k]]
				# print individual, color, k, pos
				 # color="blue", linewidth=1.0, linestyle="-"
				if genotypes[k] != '0|0':
					color = genotypes_dict[genotypes[k]]
					individuals_genotypes[individual][pos] = color
					# x_indexes = k
					# plt.scatter(k, pos, c=color, marker="|", faceted=False, s=100)
					# print k, pos, genotypes[k]
#plot per individuals
space = 1
for k, individual in enumerate(individuals):
	# print 'keys', individuals[individual]
	k = k*1000
	mask = [k for n in individuals_genotypes[individual]]
	# print test
	# die()
	colors = individuals_genotypes[individual].values()
	plt.scatter(individuals_genotypes[individual].keys(), mask, c=colors, marker="|", s=10)
	# if k == 5:
	# 	break

# for color in ['red', 'green', 'blue']:
#     n = 750
#     x, y = rand(2, n)
#     scale = 200.0 * rand(n)
#     plt.scatter(x, y, c=color, s=scale, label=color,
#                 alpha=0.3, edgecolors='none')

plt.legend()
plt.grid(True)

plt.savefig('brca_highresolution.png', dpi = 200)


# plt.show()
