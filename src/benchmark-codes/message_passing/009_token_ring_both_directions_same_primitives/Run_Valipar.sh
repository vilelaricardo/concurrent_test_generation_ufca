javac *.java
for other in {0..9} # for pega todos os 10 conjuntos
do
mkdir suite_$other
valipar project --setup
./inst.sh
./Data_Tests/Data_Test_Suite$other.sh
valipar elem
for i in {0..9} #executa cada conjunto 10X
do
contador=`wc -l ./Data_Tests/Data_Test_Suite$other.sh | awk -F" " '{print $1" "}'`
x=0
while [[ x -ne $contador ]]; do # pega todos os dados de teste de cada conjunto
valipar exec -t $x -l 10000 
x=$((x+1))
done

done

valipar eval >> eval_file.txt #gerar a avaliação de cada conjunto
tar -czvf valipar.tar valipar/
mv valipar.tar suite_$other/
mv *.txt suite_$other/
mv *.log suite_$other/
rm -rf valipar/

done

