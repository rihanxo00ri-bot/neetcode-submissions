class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
      
    stack=[]
    for i in tokens:
        if i in '+-*/':
            b = stack.pop()
            a =stack.pop()

            if i =='+':
                c=a+b
                stack.append(c)

            elif i=='-':
              c=a-b
              stack.append(c)
            elif i=='*':
              c=a*b
              stack.append(c)

            else:
              c=int(a/b)
              stack.append(c)
                
        else:
            val=int(i)
            stack.append(val)

    return stack[0]    