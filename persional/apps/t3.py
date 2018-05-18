# -*- coding: utf-8 -*-

result = '''
Started by user xiazy
Building in workspace /home/xm/jenkins-workspace/workspace/xm-fsp20-cust
Cleaning local Directory .
Checking out svn://192.168.30.75/svnroot/platform2.0/trunk/fsp2.0/xm-fsp20-cust at revision '2018-05-17T16:27:52.662 +0800' --quiet
Using sole credentials zhenxin.ren/****** in realm ‘<svn://192.168.30.75:3690> 3687f8cf-0262-4051-a21e-25b16b9d025d’
At revision 62300

No revision recorded for svn://192.168.30.75/svnroot/platform2.0/trunk/fsp2.0/xm-fsp20-cust in the previous build
Parsing POMs
Failed to transfer Could not find artifact com.ximu.fsp20:xm-fsp20-parent:pom:1.0.0 in nexcus-release (http://10.8.8.5:8081/nexus/content/groups/public)
ERROR: Failed to parse POMs
org.apache.maven.project.ProjectBuildingException: Some problems were encountered while processing the POMs:
[FATAL] Non-resolvable parent POM: Could not find artifact com.ximu.fsp20:xm-fsp20-parent:pom:1.0.0 in nexcus-release (http://10.8.8.5:8081/nexus/content/groups/public) and 'parent.relativePath' points at wrong local POM @ line 9, column 10

	at org.apache.maven.project.DefaultProjectBuilder.build(DefaultProjectBuilder.java:364)
	at hudson.maven.MavenEmbedder.buildProjects(MavenEmbedder.java:361)
	at hudson.maven.MavenEmbedder.readProjects(MavenEmbedder.java:331)
	at hudson.maven.MavenModuleSetBuild$PomParser.invoke(MavenModuleSetBuild.java:1328)
	at hudson.maven.MavenModuleSetBuild$PomParser.invoke(MavenModuleSetBuild.java:1125)
	at hudson.FilePath.act(FilePath.java:997)
	at hudson.FilePath.act(FilePath.java:975)
	at hudson.maven.MavenModuleSetBuild$MavenModuleSetBuildExecution.parsePoms(MavenModuleSetBuild.java:986)
	at hudson.maven.MavenModuleSetBuild$MavenModuleSetBuildExecution.doRun(MavenModuleSetBuild.java:691)
	at hudson.model.AbstractBuild$AbstractBuildExecution.run(AbstractBuild.java:504)
	at hudson.model.Run.execute(Run.java:1724)
	at hudson.maven.MavenModuleSetBuild.run(MavenModuleSetBuild.java:543)
	at hudson.model.ResourceController.execute(ResourceController.java:97)
	at hudson.model.Executor.run(Executor.java:421)
Finished: FAILURE

'''
import re


result = re.search(r'Finished:(\s)(\S+)', result).group(2)
print result
