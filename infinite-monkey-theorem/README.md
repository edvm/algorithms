# Infinite Monkey Theorem

The infinite monkey theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text, such as the complete works of William Shakespeare.

![Monkey typing](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Chimpanzee_seated_at_typewriter.jpg/220px-Chimpanzee_seated_at_typewriter.jpg)

Here goes my implementation!

## Usage

```python

In [4]: monkey.start_typing('hola', 100000)
Best match: hola
Iterations: 15092
Used 15.09 percent of given iterations
Score: 4
Time elapsed: 0.105 seconds
```

OR make your monkey more smart using an optimization of the above algorithm. Just use it like: 

```python

In [10]: monkey.start_typing('python', 1000, use_opt1=True)                                            
Best match: python
Iterations: 85
Used 8.50 percent of given iterations
Score: 6
Time elapsed: 0.001 seconds
```

OR Just call generate

```python
>>> import monkey
>>> monkey.generate('python', repeat=10000)
('ykthon', 4, 15082)
```

OR just call a smarter generate

```python
>>> monkey.generate('python', 1000, use_opt1=True)
>>> ('python', 6, 899)
```
