wdi.sql:
	./proc_wdi.py > $@

.PHONY: read
read:
	mysql devecondata < wdi.sql

.PHONY: clean
clean:
	rm -f wdi.sql
