TEMPLATE = """package:
  name: package_name
  output: ./output/

deck:
  name: Deck
  id: # put unique ID here

model:
  name: Model
  id: # put unique ID here
  css: |
    .question, .answer {
        text-align: center;
    }
    .question {
        font-size: 5rem;
        font-weight: 700;
    }
    .answer {
        font-size: 3rem;
    }
  templates:
    - name: Front
      qfmt: |
        <div class='question'>
        {{Question}}
        </div>
      afmt: |
        {{FrontSide}}
        <hr id='answer'>
        <div class='answer'>
        {{Answer}}
        </div>

scraping:
  urls:
    - # url 1
    # - url 2
    # - url 3
  queries:
    - name: Country
      query: .country
      many: true
      children:
        - name: Question
          query: .country-info
          regex: (Area .*)$
        - name: Answer
          query: .country-name"""
