# Importing modules
import time
from storage import per_id

i = per_id
# Loop forever
while True:
  i += 1
  # Input
  name = input("What is your name? ")
  age = input("What is your age? ")
  # Set current name (cname)
  cname = name
  # Make the name sentence-cased
  name = name[0].upper() + cname[1:]
  
  # Make person file
  wr = open(name.lower() + ".py", "w")
  # Write to person file
  wr.write("# AUTO-GENERATED\n# person number: " + str(i) + "\nimport os\nname = \"" + name + "\"\nage = " + age + "\nif input(\"Are you sure to delete " + name.lower() + ".py? (y to delete) \") == \"y\":\n\tst = open(\"storage.py\",\"w\")\n\tst.write(\"per_id = \" + str(" + str(i) + "-1))\n\tst.close()\n\tlog = open(\"perlog.log\",\"a\")\n\tlog.write(\"Deleted " + name + "\\n\")\n\tlog.close()\n\tos.remove(\"" + name.lower() + ".py\")\nelse:\n\tprint(\"Cancelled\")")
  # What the person file looks like:
  """
  # AUTO-GENERATED
  # person number: i
  import os
  name = "Name"
  age = Age
  if input("Are you sure to delete name.py? (y to delete) ") == "y":
    st = open("storage.py", "w")
    st.write("per_id = " + str(i-1))
    st.close()
    log = open("perlog.log","a")
    log.write("Deleted Name\n")
    log.close()
    os.remove("name.py")
  else:
    print("Cancelled")
  """
  # Close the person file
  wr.close()
  print("Hi, {}! Your age is {}, You're order {}".format(name,age,i))
  time.sleep(3)
  # Open storage.py
  st = open("storage.py", "w")
  # Write to storage.py
  st.write("per_id = " + str(i))
  # Close storage.py
  st.close()
  # Open log file (perlog.log)
  log = open("perlog.log", "a")
  # Append to log file
  log.write("[" + str(i) + "] " + name + ", age: " + age + "\n")
  # Close the log file
  log.close()
