
echo '************************************************************************'
echo "Running tests for TextNode..."
python3 -m unittest discover -s src/ -p "test_textnode.py"
echo '************************************************************************'
echo ""
echo "Running tests for HTMLNode..."
python3 -m unittest discover -s src/ -p "test_htmlnode.py"
echo '************************************************************************'
echo ""
echo "Running tests for LeafNode..."
python3 -m unittest discover -s src/ -p "test_leafnode.py"
echo '************************************************************************'
echo ""
echo "Running tests for ParentNode..."
python3 -m unittest discover -s src/ -p "test_parentnode.py"
echo '************************************************************************'
echo ""
echo "Running tests for inline functions..."
python3 -m unittest discover -s src/ -p "test_inline.py"
echo '************************************************************************'
echo ""
echo "Running tests for block functions..."
python3 -m unittest discover -s src/ -p "test_block.py"
echo '************************************************************************'
echo ""
echo "Running tests for main functions..."
python3 -m unittest discover -s src/ -p "test_main.py"
echo '************************************************************************'
echo ""
echo "All tests completed."