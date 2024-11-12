function oddOrEven(array) {
    if (array.length === 0) {
        array = [0];
    }
const total = array.reduce((accumulator,currentValue) => accumulator + currentValue,0);
if (total % 2 == 0){
    return "even"
}else{
    return "odd";
}
};
