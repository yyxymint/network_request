
python_file="tsp.py"

file_name="now_testing.txt"

if [ -f $file_name ]
then
    FILESIZE=$(wc -c "$file_name" | awk '{print $1}')
    echo "file size: $FILESIZE"
    
    
    
    if [ $FILESIZE -gt 500 ]
    then
        echo "large enough. Can't overwrite."
    else
        echo "Small txt. START"
        python -u $python_file > $file_name
            
    fi
    
else
    echo "NO such file. START"
    python -u $python_file > $file_name
    
fi
