from person import Person
import random
import csv

names_db_file = "yob2016.txt"
surnames_db_file = "surnames.txt"
names_count = 50

class Town(object):
  def __init__(self):
    self.male_names = []
    self.male_weights = []
    self.female_names = []
    self.female_weights = []
    self.surnames = []
    self.surname_weights = []
    self.import_name_db(names_db_file, surnames_db_file)

  def import_name_db(self, names_db_file, surnames_db_file):
    total_female = 0
    total_male = 0
    for row in csv.reader(open(names_db_file, 'r')):
      done = 0
      if len(self.male_names) < names_count:
        if row[1] == "M":
          self.male_names.append(row[0])
          self.male_weights.append(int(row[2]))
      else:
        done += 1
      if len(self.female_names) < names_count:
        if row[1] == "F":
          self.female_names.append(row[0])
          self.female_weights.append(int(row[2]))
      else:
        done += 1
      if done == 2:
        break
    for row in csv.reader(open(surnames_db_file, 'r')):
      self.surnames.append(row[0])
      self.surname_weights.append(int(row[1]))
      
  def name_gen(self, gender):
    if (gender == 'm'):
      return (random.choices(self.male_names, self.male_weights)[0], random.choices(self.surnames, self.surname_weights)[0])
    else:
      return (random.choices(self.female_names, self.female_weights)[0], random.choices(self.surnames, self.surname_weights)[0])


    