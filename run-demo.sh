# To test the sample:
cd tests/sample
sigal build
cd ../../
cp ./hp-bridge.html ./tests/sample/_build
aws s3 sync ./tests/sample/_build/ s3://[insert-your-bucket-here] --delete
