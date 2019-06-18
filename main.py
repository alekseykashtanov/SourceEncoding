from discrete_source import DiscreteSource

in_file = open("source_description.json", "r")

source = DiscreteSource(in_file)
print("Entropy: ", source.entropy())
