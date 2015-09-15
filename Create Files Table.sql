USE [CMTAGISStats]
GO

/****** Object:  Table [GDB].[DataFiles]    Script Date: 9/15/2015 6:35:43 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [GDB].[DataFiles](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](150) NULL,
	[Path] [nvarchar](500) NULL,
	[Type] [nvarchar](50) NULL,
	[Ext] [nvarchar](5) NULL,
	[Size] [float] NULL,
	[Created] [datetime] NULL,
	[Modified] [datetime] NULL,
	[CRC] [nchar](100) NULL
) ON [PRIMARY]

GO


