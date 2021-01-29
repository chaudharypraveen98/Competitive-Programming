## **[Java Method Overriding](https://www.hackerrank.com/challenges/java-method-overriding)** 
When a subclass inherits from a superclass, it also inherits its methods; however, it can also override the superclass methods (as well as declare and implement new ones). Consider the following Sports class:<br><code>class Sports{
    String getName(){
        return "Generic Sports";
    }
    void getNumberOfTeamMembers(){
        System.out.println( "Each team has n players in " + getName() );
    }
}</code><br>Next, we create a Soccer class that inherits from the Sports class. We can override the getName method and return a different, subclass-specific string:<br><code></code><br><strong>Note:</strong> When overriding a method, you should precede it with the <code>@Override</code> annotation. The parameter(s) and return type of an overridden method must be exactly the same as those of the method inherited from the supertype. <br><br>