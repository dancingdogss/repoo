
function staircase(n){
    if(n<0||n>100){
        return "Unable to generate staircase";
    }
    let steps="";
    for ( let i =n;i>0;i--){
        const whiteSpaces = generateCharString(i-1," ");
        const hashtags = generateCharString(n-i+1,"#");
        steps= steps + whiteSpaces + hashtags+"\n";
    }
//    const lastHashtagsRow= generateHashtags(n,"#");
//  steps= steps+lastHashtagsRow+"\n";
    return steps;
}

function generateCharString(n, charValue){
    let result="";
    for(let i=0;i<n;i++)
    {
        result = result+charValue;

    }
    return result;
}

const stair2=staircase(10);

console.log(stair2);


//calc of xnxs/diauri

             // v //

function calcProfXnx(X){
    let sum =0;
    if(X===150)
    {
        
        return sum+X;
        
        
    }
    else{
        if(X===100)
        {
            return sum + X;
        }
    }
}

const pret1 = calcProfXnx(150);
const pret2 = calcProfXnx(100);

console.log("Xnx ->> Profit in cazul in care se vinde la folie",pret1);
console.log("Xnx ->> Profit in cazul in care se vinde la box,",pret2);



function calcProfDia(X){
    let sum =0;
    if(X===150)
    {
        
        return sum+X;
        
        
    }
    else{
        if(X===100)
        {
            return sum + X;
        }
    }
}

const pret3 = calcProfDia(150);
const pret4 = calcProfDia(100);

console.log("Dia -->> Profit in cazul in care se vinde la folie",pret3);
console.log("Dia -->> Profit in cazul in care se vinde la box,",pret4);



const MedieXan = (pret1+pret2)/2;
const MedieDia = (pret3+pret4)/2;
console.log("Media pentru xanuri -->>",MedieXan);
console.log("Media pentru diauri -->>",MedieDia);


const total = pret1+pret2+pret3+pret4;
const medieTotal = MedieDia+MedieXan;

console.log("Total profit is "+total);
console.log("Totalmedie profit is " + medieTotal);


let debts=[];



function liabilities(ppl,csh,tme){
    let person=[ppl];
    let cash=[csh];
    let time=[tme]
    for(let i =0;i<person.length;i++){
        let obj={};

        obj['Person:']=person[i];
        obj['Cash: ']=cash[i];
        obj['Time: ']=time[i];
        debts.push(obj);
    
    }

}



liabilities("Gasdasdi2ghhi","200","9-10nov/22");

console.log(debts);









// ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo