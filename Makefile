wdi.sql:
	./proc_wdi.py > $@

.PHONY: clean
clean:
	rm -f wdi.sql
