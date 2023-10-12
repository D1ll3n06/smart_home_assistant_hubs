# Dillen Dela Cruz
#initializing how many parts are within one smart home assistant hub
case = 1
speaker = 2
microphone = 1
cpu = 1
dial = 1
cord = 1
total = 0

# initializing how many parts per package 
p_case = 2
p_speaker = 3
p_microphone = 5
p_cpu = 8
p_dial = 10
p_cord = 14

# initializing total to 0
total = 0

# initializing the variable to yes. This will make the loop continue until "again" does not equal "no"
again = "yes"

#calculates minimum package and remainder
while again == "yes":

  #ask how many stores the user will be calculating
  store = int(input('How many stores will you be inputting? '))

  #ask how many smart home assistant hubs per store. This will also get each quantity per store and add it to the variable "total"
  for num_store in range (store):
    print(f'Store Number {num_store + 1}', end='')
    amount = int(input(': '))
    total += amount
    
  print ('Materials needed for',total,"smart home assistant hubs is as follows:")
  
       
  #calculates remainder
  
  r_case = (total * case) % p_case
  r_speaker = (total * speaker) % p_speaker
  r_microphone = (total * microphone) % p_microphone
  r_cpu = (total * cpu) % p_cpu
  r_dial = (total * dial) % p_dial
  r_cord = (total * cord) % p_cord

 #calculates how the minimum number of package per part 
  if r_case > 0:
    m_case = int((total * case) / p_case) + 1
    print('          The minimum number of packages needed of Cases -', m_case)
  else:
    m_case = int((total * case) / p_case)
    print('          The minimum number of packages needed of Cases -', m_case)

  
  if r_speaker > 0:
    m_speaker = int((total * speaker) / p_speaker) + 1
    print('          The minimum number of packages needed of Speakers -', m_speaker)
  else:
    m_speaker = int((total * speaker) / p_speaker)
    print('          The minimum number of packages needed of Speakers -', m_speaker)

  
  if r_microphone > 0:
    m_microphone = int((total * microphone) / p_microphone) + 1
    print('          The minimum number of packages needed of Microphones -', m_microphone)
  else:
    m_microphone = int((total * microphone) / p_microphone)
    print('          The minimum number of packages needed of Microphones -', m_microphone)

  
  if r_cpu > 0:
    m_cpu = int((total * cpu) / p_cpu) + 1
    print('          The minimum number of packages needed of CPU Chips -', m_cpu)
  else:
    m_cpu = int((total * cpu) / p_cpu)
    print('          The minimum number of packages needed of CPU Chips -', m_cpu)


  if r_dial > 0:
    m_dial = int((total * dial) / p_dial) + 1
    print('          The minimum number of packages needed of Volume Dials -', m_dial)
  else:
    m_dial = int((total * dial) / p_dial)
    print('          The minimum number of packages needed of Volume Dials -', m_dial)

  
  if r_cord > 0:
    m_cord = int((total * cord) / p_cord) + 1
    print ('          The minimum number of packages needed of Power Cords -', m_cord)
  else:
    m_cord = int((total * cord) / p_cord)
    print ('          The minimum number of packages needed of Power Cords -', m_cord)


  #prints out remainder of each part 
  print ('          The number of Cases left over -', r_case)
  print ('          The number of Speakers left over -', r_speaker)
  print ('          The number of Microphones left over -', r_microphone)
  print ('          The number of CPU Chips left over -', r_cpu)
  print ('          The number of Volume Dials left over -', r_dial)
  print ('          The number of Power Cords left over -',r_cord)

  #makes sure that if there is another production run the total will reset to 0
  total = 0
  # ask user if they want to do another production run if they say "yes" the loop will start over and if "no" the loop will end
  print ("          'would you like another production run? yes or no': ", end='')
  again = input()




