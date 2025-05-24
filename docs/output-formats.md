## 📄 Output Formats

JSON Example

Get `json` version

```python
from scrapesome.scraper.sync_scraper import scraper
content = scraper("https://example.com", format_type="json")
content
```

Output

```json
{
  "title": "Example Domain",
  "description": "This domain is for use in illustrative examples.",
  "url": "https://example.com"
}
```

## Markdown

Convert HTML to Markdown with:

```python
from scrapesome.scraper.sync_scraper import scraper
content = scraper("https://example.com", format_type="markdown")
content
```
Output

```text
# Online Global Masters that boost your global career

**ADEN University** offers students access to professionals who operate in the world of business and administration, who share their knowledge and acumen collaboratively with their students in all **academic programs** offered at ADEN.

[About Us](about-aden-university)


Watch testimonial video 


##### Watch testimonial video

×

[

](https://res.cloudinary.com/cruminott/video/upload/vc_auto,w_auto,q_auto,f_auto/adenu/aden-university-3.mp4)



## ADEN University offers the following academic programs

[![EXECUTIVE MBA. Master of Business Administration](https://adenuniversity.us/files/2016/06/ADENU_miniatura_Emba_900-1-820x400.jpg "EXECUTIVE MBA. Master of Business Administration")](https://adenuniversity.us/academics/executive-mba/  "EXECUTIVE MBA. Master of Business Administration")

##### [EXECUTIVE MBA. Master of Business Administration](https://adenuniversity.us/academics/executive-mba/ "EXECUTIVE MBA. Master of Business Administration")

The ADEN University Executive MBA is designed to strengthen business leaders to manage...

* **37** credits
* **15** months
* **Spanish Only**

[Visit EMBA Course](https://adenuniversity.us/academics/executive-mba/ "EXECUTIVE MBA. Master of Business Administration")

[![GLOBAL MBA. Master of Business Administration](https://adenuniversity.us/files/2016/06/ADENU_miniatura_MBAgl1_900-820x400.jpg "GLOBAL MBA. Master of Business Administration")](https://adenuniversity.us/academics/global-mba/  "GLOBAL MBA. Master of Business Administration")

##### [GLOBAL MBA. Master of Business Administration](https://adenuniversity.us/academics/global-mba/ "GLOBAL MBA. Master of Business Administration")

The Global MBA is designed to prepare business leaders to manage companies in an...

* **36** credits
* **14** months
* **Spanish and English**
```

Similarly async can also be used.