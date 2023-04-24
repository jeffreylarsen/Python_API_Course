from fastapi import Response, status, HTTPException, Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. import models, schemas, Oauth2
from typing import List, Optional
from ..database import get_db

router = APIRouter(
    prefix="/3DEffect",
    tags=["3DEffect"]
)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fun 3D Effect</title>
    <!-- <link rel="stylesheet" href="styles.css"> -->
    <style>
        :root {
    --pink: hsl(338, 70%, 55%);
    --teal: hsl(183, 70%, 62%);
    --white: hsl(334. 7%, 95%);
}

*,
*::before,
*::after {
    box-sizing: border-box;
}

body {
    background: hsl(224, 32%, 12%);
    background-image: conic-gradient(
        from 0deg at 50\% 50\%,
        blue,
        purple,
        purple,
        blue
    );
    background-blend-mode: multiply;
    color: white;
    min-block-size: 100vh;
    display: grid;
    place-items: center;
}


pre {

    --selector: var(--pink);
    --property: var(--teal);
    --punctuation: var(--white);

    font-size: 1.5rem;
    font-weight: bold;
    background: hsl(222, 45%, 7%);
    padding: 2rem;
    border-radius: 1rem;

    position: relative;

    transform-style: preserve-3d;
    transform: 
        perspective(5000px)
        rotateX(var(--rotateY))
        rotatey(var(--rotateX))
        ;

}

.selector {
    color: var(--selector);
}

.property {
    color: var(--property);
}

.punctuation {
    color: var(--punctuation);
}

.property + .punctuation {
    color: var(--property);
}

pre > * {
    text-shadow: 0 0 0.3rem currentColor;
}

pre::before,
pre::after {
    content: "";
    position: absolute;
    border-radius: inherit;
}

pre::before {
    inset: 0.75rem;
    background: blue;
    transform: translateZ(-49px);
    /* glow */
    background: blue;
    filter: blur(50px);
    opacity: 0.6;
    /* shadow */
    /* background: black;
    filter: blur(15px);
    opacity: 0.7; */
}

pre::after {
    inset: -1rem;
    background: linear-gradient(-45deg, red, blue);
    transform: translateZ(-50px);
}
    </style>
</head>
<body>
    <pre cont class="language-javascript" tabindex="0"><code class="language-css"><span class="token selector">.jeffrey</span> <span class="token punctuation">{</span>
        <span class="token property">display</span><span class="token punctuation">:</span> flex<span class="token punctuation">;</span>
        <span class="token property">border-radius</span><span class="token punctuation">:</span> 42.0rem
    <span class="token punctuation">}</span></code></pre>
</body>
<!-- <script src="index.js"></script> -->
<script>
    const pre = document.querySelector('pre');

document.addEventListener('mousemove', (event) => {
    rotateElement(event, pre)
})

function rotateElement(event, element) {
    //track the mouse
    const x = event.clientX;
    const y = event.clientY;
    // console.log(x, y);

    //find the middle of screen
    const middleX = window.innerWidth / 2;
    const middleY = window.innerHeight / 2;

    //get offset from middle
    const offsetX = ((x - middleX) / middleX) * 30;
    const offsetY = ((y - middleY) / middleY) * 30;

    element.style.setProperty("--rotateX", offsetX + 'deg');
    element.style.setProperty("--rotateY", -1 * offsetY + 'deg');
}
</script>
</html>
"""

@router.get("/")
async def get():
    return HTMLResponse(html)