# font-size stands for how big or small is font on uor page
# color stands for changing a color of text
# font-style stands for the style of your font(for example italic)
# text-transform transforms our text into uppercase, lowercase etc.
# background-color stand for a colo of the background area(of text, body, entire webpage etc.)
# * to select all information from the page and change everything
""" /* p {
    font-size: 20px;
    color: purple;
}
body {
    font-size: 22px;
}
.gray {
    color: gray;
}
#third {
    font-style: italic;
}
h2, h3 {
    color: blanchedalmond;
}
.highlight {
    text-transform: uppercase;
    background-color: gold;
} */
/* body {
    font-size: 22px;
    font-family: 'Times New Roman', Times, serif;
    line-height: 1.5;
    background-color: peru;
    color: olive;
} */ 
/* 
#Box Styling
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.container {
    border: 10px double skyblue;
    font-size: 1.5rem;
    margin: 1.5em;
    padding: 1.5em;
    outline: 5px solid pink;
    outline-offset: -20px;
}
.circle {
    margin: 3rem auto;
    background-color: gold;
    width: 100px;
    height: 100px;
    border: 2px solid black;
    border-radius: 50px;
    outline: 2px solid pink;
    outline-offset: 0.25rem;
} 
*/
/* input, button {
    font-size: inherit;
} */
/* p {
   /*  line-height: 1.5; */
    /* letter-spacing: 0.1em;
    word-spacing: 0.25em; */
   /*  font-weight: 700;
    font-style: italic; */
/* a {
   color: #000;
}
a:visited {
    color: red;
}
a:hover a:focus {
    color: aquamarine;
}
a:active {
    color: firebrick;
} */

/* ol {
    list-style-type: upper-latin;
}
ul {
    text-align: center;
    line-height: 1.6;
    list-style:square url('../img/checkmark.png') inside;
}

ul ::marker {
    color: #000;
    font-family: fantasy;
    font-size: 1em;
    content: 'Only 5$>> ';
} */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    margin: 0.5rem;
    font-size: 1.5rem;
    text-align: center;
    font-family: "Oswald", sans-serif;
    font-optical-sizing: auto;
    font-weight: 500;
    font-style: normal
}

nav{
    border: 2px solid #333;
    border-radius: 2rem;
    margin: 0 auto 1rem;
    width: 600px;
    font-size: 3rem;
    line-height: 7rem;
}

h2 {
    padding: 1rem;
    background-color: gold;
    border-radius: 2rem 2rem 0 0;
}

ul {
    list-style-type: none;
}

li {
    border-top: 1px solid #333;
}

li a {
    display: block;
}

li a,
li a:visited{
    text-decoration: none;
    color: darkblue;
}

li a:hover,
li a:focus {
    background: #333;
    color: whitesmoke;
    cursor: pointer;
}

li:last-child a {
    border-radius: 0 0 2rem 2rem;
}
#
/* * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    font-family: "Oswald", sans-serif;
    font-optical-sizing: auto;
    font-weight: 500;
    font-style: normal;
    font-size: 2rem;
} */

/* p {
    background-color: lightgray;
}

.opposite {
    display: inline-block;
    background-color: gold;
    color: whitesmoke;
    padding: 4rem;
} */

/* ul {
    list-style-type: none;
    padding: 0.5rem;
    text-align: right;
    background-color: lightgray;
    margin: 0;
}

li {
    display: inline-block;
    margin-inline: 0.5rem;
}

li a {
    color: darkmagenta;
}

li a:visited {
    color: goldenrod;
}

li a:hover, 
li a:focus {
    color: tomato;
} */
# 
body {
    font-family: "Oswald", sans-serif;
    font-optical-sizing: auto;
    font-weight: 500;
    font-style: normal;
    font-size: 2rem;
}
.block {
    width: 30vw;
    height: 30vw;
    background-color: #000;
    color: white;
    padding: 1.5rem;
}

.left {
    float: left;
    margin-right: 1rem;
}
.right {
    float: right;
    margin-left: 1rem;
}

.clear {
    clear: both;
}

section {
    background-color: bisque;
    border: 1px solid #333;
    padding: 1rem;
    display: flow-root;
}
#
/* .columns {
     column-count: 4;
    column-width: 250px;
    columns: 4 250px;
    column-rule: 3px solid black;
}

.columns p {
    margin-top: 0;
}

.columns h2 {
    margin-top: 0;
    background-color: #333;
    color: whitesmoke;
    padding: 1rem;
    break-inside: avoid;
}

.columns .quote {
    margin-top: 2rem;
    font-size: 2rem;
    text-align: center;
    color: #333;
    column-span: all;
}

.nowraped {
    white-space: nowrap;
} 
#
.outer-container {
    border: 3px dashed black;
    width: 75vw;
    height: 85vh;
    margin: 40px auto;
}

.inner-container {
    border: 2px solid darkblue;
    width: 40vw;
    height: 50vh;
    margin: 200px auto;
}

.box {
    width: 150px;
    height: 150px;
    color: #fff;
    padding: 1rem;
}

.absolute {
    background-color: gold;
    position: absolute;
    top: 0;
    left: 0;
}

.relative {
    background-color: olive;
    position: relative;
    top: 300px;
    left: 100px;
}

.fixed {
    background-color: darkorchid;
    position: fixed;
    top: 100px;
}

.sticky {
    background-color: black;
    position: sticky;
    top: 0;
}

section {
    height: 100vh;
}

.blue {
    background-color: blue;
}
.red {
    background-color: red;
}
.green {
    background-color: green;
}

header, footer {
    color: #fff;
    text-align: center;
    height: 100px;
    font-size: 5rem;
}

header {
    position: sticky;
    top: 0;
}
footer {
    background-color: #000;
    position: fixed;
    bottom: 0;
}

a:visited {
    color: #fff;
}

.social {
    background-color: royalblue;
    color: #fff;
    font-size: inherit;
    padding: 1rem;
    position: fixed;
    top: 30%;
    left: 0;
}
#
/* * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    font-family: "Oswald", sans-serif;
    font-optical-sizing: auto;
    font-weight: 500;
    font-style: normal;
    font-size: 2rem;
    min-height: 200vh;
    padding: 20px;
}

.container {
    max-width: 800px;
    min-height: 400px;
    margin-inline: auto;
    border: 1px solid #000;
    display: flex;
    gap: 1rem;
    justify-content: center;
    align-items: center;
    flex-flow: row-reverse wrap;
    align-content: space-evenly;
}

.box {
    min-width: 100px
    height: 100px;
    background-color: #000;
    color: #fff;
    font-size: 3rem;
    padding: 0.5rem;

    display: flex;
    justify-content: center;
    align-items: center;

    flex: 1 1 250px;
}

.box:nth-child(2) {
    flex: 2 2 250px;
    order: 0;
} """