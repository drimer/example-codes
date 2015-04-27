build:
	javac src/MultiplesCounter.java
	javac -classpath . src/Main.java
	javac -classpath .:/usr/share/java/junit-3.8.2.jar test/TestGetSum.java

run: build
	java src.Main

clean:
	find . -name "*.class" | xargs rm -f

test: build
	java -cp .:/usr/share/java/junit-3.8.2.jar junit.textui.TestRunner test.TestGetSum
