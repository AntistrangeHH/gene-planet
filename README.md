Hello! 
Here are the list of steps you need to take to start the project. 

After cloning this repo from github, please do the following.

Go inside geneplanetApi and run following commands:
 - python3 manage.py makemigrations (to make database schema for model)
 - python3 manage.py migrate (to push them to database)

After that, inside seed_database.py script, on line 33th, give relative path to your VCF file. 
This should take some 5 minutes as script will push chunks of dataframes to database, where 
it needs to push around 85 million entries.

After the database is created, execute following queries for indexing the fields which will be main for searching the db:

CREATE INDEX "chrom" ON "geneplanetApi_genotype" (
	"chrom"
);

CREATE INDEX "chrom" ON "geneplanetApi_genotype" (
	"chrom_id"
);

CREATE INDEX "chrom" ON "geneplanetApi_genotype" (
	"pos"
);

After that you can try and run:
- python manage.py runserver 

And after server started, go to /index, where our html view is rendered, try search and best of luck! :)