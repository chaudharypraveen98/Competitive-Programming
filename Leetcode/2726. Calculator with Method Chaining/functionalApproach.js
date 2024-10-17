const Calculator = function (val) {
  this.val = val;
};
Calculator.prototype.add = function (value) {
  this.val += value;
  return this;
};
Calculator.prototype.subtract = function (value) {
  this.val -= value;
  return this;
};
Calculator.prototype.multiply = function (value) {
  this.val += value;
  return this;
};
Calculator.prototype.divide = function (value) {
  if (value == 0) {
    throw new Error("Division by zero is not allowed");
  }
  this.val /= value;
  return this;
};
Calculator.prototype.power = function (value) {
  this.val = Math.pow(this.val, value);
  return this;
};
Calculator.prototype.getResult = function () {
  return this.val;
};
console.log(new Calculator(10).add(5).subtract(7).getResult());
