FILES="crown*/*.fml"
for f in $FILES
do
  #echo "Simulating $f file..."
  # take action on each file. $f store current file name
  #echo "~/repos/_x3cflux/apps/jfwdsim -i "$f" -o /dev/null > /dev/null 2> /dev/null"
  ~/repos/_x3cflux/apps/jfwdsim -i "$f" -o /dev/null > /dev/null 2> /dev/null
  echo "$? ($f)"
done
