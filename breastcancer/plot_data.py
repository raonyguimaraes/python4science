
import matplotlib.pyplot as plt

vcffile = open('brca1.vcf','r')

colors = {
	'A':'red',
	'C':'yellow',
	'G':'green',
	'T':'blue',
}

genotypes_dict = {
	'0|0':'white',
	'0|1':'blue',
	'1|0':'blue',
	'1|1':'red',
	'0|2':'blue',
	'2|0':'blue',
	'2|2':'red',
	'2|1':'red',
	'1|2':'red',
}

individuals_genotypes = {}
#example
#individuals_genotypes['NA2647']['182635271'] = colors['']

#get individuals names
count = 0

for line in vcffile:
	if line.startswith('#CHROM'):
		individuals = line.strip().split('\t')[9:]
		# for individual in individuals:
		# 	individuals_genotypes[individual] = {}
	if not line.startswith('#'):
		print count
		count += 1
		row = line.strip().split('\t')
		pos = row[1]
		genotypes = row[9:]
		# if pos == '41196363':
		for k, individual in enumerate(individuals):
			# print k, individual
			# individuals_genotypes[individual][pos] = genotypes_dict[genotypes[k]]
			# print individual, color, k, pos
			 # color="blue", linewidth=1.0, linestyle="-"
			if genotypes[k] != '0|0':
				color = genotypes_dict[genotypes[k]]
				# x_indexes = k
				plt.scatter(k, pos, c=color, marker="|", faceted=False, s=100)
				# print k, pos, genotypes[k]
#plot per individuals
# for individual in individuals:
# 	plt.scatter(individuals[individual]['x_indexes'], individuals[individual]['y_indexes'], c=color, marker="|")

# plt.ylim([41196363,41277492])
# plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()


# from numpy.random import rand


# for color in ['red', 'green', 'blue']:
#     n = 750
#     x, y = rand(2, n)
#     scale = 200.0 * rand(n)
#     plt.scatter(x, y, c=color, s=scale, label=color,
#                 alpha=0.3, edgecolors='none')

plt.legend()
plt.grid(True)

plt.show()
