echo "Running tests for TextNode..."
python3 -m unittest discover -s src/ -p "test_textnode.py"
echo '-------------------------------'
echo "Running tests for HTMLNode..."
python3 -m unittest discover -s src/ -p "test_htmlnode.py"
echo '-------------------------------'
echo "Running tests for LeafNode..."
python3 -m unittest discover -s src/ -p "test_leafnode.py"
echo '-------------------------------'
echo "All tests completed."