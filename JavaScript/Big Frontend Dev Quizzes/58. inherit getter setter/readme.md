## [58. inherit getter setter](https://bigfrontend.dev/quiz/inherit-getter-setter)

### Approach
1. Here we have a global val and then three classes. A has both setter and getter defined. B extends A without any overriding. C extends A with get foo() overridden.
2. Note that since we have not used this keyword while setting, it'll actually update the outer variable val
3. So, when we create a new object b, the value of val is 0 and hence b.foo returns 0. Then we do b.foo = 1 which means val also gets updated to 1 and hence it prints 1 next.
4. Next we create a new object c, c.foo returns 1 (from above). However, c.foo = 2 will not update val as there is no setter defined hence val remains 1 thus printing 1 for both c.foo and b.foo Apparently, when we override the get method, it appears that the set method must also be overridden, otherwise undefined is returned See this