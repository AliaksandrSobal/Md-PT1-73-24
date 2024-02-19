# 1. Prepare to read the contents of the file text.txt
# 2. Allow the user to enter a parameter "maximum number of characters per line", which must be greater than 35.
# 3. Format the text taking into account the maximum number of characters, but if a word does not fit entirely on a line, it should be moved to the next one,
#    and the spacing between words should be evenly increased (similarly to the "Justify" function in text editors). There is a module called 
#    ‘textwrap’ which can do it, you may take a look at it but do not use for this task.
# 4. Write the resulting text to a new file and notify the user about it.

def format_text(text, max_chars):
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + word) <= max_chars:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    
    lines.append(current_line.strip())
    
    formatted_lines = []
    for line in lines:
        words = line.split()
        num_words = len(words)
        
        if num_words <= 1:
            formatted_lines.append(line)
        else:
            num_spaces = max_chars - sum(len(word) for word in words)
            num_gaps = num_words - 1
            spaces_per_gap = num_spaces // num_gaps
            remaining_spaces = num_spaces % num_gaps
            
            formatted_line = words[0]
            for i in range(1, num_words):
                gap_spaces = spaces_per_gap + 1 if i <= remaining_spaces else spaces_per_gap
                formatted_line += " " * gap_spaces + words[i]
            
            formatted_lines.append(formatted_line)
    
    formatted_text = "\n".join(formatted_lines)
    return formatted_text


text =  ("""The  February  TIOBE  Index of the most
            popular  programming  languages is out,
            and  while  the  work  going  on in the
            background  of TIOBE’s calculations has
            changed,  not  much  has shifted in the
            way of rankings.
            Python continues to sit atop the index,
            with  C and Java directly behind it. In
            Feb.  2021,  those  three also occupied
            the  top  spot,  but with Python in the
            number  three  position,  C at top, and
            Java in second place.
            Beyond the top three, there hasn’t been
            much   movement   in  the  index,  with
            positions  four through eight unchanged
            from  the  same  time  last year. Those
            slots  are  occupied,  respectively, by
            C++,  C#,  Visual Basic, JavaScript and
            PHP. Positions nine and 10 swapped from
            Feb.  21 to now, with Assembly Language
            and  SQL  now  occupying  each  other’s
            positions.
            The  one  big move of note between Feb.
            2021  and Feb. 2022 was with the Groovy
            programming         language,        an
            object-oriented language for Java. Over
            the  course  of  the  year, Groovy fell
            from 12th position all the way to 20th,
            putting  it  perilously  close  to  the
            “other programming languages” list.
            TIOBE   CEO   Paul   Jansen  attributes
            Groovy’s  decline  to the growth in the
            CI/CD   space.   Groovy  was  the  only
            language  used  for  writing scripts on
            Jenkins,   which  Jansen  describes  as
            having  been  “the  only real player in
            the  CI/CD  domain” early on. Now, with
            platforms  that  don’t  require Groovy,
            like  GitHub,  Azure DevOps and GitLab,
            Groovy  is  losing  its  place  at  the
            table.
            “Groovy   could   have   grown  further
            because  it  was the major script-based
            alternative  for  Java  running  on the
            same  JVM.  However,  Kotlin  is taking
            over  that  position  right  now,  so I
            think  Groovy  will  have a hard time,”
            Jensen said.
            The  TIOBE  index  may  not  be full of
            surprises  this  month,  but Jansen did
            have  a  lot  to  say  about  the index
            itself this month, as this is the first
            time   it   has   been  compiled  using
            Similarweb’s  traffic analysis platform
            instead of Alexa.
            “We  have used Similarweb for the first
            time   this   month  to  select  search
            engines  and  fortunately, there are no
            big  changes  in  the index due to this
            swap.  The  only striking difference is
            that  the  top  3 languages, Python, C,
            and   Java,  all  gained  more  than  1
            percent in the rankings,” Jansen said.
            TIOBE  decided  to make the switch this
            month  after  Amazon’s  announcement in
            December  2021 that it was shutting the
            Alexa   web   ranking   service   down,
            effective  May 1, 2022, ending 25 years
            of the program.
            Jansen noted that not every website has
            been  onboarded, but that the switch to
            Similarweb  included  a switch to using
            HtmlUnit,  a  non-GUI  web browser with
            APIs  that  let Java apps invoke pages,
            fill  forms  and  do other standard web
            browsing  activity.  This  switch  will
            eventually   allow   TIOBE  to  include
            websites it was unable to crawl before,
            like  Stackoverflfow  and Github, which
            could have a larger impact on scores.""")

max_chars = int(input("Введите максимальное количество символов в одной строке: "))
formatted_text = format_text(text, max_chars)

print(formatted_text)