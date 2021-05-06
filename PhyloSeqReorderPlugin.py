import PyPluMA




class PhyloSeqReorderPlugin:
    def input(self, filename):
      self.parameters = dict()
      paramfile = open(filename, 'r')
      for line in paramfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()

      myfile = open(PyPluMA.prefix()+"/"+self.parameters["OTU"], 'r')
      samplefile =open(PyPluMA.prefix()+"/"+self.parameters["META"], 'r')
      #Idea: Zero out (don't remove) OTUs in less than 50% of a category set
      # Then once everything is done, remove those with zero over all samples
      # Make table first
      self.my_mat = []
      for line in myfile:
          contents = line.strip().split(',')
          self.my_mat.append(contents)


      samplefile.readline() # Header
      self.samples = []
      self.samples.append('\"\"')
      for line in samplefile:
          contents = line.strip().split(',')
          self.samples.append(contents[0])

    def run(self):
      header = self.my_mat[0] # First row
      self.indices = []
      for sample in self.samples:
         self.indices.append(header.index(sample))

    def output(self, filename):
      outputfile = open(filename, 'w')
      for row in self.my_mat:
          for i in range(0, len(row)):
              outputfile.write(row[self.indices[i]])
              if (i != len(row)-1):
                  outputfile.write(',')
              else:
                  outputfile.write('\n')

