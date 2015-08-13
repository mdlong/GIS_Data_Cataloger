USE [CMTAGISStats]
GO

/****** Object:  Table [GDB].[Files]    Script Date: 8/13/2015 7:53:11 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [GDB].[Files](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](100) NULL,
	[Path] [nvarchar](500) NULL,
	[Type] [nvarchar](50) NULL,
	[Ext] [nvarchar](5) NULL,
	[Size] [float] NULL,
	[Created] [datetime] NULL,
	[Modified] [datetime] NULL,
	[CRC] [nchar](100) NULL
) ON [PRIMARY]

GO


