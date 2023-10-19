# Chapter 15 - Implementing a Data Mesh Strategy

In this chapter we explored the concept of a data mesh approach to organizing data responsibilities within an organization. We started off by
examining the **four core principals** of a data mesh:

- Domain-orientated, decentralized data ownership
- Data as a product
- Self-service data infrastructure as a platform
- Federated computational governance

We then looked at how a data mesh approach can solve a number of challenges that exist with traditional data lake approaches. This included
understanding how a centralized data team can be a bottleneck, how traditionally product teams did not consider data analytics to be there
"problem", and how there was a lack of organization wide visibility into which datasets were available. 

We then reviewed the organizational and technical challenges of building a data mesh. This included a discussion of the difficulties of
changing the way that an organization traditionally appraoched data analytics, and how a data mesh approach changed the way that a
centralized data and analytics team worked. We then looked at the changes needed for line of business teams, and finally at how there
were a number of technical challenges to building a data mesh. 

After that we examined the AWS services that can help to build a data mesh, including a look at the **Amazon DataZone** service. 
We also reviewed a sample architecture for building a data mesh using both AWS services, and 3rd party services. 

## Hands-On Activity
In the hands-on section of this chapter we looked at how to setup Amazon DataZone, and how to publish data to the DataZone business catalog. 

#### Setting up AWS Identity Center

- AWS Management Console - AWS IAM Identity Center: https://us-east-2.console.aws.amazon.com/singlesignon/home

- Group to create: `DataZone Users`
- User to create: `film-catalog-team-admin`
- User to create: `marketing-team-admin`

#### Enabling and configuring Amazon DataZone

- AWS Management Console - Amazon DataZone Console: https://us-east-2.console.aws.amazon.com/datazone/home

#### Adding business metadata

- Business name for the film_category table: `Movie listings with category`
- Description for the film_category table: `This table contains a complete listing of all films in our streaming movie catalog, including category / genre information for each film, as well as a list of special features.`
- Description for the Category Name field: `This field contains the movie category / genre. Sample categories include Animation, Comedy, Sports, Children, Drama, Action, and more.`










