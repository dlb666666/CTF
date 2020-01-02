# Official Solution:
`http://vulnerableweb.site/xss/xss.php?number='&name=<button id=keanu data-toggle=popover data-container=number data-content="'-alert(document.domain)//">`

# Official Explanation:
[1/6]
* 2 parameters `number` & `name`
* `number` can be only 1 character
* `name` can be anything, but DOMPurify is used to sanitize
* The site uses bootstrap
* Goal is to make our input somehow land inside the eval

[2/6]  
Clearly the `number` param is eval-ed, so before it lands inside
`eval`, can we append some data to it? To do this bootstrap has
a nice feature using popovers like using
`data-container` (https://getbootstrap.com/docs/4.0/components/popovers/),
so we set it to `number` tag.

[3/6]  
If  
`number=7` and  
`name=<button data-toggle=popover data-container=number data-content="blah blah">`  
the resulting number innerHTML will be  
`7<some popover template html code>blah blah<some popover template html code>`  

[4/6]  
So we just need to make it a valid javascript, because it's being eval-ed.  
`number='` and  
`name=<button data-toggle=popover data-container=number data-content="'-alert(1337)//">`

[5/6]  
resulting number innerHTML will be  
`'<some popover template html code>'-alert(1337)//<some popover template html code>`

now it's valid javascript that get's eval-ed.

[6/6]  
But the data we want to add won't be added unless the popover is shown, but
since there's a popover with the id #keanu where the show() is called on,
we can simply add the id #keanu


# My Subsequent Explanation and Takeaways:
1. We can't really get anywhere by trying to exploit the number field alone.
   `URLSearchParams.get()` will always return a string so
   `(new URL(location).searchParams.get('number') || "7")[0]` will always
   return a single character.
   At this point ideas like trying to set number to an array go out the window.

2. Number however *will* get eval'd at some point though, so this is still our
   attack target.  
   Since we can't directly set number to something exploitable via. the number
   GET parameter, we'll need to try to append to it or modify it via. the name
   GET parameter or some other vector.

3. The name GET parameter is geting sanitized by DOMPurify, so what can we use
   that won't get sanitized?  
   For some weird reason, DOMPurify will not remove `<button>` tags. It *will*
   however remove certian attributes like "onclick" if found inside the tag.  
   We need another supporting agent for this attack vector. Since Bootstrap is
   also being used, we can try to leverage it (but the reason why we think that
   bootstrap is a useful supporting agent is because of the next realization,
   particularly point 5).

4. Particularly, Bootstrap has "popovers" - elements based off of HTML
  `<button>` tags where we can indirectly specify what data we want to append
   to what DOM elements (containers).
   Some small points about attributes of popover buttons:
   1. Adding `data-toggle="popover"` to a button will classify it as a popover.
   2. `data-content`: the content to display when the popover is triggered. We
    can make this be our malicious payload
   3. `data-container`: specifies the ID of the DOM element to append the
    popover's data-content to. We can have this be our attack target, the
    `<number>` tag.


5. The reason why we are so interested in popovers instead of anything else is
   because popovers are already being used in the page with:
   `$('#keanu').popover('show')`.  
   So we can make another popover with it's ID as "keanu" and then it will
   automatically be shown (i.e. the data append functionality will be executed
   by the existing JavaScript).

6. Now it's time to design the payload.   
    If we ignored `number` and set `name` to:
    ```html
    <button id=keanu
      data-toggle=popover
      data-container=number
      data-content="alert(1337)">
    </button>
    ```
    Then the number field would contain:
    ```html
    <number id="number" style="display:none">
      7
      <div class="popover fade bs-popover-right show"
          role="tooltip" id="popover899396"
          x-placement="right"
          style="position: absolute;
                  transform: translate3d(138px, 407px, 0px);
                  top: 0px; left: 0px;
                  will-change: transform;">
        <div class="arrow" style="top: 0px;"></div>
        <h3 class="popover-header"></h3>
        <div class="popover-body">"alert(1337)"</div>
      </div>
    </number>
    ```
    for a while before the `$('#keanu').popover('hide')` part of the JavaScript
    executes.  
    But the alert code didn't execute... Why?
    It's because this massive innerHTML content is not valid JavaScript and the
    `eval` would fail. We need to get rid of all of the rubbish before and after
    the alert code.

7. All we now need to do (the final step) is to make the payload be valid
   JavaScript. We can use `data-content="alert(1337) //"` to comment out the
  `</button>` and other stuff that will come after the alert. Now we need to
  do something about the stuff that comes before it. We can only use a single
  character from the number field. So the idea here is to turn everything
  before the alert into a string and then try to do 'the massive string' -
  alert(1337). The result of the subtraction would be nonsense but alert(1337)
  would have been evaluated to perform the subbtraction in the first place.
  Thus we would have acheieved the intended XSS :)
  So the final payload is:
  `?number='&name=<button id=keanu data-toggle=popover data-container=number data-content="' - alert(1337) //"></button>`
  We could have used * or / in place of the - operator. But + would not have
  worked because after URL Decoding the "+" would be decoded into a space.
