IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'TestDatabase')
BEGIN
  CREATE DATABASE TestDatabase;
END;
GO

USE TestDatabase;
GO

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='MyTable' AND xtype='U')
    CREATE TABLE MyTable (
        Id nvarchar(max) not null,
        Value nvarchar(max)
    )
GO

