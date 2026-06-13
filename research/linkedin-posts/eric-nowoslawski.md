# Eric Nowoslawski — LinkedIn Posts

---

## The ICP Prompt Loop

**Date:** Thu, 28 May 2026
**URL:** *(not available in source)*

I don't write prompts for list qualification anymore. Instead, I use a skill I call it the ICP prompt loop.

I tell Codex (or Claude Code): "This is the input I'll give you. This is the output I want. Write the prompt that makes that happen."

Then I feed it what we actually mean by giving it human verified data.

"This is what we count as a B2B SaaS company, this is what we count as manufacturing, this is what financial services means to this client, and so on"

Then it runs on 10 real companies and shows me its work: "This one is B2B SaaS. This one we thought was, but isn't, and here's why. This one is manufacturing and I agree."

I correct it. It revises the prompt.

The rule that makes it work: it does not get to run across the full dataset until it shows me 10 companies with zero edits from me, three times in a row.

One edit anywhere and the counter resets. It keeps feeding me 10 at a time until we get three clean rounds.

This week we used it on a 6-vertical TAM. Sonnet 4.6 on the batch API did the actual qualification for about $50 because there were too many companies for task sub-agents.

This way, you stop guessing whether your prompt is good and start proving it on the only thing that matters, real rows from your actual list.

---

## Crawling Thousands of Sites for Free

**Date:** Wed, 27 May 2026
**URL:** *(not available in source)*

We crawled thousands of websites for this list and paid nothing to actually read the pages and score them for ICP fit.

For a lot of jobs, you do not need a paid scraping API to get website text. An open-source HTML-to-text converter gets you the homepage and footer content fine.

Paid tools like ZenRows and Firecrawl earn their money on genuinely hard targets — heavy anti-bot, JS-gated content, sites that fight you. "I just want the text on this page" usually isn't that.

The second cost people add without thinking is AI scoring. We didn't score anything with a model here. We were matching specific compliance keywords in footers, that's deterministic.

A keyword match doesn't need an LLM, and bolting one on would have made it slower and more expensive for a worse answer.

So the run was: open-source text extraction, keyword matching, Claude Code orchestrating it in goal mode overnight. Ridiculously cheap for thousands of sites.

The general rule: every paid API and every AI call in a pipeline should have to justify why a free, deterministic step couldn't do it first. Most of them can't justify it.

They just got added because that's the default everyone copies.

Link here to the repo I used: https://lnkd.in/ex2un2Kb

---

## The List Is the Message

**Date:** Tue, 26 May 2026
**URL:** *(not available in source)*

The list is the message. I don't know who first said it, but it's one of the truest things in outbound.

When the list is segmented precisely enough, the email almost writes itself.

When it isn't, you end up writing clever copy to paper over the fact that you don't actually know who you're talking to.

Most platforms only let you segment by what a company is. Industry, size, tech stack.

Useful, but it rarely changes your message on its own. CEO vs founder doesn't change what you say. Industry often doesn't either.

What changes the message is who they sell to. A company selling into legal teams has a completely different world than one selling to restaurant owners — different buyers, different pain, different proof. That difference is the message.

Prospeo's v2 now lets you filter on exactly that. Who a company sells to, the size of their customers, the department they sell into. That's not a nice-to-have filter.

That's a segmentation axis that actually splits a list into groups that need different emails.

If a data point would change what you say, it's a reason to split into a separate campaign.

If it wouldn't, don't split. "Who do they sell to" almost always changes what you say.

---

## Prospeo v2 Update

**Date:** Wed, 20 May 2026
**URL:** *(not available in source)*

You can now target companies by who they sell to, keyword searches across the whole website, how companies show up for Google searches and more.

Second post about Prospeo's update comes with a video so you can see it here.

They asked me what filters would I want to see in the platform and they added so much great stuff.

Filter for companies that sell to small business owners, or sell to legal teams, or sell to marketing, plus the size of the companies they sell to and the market they're in.

And other things like —

1. Keyword search now reads the whole website — page bodies, titles, URLs, SEO descriptions — not just the company description. Huge difference in recall.

2. Business-model and type filters: SaaS, marketplace, e-comm, agency, consulting, manufacturing, plus flags like "has a public pricing page," "has an enterprise plan," "usage-based pricing."

3. AI attributes: do they offer a demo, do they have an API, do they have a blog.

4. Google Discovery: find companies by who ranks for a given keyword.

All of it is in the API, not just the UI.

Honest read on data quality: for a quick, well-defined list it's great. If you need a complete TAM exactly to spec, still pull the broad list and run your own website prompts to finish it.

As a fast starting point, I haven't seen filters like this anywhere else.

I go over all of the updates in the video update here.

---

## There Is No Such Thing as a "B2B SaaS" Filter

**Date:** Tue, 19 May 2026
**URL:** *(not available in source)*

There is no such thing as a "B2B SaaS" filter. There's no clean "e-commerce brand" one either. And if you pull "financial services," you will miss every bank.

This is why client vertical lists come back full of junk.

A few real examples from a TAM we built this week, US companies, 50–5,000 employees, six verticals:

Bacardi is an e-commerce/retail brand. It lists itself under beverage manufacturing. Hit just "retail" and you'll never see it.

Manufacturing and logistics companies notoriously aren't all on LinkedIn, and the ones that are file themselves under wild industries.

Healthcare is the worst. Pull "healthcare" and you've blended medical device makers, healthcare SaaS, hospitals, and health insurers into one pile that means nothing to the client.

Don't filter your way to a vertical, define it, then qualify into it.

We pull broad from our internal database and Prospeo's v2 type/business-model filters, merge and dedupe, then run every company through a written definition of what that vertical actually means to this specific client.

"Banks count as financial services here. Fintech does not."

This way we get more coverage on great companies and can toss out companies that say they are in Real Estate but are really services companies for real estate professionals and such.
