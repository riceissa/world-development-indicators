MYSQL_ARGS=
DATABASE=devecondata

wdi.sql:
	./proc_wdi.py > $@

.PHONY: read
read:
	mysql $(MYSQL_ARGS) $(DATABASE) < wdi.sql

.PHONY: clean
clean:
	rm -f wdi.sql
