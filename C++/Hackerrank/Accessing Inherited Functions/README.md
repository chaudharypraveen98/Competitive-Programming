## **[Accessing Inherited Functions](https://www.hackerrank.com/challenges/accessing-inherited-functions)** 
You are given three classes A, B and C. All three classes implement their own version of func.<br>In class A, func multiplies the value passed as a parameter by :<br><code>class A
{
    public:
        A(){
            callA = 0;
        }
    private:
        int callA;
        void inc(){
            callA++;
        }

    protected:
        void func(int & a)
        {
            a = a * 2;
            
        
    
         
             
        </code><br><br><code></code><br><br><code></code><br><br><code></code><br>You need to modify the class <em>D</em> and implement the function <code>update_val</code>  which sets <em>D</em>'s <em>val</em> to <em>new_val</em> by manipulating the value by only calling the <em>func</em> defined in classes <em>A, B</em> and <em>C</em>. <br><br><br>**Sample Input 0**<br><br><br>**Sample Output 0**<br><br><br>**Explanation 0**<br><br>