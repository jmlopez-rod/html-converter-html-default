Lexor Language: HTML to HTML default style converter
====================================================

Evaluates python instructions.

## Example

Suppose we have the file `example.html`

```html
<html>
<?python include('header.html')?>
<body>
<table>
<tr><th>x</th><th>f(x)</th></tr>
<?py
def f(x):
  return x*x

row = '<tr><td>{0}</td><td>{1}</td></tr>'
for i in xrange(10):
    print row.format(i, f(i))
?>
</table>
</body>
</html>

```

and `header.html`

```html
<header>
<!-- Include scripts and css stuff here? -->
</header>
```

To be able to use lexor with this converter style you will need

- https://github.com/jmlopez-rod/html-parser-default
- https://github.com/jmlopez-rod/html-writer-default

After running the command

    $ lexor example.html to html[_:html._@add_block=[tr]]

we get the following output

```html
<html>
<header>
<!-- Include scripts and css stuff here? -->
</header>
<body>
<table>
<tr><th>x</th><th>f(x)</th></tr>
<tr><td>0</td><td>0</td></tr>
<tr><td>1</td><td>1</td></tr>
<tr><td>2</td><td>4</td></tr>
<tr><td>3</td><td>9</td></tr>
<tr><td>4</td><td>16</td></tr>
<tr><td>5</td><td>25</td></tr>
<tr><td>6</td><td>36</td></tr>
<tr><td>7</td><td>49</td></tr>
<tr><td>8</td><td>64</td></tr>
<tr><td>9</td><td>81</td></tr>
</table>
</body>
</html>
```
