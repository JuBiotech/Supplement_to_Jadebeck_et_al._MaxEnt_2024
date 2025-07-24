FILES="*.fml"
for f in $FILES
do
  echo "Simulating $f file..."
  # take action on each file. $f store current file name
  jfwdsim -i "$f" -o /dev/null
done
