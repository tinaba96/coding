class MultiStack:
  def __init__(self, stacksize):
    self.numstacks = 3
    self.array = [0]*(stacksize*self.numstacks)
    self.sizes = [0]*self.numstacks
    self.stacksize = stacksize

  def Push(self, item, stacknum):
    if self.IsFull(stacknum):
      raise Exception('Stack is full')
    self.sizes[stacknum] += 1
    self.array[self.IndexOfTop(stacknum)] = item

  def Pop(self, stacknum):
    if self.IsEmpty(stacknum):
      raise Exception('Stack is Empty')
    value = self.array[self.IndexOfTop(stacknum)]
    # self.array[self.IndexOfTop(stacknum)] = 0
#上の一文はいらないかも
    self.sizes[stacknum] -= 1
    return value

  def Peek(self, stacknum):
    if self.IsEmpty(stacknum):
      raise Exception('Stack is empty')
    return self.array[self.IndexOfTop(stacknum)]

  def IsEmpty(self, stacknum):
    return self.sizes[stacknum] == 0

  def IsFull(self, stacknum):
    return self.sizes[stacknum] == self.stacksize

  def IndexOfTop(self, stacknum):
    offset = stacknum*self.stacksize
    return offset + self.sizes[stacknum]-1

def ThreeInOne():
  newstack = MultiStack(2)
  print(newstack.IsEmpty(1))
  newstack.Push(3, 1)
  print('array',newstack.array)
  print('size',newstack.sizes)
  print('peek',newstack.Peek(1))
  print(newstack.IsEmpty(1))
  newstack.Push(2, 1)
  print('array',newstack.array)
  print('peek',newstack.Peek(1))
  print('peek',newstack.Peek(1))
  #newstack.Push(3, 1)
  print('peek',newstack.Peek(1))
  print('array',newstack.array)
  print('size',newstack.sizes)

  print('pop',newstack.Pop(1))
  print('array',newstack.array)

  print('pop',newstack.Pop(1))
  print('array',newstack.array)
  '''
  newstack.Push(3, 1)
  print(newstack.array)
  print(newstack.sizes)
  #full
  '''

ThreeInOne()

