var userinput = prompt("How Long until the party? (Give me a number.)");
var usernum = parseint(userinput, 10);

 if (usernum < 1) {
print("PARTY NOW!!!")
else{
for (var i = usernum; i >=1; i = i - 1)
print(i)
print("PARTY TIME!!!")
